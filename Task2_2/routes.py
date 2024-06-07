from flask import request, jsonify
from app import app, mysql
from models import Member, WorkoutSession


@app.route('/trainers/distinct', methods=['GET'])
def list_distinct_trainers():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT DISTINCT trainer_id FROM Members")
    trainers = cursor.fetchall()
    cursor.close()
    trainer_ids = [trainer['trainer_id'] for trainer in trainers]
    return jsonify(trainer_ids), 200

@app.route('/trainers/count_members', methods=['GET'])
def count_members_per_trainer():
    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT trainer_id, COUNT(*) as member_count
        FROM Members
        GROUP BY trainer_id
    """)
    trainer_counts = cursor.fetchall()
    cursor.close()
    return jsonify(trainer_counts), 200

@app.route('/members/age_range', methods=['GET'])
def get_members_in_age_range():
    start_age = request.args.get('start_age', default=25, type=int)
    end_age = request.args.get('end_age', default=30, type=int)
    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT id, name, age, trainer_id
        FROM Members
        WHERE age BETWEEN %s AND %s
    """, (start_age, end_age))
    members = cursor.fetchall()
    cursor.close()
    return jsonify(members), 200
