import sqlite3

class DBCo:
    conn = None
    def __init__(self):
        if DBCo.conn == None:
            DBCo.conn = sqlite3.connect("profiles.db")

def check_mail_epitech(email):
    suffix = ""
    try:
        suffix = email.split('@')[1]
    except IndexError:
        return 0
    if suffix == "epitech.eu":
        return 1
    return 0

class Student:
    cursor = DBCo().conn.cursor()

    def __init__(self, id=None, email=None):
        self.profile_id = id
        self.email = email
    
    def __str__(self):
        return "My email is '{}' and my id on discord is '{}'".format(self.email, self.profile_id)
    
    def __repr__(self):
        return str(self)

    def get_email(self):
        return self.email

    def get_db_by_id(self):
        if (self.profile_id is None):
            return False
        try:
            query = "SELECT email FROM profiles WHERE profile_id=?"
            self.cursor.execute(query, (self.profile_id, ))
            self.email = self.cursor.fetchone()[0]
            if self.email is None:
                return False
        except Exception as e:
            print(e)
            return False
        return True

    def push_in_db(self):
        if self.email is None or self.profile_id is None:
            return -1
        if (check_mail_epitech(self.email) == 0):
            return -2
        try:
            query = "INSERT INTO profiles(profile_id, email) VALUES (?, ?)"
            self.cursor.execute(query, (self.profile_id, self.email))
            DBCo().conn.commit()
        except sqlite3.IntegrityError:
            return -3
        return 1