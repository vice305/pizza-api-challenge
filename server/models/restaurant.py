from server.app import db

class Restaurant(db.Model):
         __tablename__ = 'restaurant'
         id = db.Column(db.Integer, primary_key=True)
         name = db.Column(db.String(50), nullable=False)
         address = db.Column(db.String(100), nullable=False)
         restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant', lazy=True, cascade="all, delete-orphan")