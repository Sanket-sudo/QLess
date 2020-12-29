from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/recommend', methods=['POST'])
def recommend():
	data = request.get_json()
	return data['item']