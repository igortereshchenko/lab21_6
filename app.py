import pandas as pd
import plotly
import plotly.graph_objs as go
import json
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from forms import *
from models import *

#DATABASE_URI = 'postgresql://postgres:MYUmyu2020@localhost:5432/postgres'
DATABASE_URI = 'postgres://vdhagdclthcdic:dc0f48d3be9c9b63694e1b16eb71cf674695df63f39e30ed4c90dad35364a113@ec2-54-228-243-238.eu-west-1.compute.amazonaws.com:5432/d58rtmm8nujh88'
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'ksjdfhdsjkflhdsjklvn'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
db = SQLAlchemy(app)
#db.drop_all()
#db.create_all()

@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('home.html')

@app.route('/users', methods=["GET"])
def users():
    users_all = db.session.query(Users).all()
    return render_template('users.html', usersAll=users_all)

@app.route('/users_create', methods=["GET", "POST"])
def users_create():
    form = UsersForm()
    if request.method == 'POST':
        if not form.validate():
            render_template('users_create.html', form=form, form_name='Create user')
        else:
            user_data = Users(
                user_id=db.session.query(db.func.max(Users.user_id)).scalar()+1,
                user_name=form.name.data,
                age=form.age.data,
                weight=form.weight.data,
                activity=form.activity.data
            )
            db.session.add(user_data)
            db.session.commit()
            return redirect(url_for('users'))
    return render_template('users_create.html', form=form, form_name='Create user')

@app.route('/users_update', methods=['GET','POST'])
def users_update():
    form = UsersForm()
    id = request.args.get('id')
    if request.method == 'GET':

        field = db.session.query(Users).filter(Users.user_id == id).one()

        form.name.data = field.user_name
        form.age.data = field.age
        form.weight.data = field.weight
        form.activity.data = field.activity

        return render_template('users_create.html', form=form, form_name='Update user')
    else:
        if not form.validate():
            return render_template('users_create.html', form=form, form_name='Update user')

        user = db.session.query(Users).filter(Users.user_id == id).one()
        user.user_name = form.name.data
        user.age = form.age.data
        user.weight = form.weight.data
        user.activity = form.activity.data

        db.session.commit()
        return redirect(url_for('users'))

@app.route('/delete_user')
def delete_user():
    id = request.args.get('id')
    try:
        db.session.delete(db.session.query(Users).filter(Users.user_id == id).one())
        db.session.commit()
        return redirect(url_for('users'))
    except:
        message = 'You cant delete this'
        return render_template('error.html', message=message)

@app.route('/complex', methods=["GET"])
def complex():
    complex_all = db.session.query(Complex).all()
    return render_template('complex.html', usersAll=complex_all)

@app.route('/complex_create', methods=["GET", "POST"])
def complex_create():
    form = ComplexForm()
    if request.method == 'POST':
        if not form.validate():
            render_template('complex_create.html', form=form, form_name='Create complex')
        else:
            try:
                complex_data = Complex(
                    complex_name = form.name.data
                )
                db.session.add(complex_data)
                db.session.commit()
                return redirect(url_for('complex'))
            except:
                message = 'You cant delete this'
                return render_template('error.html', message=message)

    return render_template('complex_create.html', form=form, form_name='Create complex')

@app.route('/complex_update', methods=['GET','POST'])
def complex_update():
    form = ComplexForm()
    name = request.args.get('name')
    if request.method == 'GET':

        field = db.session.query(Complex).filter(Complex.complex_name == name).one()

        form.name.data = field.complex_name

        return render_template('complex_create.html', form=form, form_name='Update complex')
    else:
        if not form.validate():
            return render_template('complex_create.html', form=form, form_name='Update complex')
        try:
            complexs = db.session.query(Complex).filter(Complex.complex_name == name).one()
            complexs.complex_name = form.name.data

            db.session.commit()
            return redirect(url_for('complex'))
        except:
            message = 'You cant delete this'
            return render_template('error.html', message=message)

@app.route('/delete_complex')
def delete_complex():
    name = request.args.get('name')
    try:
        db.session.delete(db.session.query(Complex).filter(Complex.complex_name == name).one())
        db.session.commit()
        return redirect(url_for('complex'))
    except:
        message = 'You cant delete this'
        return render_template('error.html', message=message)

