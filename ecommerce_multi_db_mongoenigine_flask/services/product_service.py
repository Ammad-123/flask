from models.product import Product
from mongoengine.errors import DoesNotExist, ValidationError

# Get all products
def get_all_products():
    try:
        return Product.objects().to_json()
    except Exception as e:
        return str(e)

# Get product by ID
def get_product_by_id(product_id):
    try:
        product = Product.objects.get(product_id=product_id)
        return product.to_json()
    except DoesNotExist:
        return f"Product with ID {product_id} does not exist"
    except ValidationError as e:
        return str(e)

# Create a new product
def create_product(data):
    try:
        product = Product(**data).save()
        return product.to_json()
    except ValidationError as e:
        return str(e)

# Update an existing product by ID
def update_product(product_id, data):
    try:
        product = Product.objects.get(product_id=product_id)
        product.update(**data)
        return f"Product with ID {product_id} updated successfully"
    except DoesNotExist:
        return f"Product with ID {product_id} does not exist"
    except ValidationError as e:
        return str(e)

# Delete a product by ID
def delete_product(product_id):
    try:
        product = Product.objects.get(product_id=product_id)
        product.delete()
        return f"Product with ID {product_id} deleted successfully"
    except DoesNotExist:
        return f"Product with ID {product_id} does not exist"
    except ValidationError as e:
        return str(e)
