import os
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy

DATABASE_URI = 'postgres+psycopg2://postgres:16071994@localhost:5432/Training'

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
db = SQLAlchemy(app)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.form:
        print(request.form)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
'''
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import sys
import json
from flask_heroku import Heroku
app = Flask( __name__ )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
heroku = Heroku(app)
db = SQLAlchemy(app)

class Dataentry(db.Model):
    __tablename__ = "dataentry"
    id = db.Column(db.Integer, primary_key=True)
    mydata = db.Column(db.Text())

    def __init__ (self, mydata):
        self.mydata = mydata

@app.route("/submit", methods=["POST"])
def post_to_db():
    indata = Dataentry(request.form['mydata'])
    data = copy(indata. __dict__ )
    del data["_sa_instance_state"]
    try:
        db.session.add(indata)
        db.session.commit()
    except Exception as e:
        print("\n FAILED entry: {}\n".format(json.dumps(data)))
        print(e)
        sys.stdout.flush()
    return 'Success! To enter more data, <a href="{}">click here!</a>'.format(url_for("enter_data"))

@app.route("/")
def enter_data():
    return render_template("dataentry.html")

if __name__ == ' __main__':
    app.debug = True
    app.run()
    '''