@app.route('/udc', methods=["GET"])
def user_do_complex():
    data_all = db.session.query(User_do_complex).all()
    return render_template('udc.html', usersAll=data_all)

@app.route('/udc_create', methods=["GET", "POST"])
def udc_create():
    form = UserDoComplexForm()
    if request.method == 'POST':
        if not form.validate():
            render_template('udc_create.html', form=form, form_name='Create UDC')
        else:
            data = User_do_complex(
                user_id=form.user_id.data,
                complex_name=form.complex_name.data,
                time_start=form.time_start.data,
                status=form.status.data,
            )
            try:
                db.session.add(data)
                db.session.commit()
                return redirect(url_for('user_do_complex'))
            except:
                message = 'You cant delete this'
                return render_template('error.html', message=message)

    return render_template('udc_create.html', form=form, form_name='Create UDC')

@app.route('/udc_update', methods=['GET','POST'])
def udc_update():
    form = UserDoComplexForm()
    id = request.args.get('id')
    complex_name = request.args.get('cn')
    time_start = request.args.get('ts')
    if request.method == 'GET':

        field = db.session.query(User_do_complex).filter(User_do_complex.user_id == id).filter(User_do_complex.complex_name == complex_name).filter(User_do_complex.time_start == time_start).one()

        form.user_id.data = field.user_id
        form.complex_name.data = field.complex_name
        form.time_start.data = field.time_start
        form.status.data = field.status

        return render_template('udc_create.html', form=form, form_name='Update UDC')
    else:
        if not form.validate():
            return render_template('udc_create.html', form=form, form_name='Update UDC')

        data = db.session.query(User_do_complex).filter(User_do_complex.user_id == id).filter(User_do_complex.complex_name == complex_name).filter(User_do_complex.time_start == time_start).one()
        try:
            data.user_id = form.user_id.data
            data.complex_name = form.complex_name.data
            data.time_start = form.time_start.data
            data.status = form.status.data

            db.session.commit()
            return redirect(url_for('user_do_complex'))
        except:
            message = 'You cant delete this'
            return render_template('error.html', message=message)

@app.route('/delete_udc')
def delete_udc():
    id = request.args.get('id')
    complex_name = request.args.get('cn')
    time_start = request.args.get('ts')

    db.session.delete(db.session.query(User_do_complex).filter(User_do_complex.user_id == id).filter(User_do_complex.complex_name == complex_name).filter(User_do_complex.time_start == time_start).one())
    db.session.commit()
    return redirect(url_for('user_do_complex'))

@app.route('/dashboard')
def rejects():
    data = db.session.query(User_do_complex).all()
    datee = [obj.time_start for obj in data]
    status = [obj.status for obj in data]
    hour = [dat.hour for dat in datee]
    df = pd.DataFrame(columns=['hour','status'])
    df.hour = hour
    df.status = status
    df1 = df[df.status.isin(['done', 'rejected'])].groupby('hour').status.count().reset_index()
    df2 = df[df.status == 'rejected'].groupby('hour').status.count().reset_index()
    df_res = pd.merge(df1,df2,how='left',on='hour')
    df_res.columns = ['hour', 'alll', 'rej']
    df_res.rej.fillna(0,inplace=True)
    df_res['ratio'] = df_res.rej / df_res.alll

    bar = go.Bar(x=df_res.hour, y=df_res.ratio)
    #fig = go.Figure([go.Scatter(x=df_res.hour, y=df_res.ratio)])
    #scatter = go.Scatter(x=,y=,z=)
    print(df_res.hour, df_res.ratio)
    graphJSON = json.dumps([bar], cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('dashboard.html', graphJSON=graphJSON,ids=[0])

@app.route('/scatter')
def scatter():
    data = db.session.query(Users).all()
    datee = [obj.age for obj in data]
    weight = [obj.weight for obj in data]
    activity = [obj.activity for obj in data]
    age = [(date.today() - dat).days // 365 for dat in datee]

    scatter = go.Scatter(x=age, y=activity,mode='markers',marker_size=weight)

    #print(age)
    graphJSON = json.dumps([scatter], cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('dashboard.html', graphJSON=graphJSON,ids=[0])

if __name__ == '__main__':
    app.run(debug=True)