from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app import DATABASE
from flask import flash



# === C R U D ===

# model the class after the friend table from our database
class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        
    #* =========== READ ===========
       
    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        data = {'id': id}
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])  
        else:
            return None
        
    #* =========== CREATE ===========

    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO dojos (name, location, language, comment) 
                VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);
                """
        result = connectToMySQL(DATABASE).query_db(query, data)
        
        return result
    
    #* =========== VALIDATION ==========

    @staticmethod
    def is_valid(survey):
        is_valid = True
        if len(survey['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters.")
        if len(survey['location']) < 1:
            is_valid = False
            flash("Must choose a dojo location.")
        if len(survey['language']) < 1:
            is_valid = False
            flash("Must choose a favorite language.")
        if len(survey['comment']) < 3:
            is_valid = False
            flash("Comments must be at least 3 characters.")
        return is_valid