from flask import Blueprint, jsonify, request

from models import db, User, Character

character_bp = Blueprint('character_custom', __name__,
                         url_prefix='/character/<int:id>')


@character_bp.route
@character_bp.route('/', methods=['GET'])
def get_character_id():

    character = Character.query.get(characters_id)
    if character is None:
        return ('Character not found', status_code == 404)
    character_data = {
        "id": character.characters_id,
        "name": character.name,
        "birth_year": character.birth_year,
        "gender": character.gender,
    }
    characters = [character.serialize]
    return jsonify(character_data), 200
