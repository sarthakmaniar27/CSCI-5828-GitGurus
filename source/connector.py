from abc import ABC, abstractmethod
from pymongo import MongoClient

class User():
    def __init__(self):
        self.username = 'user2'
        self.password = 'password'

class DBConnector():
    def __init__(self):
        self.User = User()

class MongoConnector(DBConnector):
    def __init__(self):
        super().__init__()
        self.IP_ADDRESS = 'mongodb://localhost:27017/'
        self.DATABASE_NAME = 'Crime'
        self.CONNECTION_STRING = self.IP_ADDRESS+self.DATABASE_NAME

    # @app.on_event("startup")
    def startup_db_client(self):
        mongodb_client = MongoClient(self.CONNECTION_STRING)
        print("Connected to the MongoDB database!")
        return mongodb_client

    # @app.on_event("shutdown")
    def shutdown_db_client(self):
        pass



# print('hi')
# mongo1 = MongoConnector()
# mongo1.startup_db_client()
# mongo1.shutdown_db_client()
