import requests
from bs4 import BeautifulSoup
from utils.cache import cached

POLYGON_API_KEY = 'bmN7i7CrzrpKqFvgbB1fEaztCwZKSUjJ'

@cached
def get_stock_data_from_polygon(stock_symbol, date):
    url = f"https://api.polygon.io/v1/open-close/{stock_symbol}/{date}"
    headers = {'Authorization': f'Bearer {POLYGON_API_KEY}'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        
        data = response.json()
        
        if all(key in data for key in ('open', 'high', 'low', 'close')):
            return {
                "open": data['open'],
                "high": data['high'],
                "low": data['low'],
                "close": data['close']
            }
        else:
            raise ValueError("Dados incompletos da API da Polygon.")
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer requisição para a API da Polygon: {e}")
        return None
    except ValueError as e:
        print(f"Erro de validação: {e}")
        return None

@cached
def scrape_marketwatch(stock_symbol):
    url = f'https://www.marketwatch.com/investing/stock/{stock_symbol}'
    
    try:
        response = requests.get(url)
        response.raise_for_status() 

        soup = BeautifulSoup(response.text, 'html.parser')
        
        performance_data = {
            "five_days": None,  
            "one_month": None,
            "three_months": None,
            "year_to_date": None,
            "one_year": None
        }
        
        competitors = [
            {
                "name": "Competitor Placeholder",
                "market_cap": {
                    "currency": "USD",
                    "value": 1000000.00
                }
            }
        ]
        
        return {
            "performance_data": performance_data,
            "competitors": competitors
        }
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer scraping da MarketWatch: {e}")
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
            "stock_values": stock_values,
            "performance_data": marketwatch_data['performance_data'],
            "competitors": marketwatch_data['competitors']
        }
        
    return {"status": "error", "message": "Could not retrieve stock data"}

def update_purchased_amount(stock_symbol, amount):
    return f"{amount} units of stock {stock_symbol} were added to your stock record"