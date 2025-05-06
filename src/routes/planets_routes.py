from flask import Blueprint, jsonify, request
from models import Planet

planets_bp = Blueprint('planets', __name__, url_prefix='/planets')

@planets_bp.route('/', methods=['GET'])
def get_planets():
    raw_planets_list = Planet.get_all_planets()
    planets = [planet.serialize() for planet in raw_planets_list]
    return planets, 200
# jsonify({"message": "Lista de planetas"})

# @planets_bp.route('/<int:planet_id>', methods=['GET'])
# def get_planet_by_id(planet_id):
#     return jsonify()

# @planets_bp.route('/', methods=['POST'])
# def create_planet():
#     data = request.get_json()
#     return jsonify(), 201

# @planets_bp.route('/<int:planet_id>', methods=['PUT'])
# def update_planet(planet_id):
#     data = request.get_json()
#     return jsonify()

# @planets_bp.route('/<int:planet_id>', methods=['DELETE'])
# def delete_planet(planet_id):
#     return jsonify()