
from models.user import User
from mongoengine.errors import DoesNotExist, ValidationError

# Get all users
def get_all_users():
    try:
        return User.objects().to_json()
    except Exception as e:
        return str(e)

# Get user by ID
def get_user_by_id(user_id):
    try:
        user = User.objects.get(user_id=user_id)
        return user.to_json()
    except DoesNotExist:
        return f"User with ID {user_id} does not exist"
    except ValidationError as e:
        return str(e)

# Create a new user
def create_user(data):
    try:
        user = User(**data).save()
        return user.to_json()
    except ValidationError as e:
        return str(e)

# Update an existing user by ID
def update_user(user_id, data):
    try:
        user = User.objects.get(user_id=user_id)
        user.update(**data)
        return f"User with ID {user_id} updated successfully"
    except DoesNotExist:
        return f"User with ID {user_id} does not exist"
    except ValidationError as e:
        return str(e)

# Delete a user by ID
def delete_user(user_id):
    try:
        user = User.objects.get(user_id=user_id)
        user.delete()
        return f"User with ID {user_id} deleted successfully"
    except DoesNotExist:
        return f"User with ID {user_id} does not exist"
    except ValidationError as e:
        return str(e)
