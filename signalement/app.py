import datetime
import os

from flask import Flask, render_template, session, g, request
from flask_migrate import Migrate
from flask_login import current_user

from signalement.config import DefaultConfig

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
    create_migrate(app)
    configure_logging(app)
    configure_template_filters(app)
    configure_error_handlers(app)
    configure_cli(app)

    return app


def create_migrate(app):
    migrate = Migrate(app, db)
    return migrate


def configure_app(app, config=None):
    app.config.from_object(DefaultConfig)

    app.config.from_pyfile('production.cfg', silent=True)


def configure_extensions(app):
    # flask-sqlaclhemy
    db.init_app(app)

    # flask-login
    login_manager.login_view = 'admin.login'
    login_manager.refresh_view = 'admin.reauth'

    login_manager.setup_app(app)

    # flask-babel
    babel.init_app(app)

    @babel.localeselector
    def get_locale():
        return request.accept_languages.best_match(app.config["LANGUAGES"])


def configure_blueprints(app):

    # from signalement.user import user
    from signalement.frontend import frontend
    from signalement.admin import admin

    for bp in [frontend, admin]:
        app.register_blueprint(bp)


def configure_template_filters(app):
    pass


def configure_logging(app):

    if app.debug or app.testing:
        return


def configure_hook(app):

    @app.before_request
    def before_request():
        session.permanent = True
        app.permanent_session_lifetime = datetime.timedelta(minutes=20)
        session.modified = True
        g.user = current_user


def configure_error_handlers(app):

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html")


def configure_cli(app):

    # Initialisation de la base de donnée
    @app.cli.command()
    def initdb():
        db.drop_all()
        db.create_all()

    # Commande pour la traduction
    @app.cli.group()
    def translate():
        pass

    @translate.command()
    def update():
        """Mise à jour des traductions."""
        if os.system('pybabel extract -F signalement/babel.cfg -o signalement/messages.pot signalement/'):
            raise RuntimeError("Échec de l'extraction des traductions.")
        if os.system('pybabel update -i signalement/messages.pot -d signalement/translations'):
            raise RuntimeError("Échec de la mise à jour des traductions.")

    @translate.command()
    def compile():
        """Compilation des traductions."""
        if os.system('pybabel compile -f -d signalement/translations'):
            raise RuntimeError("Échec de la compilation des traductions.")
