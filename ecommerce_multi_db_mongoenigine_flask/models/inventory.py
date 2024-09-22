from mongoengine import Document, IntField, DateTimeField, ReferenceField

class Inventory(Document):
    meta = {'db_alias': 'inventory_db'}
    
    product = ReferenceField('Product', reverse_delete_rule='CASCADE')
    stock_available = IntField(required=True)
    stock_reserved = IntField(default=0)
    
    stock_threshold = IntField(default=10)
    restock_date = DateTimeField()
    
    last_updated = DateTimeField()
