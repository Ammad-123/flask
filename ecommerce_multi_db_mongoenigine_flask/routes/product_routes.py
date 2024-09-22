from flask import Blueprint, request, jsonify
from models.product import Product

product_routes = Blueprint('product_routes', __name__)

@product_routes.route('/products', methods=['GET'])
def get_products():
    products = Product.objects().to_json()
    return products

@product_routes.route('/products', methods=['POST'])
def create_product():
    data = request.json
    product = Product(**data).save()
    return jsonify(product.to_json()), 201
