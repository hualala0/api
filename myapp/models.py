from myapp import app
from flask_sqlalchemy import SQLAlchemy
import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/user.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)
class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(50), unique=True)
    pwd = db.Column(db.String(50))

    def __init__(self, uname, pwd):
        self.uname = uname
        self.pwd = pwd

class Product(db.Model):
    __tablename__ = 'product'
    pid = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(50), unique=True)

    def __init__(self, pname):
        self.pname = pname

class Up(db.Model):
    __tablename__ = 'up'
    uid = db.Column(db.Integer ,db.ForeignKey('user.uid'), primary_key=True)
    pid = db.Column(db.Integer, db.ForeignKey('product.pid'), primary_key=True)
    count = db.Column(db.Integer, default=0)
    date = db.Column(db.Date, default=(datetime.date.today()), primary_key=True)

    def __init__(self, *args):
        if len(args) == 2:
            self.uid, self.pid = args
        if len(args) == 3:
            self.uid, self.pid, self.date = args

db.create_all()

