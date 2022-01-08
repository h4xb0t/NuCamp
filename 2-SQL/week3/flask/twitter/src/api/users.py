#!/usr/bin/env python
'''docstring'''

from flask import Blueprint, jsonify, abort, request
from ..models import User, Tweet, db
import hashlib
import secrets

bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    users = User.query.all()  # ORM performs SELECT query
    result = []
    for u in users:
        result.append(u.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    u = User.query.get_or_404(id)
    return jsonify(u.serialize())


@bp.route('', methods=['POST'])
def create():
    # req body must contain user_id and content
    # if 'username' not in request.json or 'password' not in request.json:
    #     return abort(400)
    # user with id of user_id must exist
    # User.query.get_or_404(request.json['id'])
    # construct User
    u = User(
        username=request.json['username'],
        password=scramble(request.json['password'])
    )
    if len(request.json['username']) < 3:
        or len(request.json['password']) < 8:
        return abort(400)

    db.session.add(u)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(u.serialize())


def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = User.query.get_or_404(id)
    try:
        db.session.delete(u)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)


@bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update(id: int):
    u = User.query.get_or_404(id)

    if len(request.json['username']) < 3:
        or len(request.json['password']) < 8:
        return abort(400)

    if request.json['username'] and request.json['password']:
        u.username = request.json['username'],
        u.password = request.json['password']
    elif request.json['username']:
        u.username = request.json['username']
    elif request.json['password']:
        u.password = request.json['password']

    # db.session.add(u)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(u.serialize())


@bp.route('/<int:id>/<liking_users>', methods=['GET'])
def liking_users(id: int):
    t = Tweet.query.get_or_404(id)
