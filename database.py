import sqlalchemy as db

class Database():

    engine = db.create_engine('postgres+psycopg2://postgres:16071994@localhost:5432/Training')
    def __init__(self):
        self.connection = self.engine.connect()
        print("DB Instance created")

    def fetchByQyery(self, query):
        fetchQuery = self.connection.execute(f"SELECT * FROM {query}")

        for data in fetchQuery.fetchall():
            print(data)