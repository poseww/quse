from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, 
TextAreaField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

from application.utlis import exists_email, not_exists_email, exists_username

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=8), exists_username])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=1)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField("Log In")


class SignUpForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Length(max=128), exists_email])
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=8), exists_username])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", message="Password does not match")])
    submit = SubmitField("Sign Up")


class EditProfile(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=128), exists_username])
    email = EmailField("email", validators=DataRequired(), Email(), exists_email)
    bio = TextAreaField('Bio', validators=[Length(max=256)])
    profile_pic = FileField('Profile Picture', validators=[FileAllowed(['jpg', 'png','jpeg'])])
    submit = SubmitField('update profile')

class ResetPassword(FlaskForm):
    old_password = PasswordField("old password", validators=[DataRequired(), Length(min=8)])
    new_password = PasswordField("new password", validators=[DataRequired(), Length(min=8)])
    confirm_new_password = PasswordField("confirm new password", validators=[DataRequired(), Length=(min=8), EqualTo("new_password")])
    submit = SubmitField("reset password")

class ForgotPassword(FlaskForm):
    email = StringField("email", validators=DataRequired(), Email(), not_exists_email)
    recaptcha = RecaptchaField()
    submit = SubmitField("send link verification to email")

class VerificationResetPassword(FlaskForm):
    password = PasswordField(" new Password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("confirm new password", validators=[DataRequired(),Length(min=8), EqualTo("password")])
    submit = SubmitField("reset password")
    
class CreatePost(FlaskForm):
    caption = TextAreaField('Caption')
    post_pic = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png', jpeg])])
    submit = SubmitField('Post')


class EditPost(FlaskForm):
    caption = StringField("caption")
    submit = SubmitField('update post')



