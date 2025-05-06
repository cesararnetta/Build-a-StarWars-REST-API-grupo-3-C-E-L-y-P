from flask import Blueprint, jsonify, request
from models import Favorite, db

favorite_bp = Blueprint('favorites', __name__, url_prefix='/favorite')

@favorite_bp.route('/planet/<int:planet_id>', methods=['DELETE'])
def delete_fav_planet(planet_id):
    try:
        favorite = Favorite.query.filter_by(planets_id=planet_id).first()

        if favorite is None:
            return jsonify({"error": "Favorite planet not found"}), 404

        db.session.delete(favorite)
        db.session.commit()

        return jsonify({"msg": f"Favorite planet {planet_id} deleted"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "An error occurred", "details": str(e)}), 500



@favorite_bp.route('/people/<int:character_id>', methods=['DELETE'])
def delete_fav_planet(character_id):
    try:
        favorite = Favorite.query.filter_by(characters_id=character_id).first()

        if favorite is None:
            return jsonify({"error": "Favorite planet not found"}), 404

        db.session.delete(favorite)
        db.session.commit()

        return jsonify({"msg": f"Favorite planet {character_id} deleted"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "An error occurred", "details": str(e)}), 500
