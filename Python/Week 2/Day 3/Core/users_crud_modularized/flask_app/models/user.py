# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app import DATABASE


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
    
    @classmethod
    def get_by_id(cls, user_id):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        data = {'user_id': user_id}
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])  # Assuming the query returns only one user
        else:
            return None
        
    #* =========== CREATE ===========

    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO users (first_name, last_name, email) 
                VALUES (%(first_name)s, %(last_name)s, %(email)s);
                """
        result = connectToMySQL(DATABASE).query_db(query, data)
        
        return result
    
    #* =========== UPDATE ===========

    @classmethod
    def update(cls, user_id, first_name, last_name, email):
        query = """
                UPDATE users
                SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
                WHERE id = %(id)s;
                """
        data = {
            'id': user_id,
            'first_name': first_name,
            'last_name': last_name,
            'email': email
        }
        connectToMySQL(DATABASE).query_db(query, data)
    
    
    #* =========== DELETE ===========

    @classmethod
    def delete(cls, id):
        query = "DELETE FROM users WHERE id = %(id)s;"
        connectToMySQL(DATABASE).query_db(query, {'id': id})
