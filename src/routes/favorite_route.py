from flask import request, jsonify, Blueprint
from models import db, Planet, User, Favorite, Character

favorite_bp = Blueprint('favorite_custom', __name__, url_prefix='/favorite')

# [POST] /favorite/planet/<int:planet_id> César
print(__name__)

@favorite_bp.route('/planet/<int:planet_id>', methods=['POST'])
def add_favorite(planet_id):
    data_request = request.get_json()
    print(data_request)
    if "users_id" not in data_request:
        return jsonify({"error": "Es obligatorio que en el body del post estén los campos: users_id"}), 400
    planets = Planet.query.get(planet_id)
    print(planets)
    if not planets:
        return jsonify({"error": "No se ha encontrado planets_id"}), 400
    users_id = data_request["users_id"]
    users = User.query.get(users_id)
    print(users)
    if not users:
        return jsonify({"error": "No se ha encontrado users_id"}), 400

    new_favorite = Favorite(
        users_id=users_id,
        planets_id=planet_id,
        characters_id=None
    )

    try:
        db.session.add(new_favorite)
        db.session.commit()
        return jsonify({"message": "Favorite añadido"})
    except Exception as e:
        db.session.rollback()
        print("Error", e)
        return jsonify({"error": "No se ha agregado el favorite"})


@favorite_bp.route('/planet/<int:planet_id>', methods=['DELETE'])
def delete_fav_planet(planet_id):
    favorite = Favorite.query.filter_by(planets_id=planet_id).first()

    if favorite is None:
        return jsonify({"error": "Favorite planet not found"}), 404

    db.session.delete(favorite)
    db.session.commit()

    return jsonify({"message": f"Favorite planet {planet_id} deleted"}), 200


# [POST] /favorite/people/<int:people_id>

@favorite_bp.route('/people/<int:people_id>', methods=['POST'])
def add_favorite_people(people_id):
    data_request = request.get_json()
    print(data_request)
    if "users_id" not in data_request:
        return jsonify({"error": "Es obligatorio que en el body del post estén los campos: users_id"}), 400
    people = Character.query.get(people_id)
    print(people)
    if not people:
        return jsonify({"error": "No se ha encontrado people_id"}), 400
    users_id = data_request["users_id"]
    users = User.query.get(users_id)
    print(users)
    if not users:
        return jsonify({"error": "No se ha encontrado users_id"}), 400

    new_favorite = Favorite(
        users_id=users_id,
        planets_id=None,
        characters_id=people_id
    )

    try:
        db.session.add(new_favorite)
        db.session.commit()
        return jsonify({"message": "Favorite añadido"})
    except Exception as e:
        db.session.rollback()
        print("Error", e)
        return jsonify({"error": "No se ha agregado el favorite"})


# [DELETE] /favorite/people/<int:people_id>

@favorite_bp.route('/people/<int:character_id>', methods=['DELETE'])
def delete_fav_peoplet(character_id):
    favorite = Favorite.query.filter_by(characters_id=character_id).first()

    if favorite is None:
        return jsonify({"error": "Favorite planet not found"}), 404

    db.session.delete(favorite)
    db.session.commit()

    return jsonify({"msg": f"Favorite planet {character_id} deleted"}), 200
