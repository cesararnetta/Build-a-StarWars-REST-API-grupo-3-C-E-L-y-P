from flask import jsonify, Blueprint
from models import Character

people_bp = Blueprint('people_custom', __name__, url_prefix='/people')
print(__name__)

# [GET] /people


@people_bp.route('/', methods=['GET'])
def get_all_people():
    raw_list_people = Character.query.all()
    list_people = [people.serialize() for people in raw_list_people]
    print(list_people)
    return jsonify({"people": list_people}), 200


@people_bp.route('/<int:people_id>', methods=['GET'])
def get_character_id(people_id):
    character = Character.query.get(people_id)
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
