from app import mysql

class Member:
    def __init__(self, id, name, age, membership_type):
        self.id = id
        self.name = name
        self.age = age
        self.membership_type = membership_type

    @staticmethod
    def get_all():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM Members")
        members = cursor.fetchall()
        cursor.close()
        return members

    @staticmethod
    def get_by_id(member_id):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM Members WHERE id = %s", (member_id,))
        member = cursor.fetchone()
        cursor.close()
        return member

    @staticmethod
    def add(member):
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO Members(name, age, membership_type) VALUES (%s, %s, %s)",
                       (member['name'], member['age'], member['membership_type']))
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def update(member_id, member):
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE Members SET name = %s, age = %s, membership_type = %s WHERE id = %s",
                       (member['name'], member['age'], member['membership_type'], member_id))
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete(member_id):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM Members WHERE id = %s", (member_id,))
        mysql.connection.commit()
        cursor.close()

class WorkoutSession:
    def __init__(self, id, member_id, session_date, activity, duration):
        self.id = id
        self.member_id = member_id
        self.session_date = session_date
        self.activity = activity
        self.duration = duration

    @staticmethod
    def get_all_by_member(member_id):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM WorkoutSessions WHERE member_id = %s", (member_id,))
        sessions = cursor.fetchall()
        cursor.close()
        return sessions

    @staticmethod
    def add(session):
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO WorkoutSessions(member_id, session_date, activity, duration) VALUES (%s, %s, %s, %s)",
                       (session['member_id'], session['session_date'], session['activity'], session['duration']))
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def update(session_id, session):
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE WorkoutSessions SET member_id = %s, session_date = %s, activity = %s, duration = %s WHERE id = %s",
                       (session['member_id'], session['session_date'], session['activity'], session['duration'], session_id))
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete(session_id):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM WorkoutSessions WHERE id = %s", (session_id,))
        mysql.connection.commit()
        cursor.close()
