import sqlite3 as sql


class Database:

    def __init__(self, db_name, ext):
        if db_name != None:
            self.db_name = db_name
            self.conn = sql.connect(db_name+ext)
            self.c = self.conn.cursor()


db = Database(None)
