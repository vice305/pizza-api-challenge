from flask import jsonify, request
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza
from server.app import app, db

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{"id": r.id, "name": r.name, "address": r.address} for r in restaurants])

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    pizzas = [{"id": rp.pizza.id, "name": rp.pizza.name, "ingredients": rp.pizza.ingredients} for rp in restaurant.restaurant_pizzas]
    return jsonify({"id": restaurant.id, "name": restaurant.name, "address": restaurant.address, "pizzas": pizzas})

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204