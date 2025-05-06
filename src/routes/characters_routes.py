from flask import Blueprint, jsonify, request
from models import Character, db

characters_bp = Blueprint('characters', __name__, url_prefix='/characters')