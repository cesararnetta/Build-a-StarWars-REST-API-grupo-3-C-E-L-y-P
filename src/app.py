"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Character, Planet, User, Favorite
from routes import favorite_bp, people_bp, planets_bp, user_bp
# from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False

app.register_blueprint(favorite_bp)
app.register_blueprint(people_bp)
app.register_blueprint(planets_bp)
app.register_blueprint(user_bp)

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace(
        "postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)


# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/user', methods=['GET'])
def handle_hello():

#  codigo de Eduardo para obtener los favorites by user from its ID
# @app.route('/users/favorites/<int:user_id>', methods=['GET'])
# def get_all_favorites(user_id):
#     raw_list_favorite = Favorite.query.filter_by(users_id=user_id).first()
#     list_favorite = [favorite.serialize_with_relations()
#                      for favorite in raw_list_favorite]
#     return jsonify(list_favorite)

# this only runs if `$ python src/app.py` is executed


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
