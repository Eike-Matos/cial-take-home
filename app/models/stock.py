from app import db 

class StockModel(db.Model):
    __tablename__ = 'stocks'
    
    id = db.Column(db.Integer, primary_key = True)
    company_code = db.Column(db.String, nullable=False)
    purchased_amount = db.Column(db.Integer, default=0)
    purchased_status = db.Column(db.String, default='not purchased')
    request_data = db.Column(db.Date, nullable=False)
    company_name = db.Column(db.String, nullable=False)