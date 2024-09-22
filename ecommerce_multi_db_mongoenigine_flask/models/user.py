from mongoengine import Document, StringField, DictField, ListField, ReferenceField, DateTimeField

class User(Document):
    meta = {'db_alias': 'users_db'}
    
    user_id = StringField(required=True, unique=True)
    name = StringField(required=True)
    email = StringField(required=True, unique=True)
    password_hash = StringField(required=True)
    phone_number = StringField()
    
    shipping_address = DictField()  # Address dictionary
    billing_address = DictField()  # Address dictionary
    
    payment_methods = ListField(DictField())  # List of payment methods
    
    order_history = ListField(ReferenceField('Order'))
    
    wishlist = ListField(ReferenceField('Product'))
    
    created_at = DateTimeField()
    updated_at = DateTimeField()
