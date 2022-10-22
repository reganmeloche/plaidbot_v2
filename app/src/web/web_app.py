from flask import Flask, request, jsonify
import requests
from app.options.model_options import ModelOptions
from app.src.web.web_dependencies import WebDependencies

app = Flask(__name__)

with app.app_context():
    deps = WebDependencies(ModelOptions())
    
    @app.route('/test')
    def basic():
        return 'Hello, World!'

    @app.route('/predict', methods=['POST'])
    def predict():
        request_text = request.form.get('text', None)
        result = deps.prediction_handler.handle(request_text)
        return jsonify(result)
  