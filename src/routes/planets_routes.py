from flask import Blueprint, jsonify, request
from models import Planet

planets_bp = Blueprint('planets', __name__, url_prefix='/planets')

@planets_bp.route('/', methods=['GET'])
def get_planets():
    raw_planets_list = Planet.get_all_planets()
    planets = [planet.serialize() for planet in raw_planets_list]
    return planets, 200