from flask import Flask
from flask_mail import Mail
from flask_security import Security, login_required, SQLAlchemySessionUserDatastore
from database import db_session, init_db
from models import User, Role
from form_extensions import ExtendedRegisterForm
import config

mail = Mail()
app = Flask(__name__)


app.config['DEBUG'] = True
app.config['SECRET_KEY'] = config.secret_key
app.config['SECURITY_PASSWORD_SALT'] = config.password_salt
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_CONFIRMABLE'] = True
app.config['MAIL_DEFAULT_SENDER'] = config.mail_default
app.config['MAIL_SERVER'] = config.mail_server
app.config['MAIL_PORT'] = config.mail_port
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = config.mail_username
app.config['MAIL_PASSWORD'] = config.mail_password

mail.init_app(app)

user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)

security = Security(
        app,
        user_datastore,
        confirm_register_form=ExtendedRegisterForm)

init_db()
def create_user():
    init_db()
    user_datastore.create_user(email='dsouzadyn@gmail.com', password='test@1234')
    db_session.commit()

@app.route('/')
@login_required
def home():
    return 'Here you go!'

if __name__ == '__main__':
    app.run()
