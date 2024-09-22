from flask import Blueprint, request, jsonify
from models.inventory import Inventory

inventory_routes = Blueprint('inventory_routes', __name__)

@inventory_routes.route('/inventory', methods=['GET'])
def get_inventory():
    inventory = Inventory.objects().to_json()
    return inventory

@inventory_routes.route('/inventory', methods=['POST'])
def update_inventory():
    data = request.json
    inventory_item = Inventory(**data).save()
    return jsonify(inventory_item.to_json()), 201
