from models.inventory import Inventory
from mongoengine.errors import DoesNotExist, ValidationError

# Get all inventory items
def get_all_inventory():
    try:
        return Inventory.objects().to_json()
    except Exception as e:
        return str(e)

# Get inventory by product ID
def get_inventory_by_product_id(product_id):
    try:
        inventory_item = Inventory.objects.get(product__product_id=product_id)
        return inventory_item.to_json()
    except DoesNotExist:
        return f"Inventory for product with ID {product_id} does not exist"
    except ValidationError as e:
        return str(e)

# Create a new inventory entry
def create_inventory(data):
    try:
        inventory_item = Inventory(**data).save()
        return inventory_item.to_json()
    except ValidationError as e:
        return str(e)

# Update an existing inventory entry by product ID
def update_inventory(product_id, data):
    try:
        inventory_item = Inventory.objects.get(product__product_id=product_id)
        inventory_item.update(**data)
        return f"Inventory for product with ID {product_id} updated successfully"
    except DoesNotExist:
        return f"Inventory for product with ID {product_id} does not exist"
    except ValidationError as e:
        return str(e)

# Delete inventory by product ID
def delete_inventory(product_id):
    try:
        inventory_item = Inventory.objects.get(product__product_id=product_id)
        inventory_item.delete()
        return f"Inventory for product with ID {product_id} deleted successfully"
    except DoesNotExist:
        return f"Inventory for product with ID {product_id} does not exist"
    except ValidationError as e:
        return str(e)
