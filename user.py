# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    DB = 'users_schema'
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
# Now we use class methods to query our database

    # CREATE
    @classmethod
    def save(cls, data):
        query = """ INSERT INTO users (first_name, last_name, email)
                    VALUES (%(first_name)s,%(last_name)s,%(email)s);"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    # READ

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.DB).query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users
    @classmethod
    def get_one(cls, id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, {'id':id})
        user = cls(results[0])
        return user
    
    # UPDATE
    @classmethod
    def update_user(cls,data,id):
        query = """UPDATE users 
        SET first_name = %(first_name)s, 
        last_name = %(last_name)s,
        email = %(email)s
        WHERE id = %(id)s;"""
        data = {
            'first_name':data['first_name'],
            'last_name':data['last_name'],
            'email':data['email'],
            'id':id #takes in passed-through id from function, adds it to form dictionary
            }
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
    
    #DELETE
    @classmethod
    def delete_user(cls,id):
        query = "DELETE FROM users WHERE id = %(id)s;"
        data = {'id':id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
