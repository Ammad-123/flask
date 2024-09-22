from flask import Flask
from config import initialize_databases
# from routes import product_routes, user_routes, order_routes, inventory_routes
from routes.product_routes import product_routes  # Correctly import the blueprint
from routes.user_routes import user_routes
from routes.order_routes import order_routes
from routes.inventory_routes import inventory_routes

app = Flask(__name__)

# Initialize the database connections
initialize_databases()

# Register blueprints (routes)
app.register_blueprint(product_routes)
app.register_blueprint(user_routes)
app.register_blueprint(order_routes)
app.register_blueprint(inventory_routes)

if __name__ == '__main__':
    app.run(debug=True)
