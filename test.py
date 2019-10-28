from sqlalchemy import create_engine
import sqlalchemy as db

DATABASE_URI = 'postgres+psycopg2://postgres:16071994@localhost:5432/Training'

engine = create_engine(DATABASE_URI)
connection = engine.connect()
metadata = db.MetaData()
exercise = db.Table('exercise', metadata, autoload=True, autoload_with=engine)

query = db.select([exercise])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet)

res = connection.execute(db.select([exercise]).where(exercise.columns.exercise_name == 'squats')).fetchall()
print(res)