import dash
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import dash_bootstrap_components as dbc


def create_app():
    server = Flask(__name__)
    server.config.from_pyfile('config.py')

    register_dashapps(server)
    register_extensions(server)
    register_blueprints(server)

    return server


def register_dashapps(app):
    from app.dashapp.layout import layout
    from app.dashapp.callbacks import register_callbacks

    # Meta tags for viewport responsiveness
    meta_viewport = {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

    dashapp = dash.Dash(__name__,
                        server=app,
                        url_base_pathname='/stats/',
                        meta_tags=[meta_viewport])

    with app.app_context():
        dashapp.title = 'Dashapp'
        dashapp.layout = layout
        register_callbacks(dashapp)


def register_extensions(server):
    pass
    # from app.extensions import db
    # from app.extensions import migrate
    #
    # db.init_app(server)
    # migrate.init_app(server, db)


def register_blueprints(server):
    from app.views import server_bp

    server.register_blueprint(server_bp)
