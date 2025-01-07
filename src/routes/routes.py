from flask import Blueprint
from controllers.controller import hello_world

def init_routes(app):
    main = Blueprint('main', __name__)
    main.route('/')(hello_world)
    app.register_blueprint(main)