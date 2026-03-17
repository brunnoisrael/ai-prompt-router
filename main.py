from flask import Flask, request, jsonify
from api.routes import prompt_bp, prompt

def create_app():

    app = Flask(__name__)

    app.register_blueprint(prompt_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)