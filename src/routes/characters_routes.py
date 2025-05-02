from flask import Blueprint, jsonify, request

characters_bp = Blueprint('characters', __name__, url_prefix='/characters')