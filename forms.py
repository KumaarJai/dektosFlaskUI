'''
Created on Feb 8, 2019

@author: Ajay_Rabidas
'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange

 
class RegistrationForm(FlaskForm):
    macId =''
    STACK_NAME = StringField('Stack Name',validators=[DataRequired(), Length(min=2, max=20)])
    BASE_PATH = StringField('Base Path on file system', validators=[DataRequired(), Email()])
    PORT= StringField('PORT',validators=[DataRequired(), Length(min=4, max=20)])
    BAUD_RATE= IntegerField('Baud Rate', validators=[DataRequired(), NumberRange()])
    BIT_RATE= IntegerField('Bit Rate', validators=[DataRequired(), NumberRange()])
    TIMEOUT= IntegerField('Timeout', validators=[DataRequired(), NumberRange()])
    DATA_BYTES_START_INDEX = IntegerField('Data Bytes Start Index', validators=[DataRequired(), NumberRange()])
    
    #CLIENT Details ----------------------------------------------:
    CLIENT_NAME= StringField('Client Name',validators=[DataRequired(), Length(min=4, max=20)])
    CLIENT_ID= StringField('Client ID',validators=[DataRequired(), Length(min=4, max=20)])
    DATA_UPLOAD_INTERVAL = IntegerField('Data Bytes Start Index', validators=[DataRequired(), NumberRange()])
    
    #DATABASE DETAILS
    DB_HOST_URL = StringField('DB URL',validators=[DataRequired(), Length(min=4, max=20)])
    DB_USER = StringField('DB User',validators=[DataRequired(), Length(min=4, max=20)])
    DB_PASSWORD = StringField('DB Password',validators=[DataRequired(), Length(min=4, max=20)])
    
    submit = SubmitField('Upload Configuration')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')