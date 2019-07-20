"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from utils import APIException, generate_sitemap
from models import Family

app = Flask(__name__)
app.url_map.strict_slashes = False

doe = Family("Londono")

john = {"age": "33 Years old", "gender": "Male", "Lucky Numbers": [7, 13, 22], "member_id": 1}
jane = {"age": "35 Years old", "gender": "Female", "Lucky Numbers": [10, 14, 3], "member_id": 2}
jimmy = {"age": "5 Years old", "gender": "Male", "Lucky Numbers": [1], "member_id": 3}
family = {"members": [john, jane, jimmy]}

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members')
def members():
    all = family["members"]
    return jsonify(all)

@app.route('/members/<int:person_id>')
def memberId(person_id):
    for x in family["members"]:
        if x["member_id"] == person_id:
            return jsonify(x)

@app.route('/members/sum')
def luckysum():
    sum = 0
    for x in family["members"]:
        for y in x["Lucky Numbers"]:
            sum = sum + y
            return jsonify(sum)

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT)
