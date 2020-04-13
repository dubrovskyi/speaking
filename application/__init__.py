from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask import Flask, render_template, session, redirect,url_for
from flask import request, make_response
from application.app import index

from models.InfoForm import InfoForm

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    csrf = CSRFProtect(app)
    app.config['SECRET_KEY'] = 'mysecretkey'

    # Application Configuration

    return app