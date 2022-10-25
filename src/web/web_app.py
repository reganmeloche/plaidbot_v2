from flask import Flask, request, jsonify
import requests
from src.web.secret_decorator import secret_required
from options.model_options import ModelOptions
from src.web.web_dependencies import WebDependencies

app = Flask(__name__)

with app.app_context():
    deps = WebDependencies(ModelOptions())

    @app.route('/')
    def basic():
        return 'Hello, World!'

    @app.route('/predict', methods=['POST'])
    @secret_required
    def predict():
        try:
            request_text = request.form.get('text', None)
            result = deps.prediction_handler.handle(request_text)   
        except:
            result = 'I have no idea'

        return get_response(result)

    
    def get_response(result_text: str):
        return jsonify({
            'response_type': 'in_channel',
            'text': result_text 
        })
  