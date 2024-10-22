from flask import Blueprint, request, jsonify
from services.stock_service import get_stock_data, update_purchased_amount

stock_bp = Blueprint('stock', __name__)

@stock_bp.route('/stock/<stock_symbol>', methods=['GET'])
def get_stock(stock_symbol):
    date = request.args.get('date', '2024-10-22')
    stock_data = get_stock_data(stock_symbol, date)
    
    if stock_data['status'] == 'available':
        return jsonify(stock_data)
    else:
        return jsonify({"error": stock_data["message"]}), 404

@stock_bp.route('/stock/<stock_symbol>', methods=['POST'])
def update_stock(stock_symbol):
    amount = request.json.get('amount')
    if amount is None:
        return jsonify({"error": "Invalid request, 'amount' required"}), 400
    
    message = update_purchased_amount(stock_symbol, amount)
    return jsonify({"message": message}), 201