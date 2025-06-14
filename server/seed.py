from server.app import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="Pizza Palace", address="123 Pizza Lane")
    r2 = Restaurant(name="Dough Delight", address="456 Dough St")
    db.session.add_all([r1, r2])

    p1 = Pizza(name="Margherita", ingredients="Tomato, Basil, Mozzarella")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato, Pepperoni, Cheese")
    db.session.add_all([p1, p2])

    rp1 = RestaurantPizza(price=8, restaurant_id=1, pizza_id=1)
    rp2 = RestaurantPizza(price=10, restaurant_id=2, pizza_id=2)
    db.session.add_all([rp1, rp2])

    db.session.commit()