import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost:5432/stocks')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POLYGON_APY_KEY = os.getenv('POLYGON_API_KEY', 'bmN7i7CrzrpKqFvgbB1fEaztCwZKSUjJ')