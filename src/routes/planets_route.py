from flask import Blueprint, jsonify, request
from models import Planet

planets_bp = Blueprint('planets_custom', __name__, url_prefix='/planets')

@planets_bp.route('/', methods=['GET'])
def get_planets():
    raw_planets_list = Planet.query.all()
    planets = [planet.serialize() for planet in raw_planets_list]
    return planets, 200

@planets_bp.route('/<int:planet_id>', methods=['GET'])
def get_planet_by_id(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
        return jsonify({"error": "Planet not found"}), 404
    return jsonify(planet.serialize()), 200