from mongoengine import Document, StringField, FloatField, IntField, ListField, DateTimeField, DictField

class Product(Document):
    meta = {'db_alias': 'products_db'}
    
    product_id = StringField(required=True, unique=True)
    name = StringField(required=True)
    description = StringField()
    category = StringField()
    brand = StringField()
    
    price = FloatField(required=True)
    discount = FloatField()
    
    image_urls = ListField(StringField())  # URLs to product images
    video_url = StringField()
    
    stock = IntField(default=0)
    
    average_rating = FloatField(default=0.0)
    reviews = ListField(DictField())  # List of reviews
    
    created_at = DateTimeField()
    updated_at = DateTimeField()
