# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app import DATABASE


# === C R U D ===

# model the class after the friend table from our database
class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        
    #* =========== READ ALL ===========
        
    @classmethod
    def get_all(cls):

        query = "SELECT * FROM dojos;"

        results = connectToMySQL(DATABASE).query_db(query)

        dojos_instances = []
        if results:
            for row in results:
               one_dojo = Dojo(row)
               dojos_instances.append(one_dojo)
        
        return dojos_instances
        
    #* =========== CREATE ===========

    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO dojos (name) 
                VALUES (%(name)s);
                """
        result = connectToMySQL(DATABASE).query_db(query, data)
        
        return result
    
    #* =========== GET BY ID ===========
    @classmethod
    def get_by_id(cls, dojo_id):
        query = "SELECT * FROM dojos WHERE id = %(dojo_id)s;"
        data = {'dojo_id': dojo_id}
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])  # Assuming the query returns only one dojo
        else:
            return None


