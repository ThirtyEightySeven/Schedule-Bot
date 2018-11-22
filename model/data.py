from model.user import User
import pickle

class Data:
    __slots__ = ['db']

    def __init__(self, db_file='db.data'):
        self.read_data(db_file)

    def add_user(self, user):
        self.db['users'][user.name] = user
        print(self.db)

    
    def read_data(self, db_file='db.data'):
        self.db = pickle.load(open(db_file, 'rb'))

    def write_data(self, db_file='db.data'):
        fw = open(db_file, 'wb')
        pickle.dump(self.db, fw)
        fw.close()
