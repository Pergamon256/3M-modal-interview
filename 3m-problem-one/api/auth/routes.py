from datetime import date
import math

import flask
import flask_praetorian

from models.auth import db, guard, User
from flask import Blueprint, request
import constants.errors as errors

auth = Blueprint('auth', __name__)

@auth.route('/api/auth/register', methods=['POST'])
def register():
    """
    Registers a user by parsing a POST request containing user credentials and
    writing these values to the accounts db. Sensitive data is hashed.
    .. example::
       $ curl http://127.0.0.1:5000/api/auth/register -X POST -d '{"username":"user","password":"pswrd", "age": 21}'
    """
    req = flask.request.get_json(force=True)
    username = req.get('username', None)
    password = req.get('password', None)
    age = int(req.get('age', None))

    lowerAge = (age // 10) * 10
    upperAge = lowerAge + 9
    ageGroup = "{0}-{1}".format(lowerAge, upperAge)

    db.create_all()
    if db.session.query(User).filter_by(username=username).count() < 1:
        db.session.add(User(
          username=username,
          hashed_password=guard.hash_password(password),
          age=age,
          ageGroup=ageGroup,
            ))
        db.session.commit()
        return {'message': 'new user created.'}, 200
    else:
        return {'error': 'user already exists.'}, 409

@auth.route('/api/auth/login', methods=['POST'])
def login():
    """
    Logs a user in by parsing a POST request containing user credentials and
    issuing a JWT token.
    .. example::
       $ curl http://localhost:5000/api/auth/login -X POST -d '{"username":"user","password":"pswrd"}'
    """
    req = flask.request.get_json(force=True)
    username = req.get('username', None)
    password = req.get('password', None)

    # if user is not registered yet
    if db.session.query(User).filter_by(username=username).count() < 1:
      return errors.USER_NOT_FOUND

    user = guard.authenticate(username, password) # will throw 401 if user unauthorized
    return {'access_token': guard.encode_jwt_token(user)}, 200

@auth.route('/api/auth/refresh', methods=['POST'])
def refresh():
    """
    Refreshes an existing JWT by creating a new one that is a copy of the old
    except that it has a refrehsed access expiration.
    .. example::
       $ curl http://localhost:5000/api/refresh -X GET \
         -H "Authorization: Bearer <your_token>"
    """

    old_token = request.get_data()
    new_token = guard.refresh_jwt_token(old_token)
    ret = {'access_token': new_token}
    return ret, 200