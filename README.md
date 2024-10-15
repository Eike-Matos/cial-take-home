# Stock API Application

This is a Python-based REST API project that retrieves stock data from an external financial API (Polygon.io) and performs data scraping from the MarketWatch website. The application allows users to fetch stock data and update the purchased amount of stocks, with data persistence in a PostgreSQL database.

## Features

- Fetch stock open/close prices from the Polygon.io API.
- Scrape performance and competitor data from the MarketWatch website.
- Update the purchased amount of stocks with persistence in a PostgreSQL database.
- Caching mechanism to optimize repeated requests for the same stock data.
- Dockerized for easy deployment.
- Unit tests included for core functionalities.

## Requirements

- Python 3.10 or above
- PostgreSQL
- Docker

## Installation and Setup

### 1. Clone the repository
- git clone https://github.com/yourusername/stock-api.git
- cd stock-api

### 2. Set up a virtual environment
- python3 -m venv venv
- source venv/bin/activate

### 3. Install dependencies
- pip install -r requirements.txt

### 4. Set up the PostgreSQL database
- psql
- CREATE DATABASE stocks;
- in the config.py file, make sure the SQLALCHEMY_DATABASE_URI is correctly set: SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost:5432/stocks'

### 5. Run database migrations if needed
- flask db upgrade

### 6. Run the application locally
- python app.py

### API ENDPOINT

Fetch stock data for a given stock symbol. The data includes the stock open/close values, performance data, and competitors’ information.

- GET /stock/AAPL
- Example of response: {
    "status": "available",
    "company_code": "AAPL",
    "company_name": "Apple Inc.",
    "stock_values": {
        "open": 145.67,
        "high": 146.34,
        "low": 144.56,
        "close": 145.23
    },
    "performance_data": {
        "five_days": 1.5,
        "one_month": 3.0,
        "three_months": 6.2,
        "year_to_date": 12.4,
        "one_year": 25.3
    },
    "competitors": [
        {
            "name": "Microsoft Corporation",
            "market_cap": {
                "currency": "USD",
                "value": 2500000000
            }
        }
    ]
}

- POST /stock/AAPL
{
    "amount": 5
}
- Example of response: {
    "message": "5 units of stock AAPL were added to your stock record"
}

### Running with Docker

- docker build -t stock-api
- docker run -p 8000:8000 stock-api

### Running Unit Test
- pytest

### Logging
The application logs requests and errors to help monitor the API’s activity. Logs are printed to the console by default but can be configured to write to files or external logging services.
