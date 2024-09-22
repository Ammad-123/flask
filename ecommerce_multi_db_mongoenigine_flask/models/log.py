from mongoengine import Document, StringField, ReferenceField, DateTimeField

class Log(Document):
    meta = {'db_alias': 'logs_db'}
    
    event_type = StringField(required=True)
    description = StringField()
    user = ReferenceField('User', required=False)  # Optional
    order = ReferenceField('Order', required=False)  # Optional
    
    timestamp = DateTimeField(required=True)
    ip_address = StringField()
    device_info = StringField()
