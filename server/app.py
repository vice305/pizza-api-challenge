from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from server.models import restaurant, pizza, restaurant_pizza
from server.controllers import restaurant_controller, pizza_controller, restaurant_pizza_controller

if __name__ == '__main__':
    app.run(port=8050)