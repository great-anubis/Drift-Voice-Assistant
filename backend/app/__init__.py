from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import process_text
    app.add_url_rule('/process', 'process_text', process_text, methods=['POST'])

    return app