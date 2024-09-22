from mongoengine import connect

def initialize_databases():
    connect(alias='users_db', db='users_db', host='mongodb://localhost/users_db')
    connect(alias='products_db', db='products_db', host='mongodb://localhost/products_db')
    connect(alias='orders_db', db='orders_db', host='mongodb://localhost/orders_db')
    connect(alias='inventory_db', db='inventory_db', host='mongodb://localhost/inventory_db')
    connect(alias='logs_db', db='logs_db', host='mongodb://localhost/logs_db')
