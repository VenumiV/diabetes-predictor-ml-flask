from flask import Flask
from src.routes.ui import ui_bp

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.register_blueprint(ui_bp)
    return app