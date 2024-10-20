from flask import Flask, request, jsonify
import db_utils

app = Flask(__name__)


# This the code id use to 'Get' all fan club members (GET)
@app.route('/fanclub', methods=['GET'])
def get_members():
    members = db_utils.fetch_all_members()
    return jsonify(members)


# This is for me to Add a new member to the fan club (POST) as well their favourite movie
@app.route('/fanclub/add', methods=['POST'])
def add_member():
    data = request.get_json()
    name = data.get('name')
    favorite_movie = data.get('favorite_movie')

    if not name or not favorite_movie:
        return jsonify({'error': 'Name and favorite movie are required!'}), 400

    db_utils.add_member(name, favorite_movie)
    return jsonify({'message': 'Member added successfully!'})


# This is what i could use to  remove a member from the fan club (DELETE)
@app.route('/fanclub/remove', methods=['DELETE'])
def remove_member():
    data = request.get_json()
    member_id = data.get('id')

    if not member_id:
        return jsonify({'error': 'Member ID is required!'}), 400

    db_utils.remove_member(member_id)
    return jsonify({'message': 'Member removed successfully!'})


if __name__ == '__main__':
    app.run(debug=True)

