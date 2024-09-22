from flask import Blueprint, request, jsonify
from models.order import Order

order_routes = Blueprint('order_routes', __name__)

@order_routes.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.objects().to_json()
    return orders

@order_routes.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    order = Order(**data).save()
    return jsonify(order.to_json()), 201
