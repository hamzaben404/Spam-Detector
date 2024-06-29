from flask import Blueprint, request, jsonify
from .model.predict import predict_email

api = Blueprint('api', __name__)

@api.route('/predict', methods=['POST'])
def predict():
    data = request.json
    email = data['email']
    result = predict_email(email)
    return jsonify({'prediction': result})
