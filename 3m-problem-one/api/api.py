import os
from flask import Flask

from models.auth import db, guard, cors, User
from auth.routes import auth
from view.routes import view

from functools import wraps
from flask import request, jsonify
import jwt



app = Flask(__name__)
app.debug = True
app.register_blueprint(auth)
app.register_blueprint(view)

app.config['SECRET_KEY'] = 'change-this-at-some-point'
app.config["JWT_ACCESS_LIFESPAN"] = {"hours": 24}
app.config["JWT_REFRESH_LIFESPAN"] = {"days": 30}

guard.init_app(app, User)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.getcwd(), 'accounts.db')}"
db.init_app(app)

cors.init_app(app)