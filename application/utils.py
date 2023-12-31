from wtforms.validators import ValidationError

from application mport login_manager
from application.models import user

#FORM UTILS
def exists_email(form, email):
    user = User.query.filter_by(email = email.data).first()
    if user():
        raise ValidationError("Email already exists. Please use a different email.")

def not_exists_email(form, email):
    user = User.query.filter_by(email = email.data).first()
    if not user:
        raise ValidationError("Email not found.")

def exists_username(form, email):
    user = User.query.filter_by(username = username.data).first()
    if user:
        raise ValidationError("Username already exists. Please use a different username.")
#END OF FORM UTILS


#LOGIN MANAGER UTLIS
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_Id))
#END