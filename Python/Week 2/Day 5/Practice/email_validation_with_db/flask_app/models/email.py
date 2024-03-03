from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app import DATABASE
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class Email:
    def __init__(self, data):
        self.id = data["id"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # ========== C R U D ==========

    # ========== create ===========
    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO email (email) 
                VALUES (%(email)s)
                """
        result = connectToMySQL(DATABASE).query_db(query, data)

        return result

    # ========== read =============
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM email"
        results = connectToMySQL(DATABASE).query_db(query)

        emails_instances = []

        if results:
            for row in results:
                one_email = Email(row)
                emails_instances.append(one_email)

            return emails_instances

        return []
    
    #*========== validation ==========
    @staticmethod
    def is_valid(email):
        is_valid = True
        query = "SELECT * FROM email WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, email)
        if len(results) >= 1:
            flash("Email already taken.")
            is_valid = False
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid Email!!!")
            is_valid = False
        return is_valid

