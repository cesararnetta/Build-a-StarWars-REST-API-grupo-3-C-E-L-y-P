from flask import Blueprint, jsonify

from models import db, Favorite

# [GET] /users/favorites Get all the favorites that belong to the current user.

user_bp = Blueprint(
    'user_custom', __name__, url_prefix='/users')


@user_bp.route('/favorites/<int:user_id>', methods=['GET'])
def get_all_favorites(user_id):
    print(user_id)
    raw_list_favorite = Favorite.query.filter_by(users_id=user_id).all()
    print(raw_list_favorite)
    list_favorite = [favorite.serialize_with_relations()
                     for favorite in raw_list_favorite]
    return jsonify({"user_favorites": list_favorite})
