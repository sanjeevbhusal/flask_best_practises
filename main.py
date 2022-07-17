from flask import Flask
from flask_app.blueprints import page
from flask_app.extensions import debug_toolbar


def create_app(settings_override=None):
    app = Flask(__name__)
    app.config.from_object("config.settings")
    app.config.from_pyfile("instance/settings.py")

    if settings_override:
        app.config.update(settings_override)

    app.register_blueprint(page)
    extensions(app)
    return app


def extensions(app):
    debug_toolbar.init_app(app)


if __name__ == '__main__':
    app = create_app()
    app.run()
