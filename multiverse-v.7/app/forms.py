from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User 

class RegistrationForm(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired(), Length(min=2, max=20)])

    surname = StringField('Surname', validators=[DataRequired(), Length(min=2, max=20)])

    enterdate = DateField('Enterdate', format='%d/%m/%Y')

    company = StringField('Company', validators=[DataRequired(), Length(min=2, max=20)])

    companytype = StringField('Companytype', validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    confirmpassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    county = StringField('County', validators=[DataRequired(), Length(min=2, max=20)])

    city = StringField('City', validators=[DataRequired(), Length(min=2, max=20)])

    phonenumber = StringField('Phonenumber', validators=[DataRequired(), Length(min=2, max=20)])

    submit = SubmitField('Register')

    def validate_firstname(self,firstname):

        user = User.query.filter_by(firstname=firstname.data).first()
        if user:
            raise ValidationError('This name is taken!')

    def validate_email(self,email):

        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is taken!')


class LoginForm(FlaskForm):
    email = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')