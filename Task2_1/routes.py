from flask import request, jsonify
from app import app
from models import Member
from models import WorkoutSession

@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()
    Member.add(data)
    return jsonify({'message': 'Member added successfully'}), 201

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    member = Member.get_by_id(id)
    if member:
        return jsonify(member), 200
    return jsonify({'message': 'Member not found'}), 404

@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    data = request.get_json()
    Member.update(id, data)
    return jsonify({'message': 'Member updated successfully'}), 200

@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    Member.delete(id)
    return jsonify({'message': 'Member deleted successfully'}), 200

@app.route('/members', methods=['GET'])
def get_all_members():
    members = Member.get_all()
    return jsonify(members), 200

@app.route('/workouts', methods=['POST'])
def add_workout():
    data = request.get_json()
    WorkoutSession.add(data)
    return jsonify({'message': 'Workout session added successfully'}), 201

@app.route('/workouts/<int:id>', methods=['PUT'])
def update_workout(id):
    data = request.get_json()
    WorkoutSession.update(id, data)
    return jsonify({'message': 'Workout session updated successfully'}), 200

@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    WorkoutSession.delete(id)
    return jsonify({'message': 'Workout session deleted successfully'}), 200

@app.route('/workouts/member/<int:member_id>', methods=['GET'])
def get_workouts_by_member(member_id):
    sessions = WorkoutSession.get_all_by_member(member_id)
    return jsonify(sessions), 200
