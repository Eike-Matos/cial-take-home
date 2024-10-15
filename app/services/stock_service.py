import requests
from bs4 import BeautifulSoup
from utils.cache import cached

POLYGON_API_KEY = 'bmN7i7CrzrpKqFvgbB1fEaztCwZKSUjJ'

@cached
def get_stock_data_from_polygon(stock_symbol, date):
    url = f"https://api.polygon.io/v1/open-close/{stock_symbol}/{date}"
    headers = {'Authorization': f'Bearer {POLYGON_API_KEY}'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "open": data['open'],
            "high": data['high'],
            "low": data['low'],
            "close": data['close']
        }
    return None

@cached
def scrape_marketwatch(stock_symbol):
    url = f'https://www.marketwatch.com/investing/stock/{stock_symbol}'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        performance_data = {}  
        competitors = []  
        return {
            "performance_data": performance_data,
            "competitors": competitors
        }
    return None

def get_stock_data(stock_symbol, date):
    stock_values = get_stock_data_from_polygon(stock_symbol, date)
    marketwatch_data = scrape_marketwatch(stock_symbol)
    
    if stock_values and marketwatch_data:
        return {
            "status": "available",
            "purchased_amount": 0,
            "purchased_status": "not purchased",
            "request_data": date,
            "company_code": stock_symbol.upper(),
            "company_name": "Company Placeholder", 
            "performance_data": marketwatch_data['performance_data'],
            "competitors": marketwatch_data['competitors']
        }
    return {"status": "error", "message": "Could not retrieve stock data"}

def update_purchased_amount(stock_symbol, amount):
    return f"{amount} units of stock {stock_symbol} were added to your stock record"