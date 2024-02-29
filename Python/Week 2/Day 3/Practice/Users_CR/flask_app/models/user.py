# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app

DATABASE = "users"

# === C R U D ===

# model the class after the friend table from our database
class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        
    #* =========== READ ALL ===========
        
    @classmethod
    def get_all(cls):

        query = "SELECT * FROM users;"

        results = connectToMySQL(DATABASE).query_db(query)

        users_instances = []
        if results:
            for row in results:
               one_user = User(row)
               users_instances.append(one_user)

            return users_instances
        
        return []
        
    #* =========== CREATE ===========

    @classmethod
    def save(cls, data):

        query = """
                INSERT INTO users (first_name, last_name, email) 
                VALUES (%(first_name)s, %(last_name)s, %(email)s);
                """
        result = connectToMySQL(DATABASE).query_db(query, data)
        
        return result
