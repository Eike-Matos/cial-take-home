from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.stock_routes import stock_bp

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

#Register of routes
app.register_blueprint(stock_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)