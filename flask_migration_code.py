from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


#initialize app
app = Flask(__name__)


# db configurations
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///example.db"
#initialize sqlalchemy
db = SQLAlchemy(app)

# initialize migration
migrate = Migrate(app,db)

# Create user model
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    age= db.Column(db.Integer())


if __name__ == "__main__":
    app.run(debug=True)