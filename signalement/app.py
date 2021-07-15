from flask import Flask, render_template

from signalement.config import DefaultConfig
from signalement.user import User

from signalement.extensions import db, login_manager, babel

__all__ = ['create_app']

def create_app(config=None, app_name=None):

    if app_name is None:
        app_name = DefaultConfig.PROJECT

    app = Flask(app_name, instance_relative_config=True)
    configure_app(app, config)
    configure_hook(app)
    configure_blueprints(app)
    configure_extensions(app)
    configure_logging(app)
    configure_template_filters(app)
    configure_error_handlers(app)
    configure_cli(app)

    return app

def configure_app(app, config=None):
    app.config.from_object(DefaultConfig)

def configure_extensions(app):
    # flask-sqlaclhemy
    db.init_app(app)

    # flask-login
    login_manager.login_view = 'frontend.login'
    login_manager.refresh_view = 'frontend.reauth'

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)
    login_manager.setup_app(app)

    # flask-babel
    babel.init_app(app)

    @babel.localeselector
    def get_locale():
        return

def configure_blueprints(app):

    from signalement.user import user
    from signalement.frontend import frontend

    for bp in  [user, frontend]:
        app.register_blueprint(bp)

def configure_template_filters(app):
    pass

def configure_logging(app):

    if app.debug or app.testing:
        return

def configure_hook(app):

    @app.before_request
    def before_request():
        pass

def configure_error_handlers(app):

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html")

def configure_cli(app):

    @app.cli.command()
    def initdb():
        db.drop_all()
        db.create_all()
