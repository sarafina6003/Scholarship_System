from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, DateField
from wtforms.validators import Email, DataRequired, Length, NumberRange
from wtforms_components import DateRange
from datetime import date

class MyForm(FlaskForm):
    names = StringField("Names", validators=[DataRequired(message="Enter Names please!"), Length(min=4)])
    email = StringField("Email", validators=[DataRequired(message="Enter your email address please!"), Email(message="Invalid Email!")])
    age  = IntegerField("Age", validators=[DataRequired(message="Enter Age"), NumberRange(min=1, max=100, message="Age must be between 1 and 100")])
    password = PasswordField("Password", validators=[DataRequired(message="Enter Password"), Length(min=6)])

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(message="Enter your email address please!"),Email(message="Invalid Email!")])
    password = PasswordField("Password", validators=[DataRequired(message="Enter Password")])


class AddForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(message="Enter Names please!")])
    sat = StringField("SAT Exam", validators=[DataRequired(message="Enter SAT Name please!")])
    date = DateField("Expected Completion:yy-mm-dd", validators=[DateRange(min=date.today(),message="Enter a valid date please!")])
