from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)


    def __init__(self, price, restaurant_id, pizza_id):
        if not (1 <= price <= 30):
            raise ValueError("Price must be between 1 and 30")
        self.price = price
        self.restaurant_id = restaurant_id
        self.pizza_id = pizza_id