from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, DateField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, Length, Email, NumberRange
from datetime import date, datetime

class UsersForm(FlaskForm):
    """Users CRUD"""
    name = StringField('Name', [
        DataRequired("Enter name"), Length(2,20,"Name should be from 2 to 20 chars")])
    age = DateField('Age', default=date.today())
    weight = IntegerField("Weight", [
        DataRequired('Enter weight - should be from 10 to 900'), NumberRange(min=10, max=900)])
    activity = IntegerField("Activity per day in hours",[
        DataRequired('Enter how many hours you are active per day'), NumberRange(min=0, max=24)])

    submit = SubmitField('Submit')

class ComplexForm(FlaskForm):
    """Complex CRUD"""
    name = StringField('Complex name', [
        DataRequired("Enter name complex"), Length(2,20,"Name should be from 2 to 20 chars")])

    submit = SubmitField('Submit')

class UserDoComplexForm(FlaskForm):
    user_id = IntegerField("UserId",[
                           DataRequired("Enter User Id that exist")])
    complex_name = StringField('Complex name', [
        DataRequired("Enter name complex"), Length(2,20,"Name should be from 2 to 20 chars")])
    time_start = DateTimeField('Time start', default=datetime.today())
    status = StringField('status activity', [
        DataRequired("Enter status activity"), Length(2,10,"Status should be from 2 to 10 chars")])

    submit = SubmitField('Submit')

class ClubForm(FlaskForm):
    club_name = StringField("ClabName", [
        DataRequired("Enter name Club that exist")])
    prise = IntegerField("Prise",[
                           DataRequired("Enter User Id that exist"), NumberRange(min=0, max=999)])
    city = StringField("City", [
        DataRequired("Enter name Club that exist") ])
    rating = IntegerField("rating",[
                           DataRequired("Enter User Id that exist"), NumberRange(min=1, max=10)])

