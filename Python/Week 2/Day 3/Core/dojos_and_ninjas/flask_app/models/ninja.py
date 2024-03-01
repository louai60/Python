# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app import DATABASE


# === C R U D ===

# model the class after the friend table from our database
class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        
    #* =========== READ ALL ===========
        
    @classmethod
    def get_all(cls):

        query = "SELECT * FROM ninjas;"

        results = connectToMySQL(DATABASE).query_db(query)

        ninjas_instances = []
        if results:
            for row in results:
               one_ninja = Ninja(row)
               ninjas_instances.append(one_ninja)

            return ninjas_instances
        
        return []
    
    @classmethod
    def get_by_id(cls, ninja_id):
        query = "SELECT * FROM ninjas WHERE id = %(ninja_id)s;"
        data = {'ninja_id': ninja_id}
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])  
        else:
            return None
        
    #* =========== CREATE ===========

    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO ninjas(first_name, last_name, age, dojo_id)
                VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);
                """
        result = connectToMySQL(DATABASE).query_db(query, data)
        
        return result