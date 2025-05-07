from flask import Blueprint, jsonify, request

from models import db, User

user_bp = Blueprint(
    'user_custom', __name__, url_prefix='/user/favorites/<int:id>')


@user_bp.route
@user_bp.route('/', methods=['GET'])
def get_all_favorites(user_id):
    raw_list_favorite = Favorite.query.filter_by(users_id=user_id).first()
    list_favorite = [favorite.serialize_with_relations()
                     for favorite in raw_list_favorite]
    return jsonify(list_favorite)
