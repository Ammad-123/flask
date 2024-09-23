from flask import Flask, request,jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# Step 1: Configure the SQLAlchemy Database URI (SQLite in this case)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning

#initializing sql alchem
db = SQLAlchemy(app)


# defining a model which represent table
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),unique=True, nullable=False)

@app.route('/')
def index():
    return "app running...."


@app.route('/add_user')
def add_user():
    user = User(name='Ikram',email='ikram@gmail.com')
    db.session.add(user) # add user to the session
    db.session.commit()  # commit transaction to the database
    return "User added!" 

@app.route('/list_user')
def list_user():
    users = User.query.all()
    return {user.id:{"name":user.name,"email":user.email}for user in users}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()   # create the database and table
    app.run(debug=True)


