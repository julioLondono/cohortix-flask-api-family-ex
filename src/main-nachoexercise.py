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

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def sitemap():
    return jsonify(doe.get_all_members())

@app.route('/new', methods=['POST'])
def newMember():
    addedMember = doe.add_member(request.get_json())
    return jsonify(addedMember)

@app.route('/member/<int:person_id>', methods=['PUT', 'GET', 'DELETE'])
def getMember(person_id):
    if request.method == 'GET':
        member = doe.get_member(person_id)
        if member is not None and member is not False:
            return jsonify(member)
        return jsonify({"error": "Invalid Id"}), 404

    if request.method == 'PUT':
        updatedMember = doe.update_member(person_id, request.get_json())
        if updatedMember == 400:
            return jsonify({"error": "Missing information"}), 400
        if updatedMember == 404:
            return jsonify({"error": "Invalid Id"}), 404

        return jsonify(updatedMember)

    if request.method == 'DELETE':
        return jsonify(doe.delete_member(person_id))

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT)
