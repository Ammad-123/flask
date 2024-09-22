from mongoengine import Document, StringField, FloatField, ListField, DictField, ReferenceField, DateTimeField

class Order(Document):
    meta = {'db_alias': 'orders_db'}
    
    order_id = StringField(required=True, unique=True)
    user = ReferenceField('User', reverse_delete_rule='CASCADE')
    
    items = ListField(DictField())  # List of products with quantity and price
    
    total_amount = FloatField(required=True)
    payment_status = StringField(choices=['Pending', 'Completed', 'Failed'])
    payment_method = DictField()  # Payment method details
    
    shipping_address = DictField()
    shipping_status = StringField(choices=['Pending', 'Shipped', 'Delivered', 'Cancelled'])
    shipping_method = StringField()
    tracking_number = StringField()
    
    ordered_at = DateTimeField(required=True)
    shipped_at = DateTimeField()
    delivered_at = DateTimeField()
