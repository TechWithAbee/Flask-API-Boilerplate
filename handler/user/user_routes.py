from flask import Blueprint, jsonify, request
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)
from handler.user.user_service import get_me_service

user_bp = Blueprint("user", __name__)

@user_bp.route('/api/v0/me', methods=['GET'])
def get_me():
    user = get_me_service()
    return user
