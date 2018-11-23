from model.user import User
from model.schedule import Schedule
import pickle

class Data:
    __slots__ = ['db']

    def __init__(self, db_file='db.data'):
        try:
            self.read_data(db_file)
        except:
            self.db = {
                "users": {

                }
            }

    def add_user(self, user_id, name):
        self.db['users'][user_id] = User(name, Schedule(dict(), dict()))
    
    def read_data(self, db_file='db.data'):
        self.db = pickle.load(open(db_file, 'rb'))

    def write_data(self, db_file='db.data'):
        fw = open(db_file, 'wb')
        pickle.dump(self.db, fw)
        fw.close()
