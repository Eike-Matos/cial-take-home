from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Stock(db.Model):
    __tablename__ = 'stocks'
    
    id = db.Column(db.Integer, primary_key=True, index=True)
    status = db.Column(db.String)
    purchased_amount = db.Column(db.Integer)
    purchased_status = db.Column(db.String)
    request_data = db.Column(db.Date)
    company_code = db.Column(db.String)
    company_name = db.Column(db.String)
    stock_values = db.Column(db.JSON)
    performance_data = db.Column(db.JSON)
    competitors = db.Column(db.JSON)
    market_cap = db.Column(db.JSON)
    currency = db.Column(db.String)
    value = db.Column(db.Float)