from model.user import User

import json

class Data:
    __slots__ = ['db']

    def __init__(self, db_file='db.json'):
        with open('db.json', 'r') as read_file:
            self.db = json.load(read_file)

    def add_user(self, user):
        self.db['users'][user.name] = user
        print(self.db)

    def write_data(self, db_file='db.json'):
        with open("db.json", "w") as write_file:
            json.dump(self.db, write_file)
