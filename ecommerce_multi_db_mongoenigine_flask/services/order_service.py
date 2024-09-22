from models.order import Order
from mongoengine.errors import DoesNotExist, ValidationError

# Get all orders
def get_all_orders():
    try:
        return Order.objects().to_json()
    except Exception as e:
        return str(e)

# Get order by ID
def get_order_by_id(order_id):
    try:
        order = Order.objects.get(order_id=order_id)
        return order.to_json()
    except DoesNotExist:
        return f"Order with ID {order_id} does not exist"
    except ValidationError as e:
        return str(e)

# Create a new order
def create_order(data):
    try:
        order = Order(**data).save()
        return order.to_json()
    except ValidationError as e:
        return str(e)

# Update an existing order by ID
def update_order(order_id, data):
    try:
        order = Order.objects.get(order_id=order_id)
        order.update(**data)
        return f"Order with ID {order_id} updated successfully"
    except DoesNotExist:
        return f"Order with ID {order_id} does not exist"
    except ValidationError as e:
        return str(e)

# Delete an order by ID
def delete_order(order_id):
    try:
        order = Order.objects.get(order_id=order_id)
        order.delete()
        return f"Order with ID {order_id} deleted successfully"
    except DoesNotExist:
        return f"Order with ID {order_id} does not exist"
    except ValidationError as e:
        return str(e)
