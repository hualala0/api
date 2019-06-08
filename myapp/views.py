from flask import  render_template,redirect,url_for,flash,session,request,make_response,jsonify,abort
from myapp import  app
from myapp.models import db,User,Product,Up
import json
import datetime
from sqlalchemy import distinct
from PIL import Image
import numpy as np
from myapp.loadimage.imnumeralrecognition import loadImage,rtnY

class DateEnconding(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.date):
            return o.strftime('%Y/%m/%d')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/docs')
def docs():
    return render_template('docs.html')

@app.route('/signin',methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        if User.query.filter_by(uname=request.form['username'],
                                pwd=request.form['pwd']).first() is not None:
            session['user'] = request.form['username']
        else:
            return '0'
    if 'user' in session:
        return redirect(url_for('user', user=session['user']))
    else:
        return render_template('signin.html')
app.secret_key = '123456'

@app.route('/signup',methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        if User.query.filter_by(uname=request.form['username']).first() is None:
            db.session.add(User(request.form['username'], request.form['pwd']))
            db.session.commit()
            return redirect(url_for('signin'))
        else: return '0'
    else:
        return render_template('signup.html')

@app.route('/signout')
def signout():
    session.pop('user', None)
    return redirect(url_for('signin'))

@app.route('/user/<user>/myinfomation')
def user(user):
    if 'user' in session:
        return render_template('myinfo.html',user=user)
    else:
        return redirect(url_for('signin'))


@app.route('/user/<user>/apimanagement',methods=['GET', 'POST'])
def apima(user):
    if 'user' in session:
        if request.method != 'POST':
            data = db.session.query(distinct(Product.pname))\
                .join(Up, Product.pid == Up.pid)\
                .join(User, Up.uid == User.uid).filter_by(uname=user)
            return render_template('apimana.html', user=user, data=data)
        else:
            try:
                p = Product.query.filter_by(pname=request.form['pname']).first()
                u = User.query.filter_by(uname=request.form['uname']).first()
                db.session.query(Up).filter_by(uid=u.uid,pid=p.pid).delete()
                db.session.commit()
            except BaseException:
                return '0'
            else:
                return '1'
    else:
        return redirect(url_for('signin'))

@app.route('/user/<user>/apimanagement/addapi',methods=['GET', 'POST'])
def addapi(user):
    if 'user' in session:
        if request.method != 'POST':
            products = Product.query.all()
            return render_template('addapi.html', user=user, products=products)
        else:

            try:
                p = Product.query.filter_by(pname=request.form['data']).first()
                u = User.query.filter_by(uname=user).first()
                if(Up.query.filter_by(uid=u.uid,pid=p.pid).first() is None):
                    db.session.add(Up(u.uid, p.pid))
                    db.session.commit()
                else:
                    return '0'

            except BaseException:
                return '0'
            else:
                return '1'
    else:
        return redirect(url_for('signin'))

@app.route('/user/<user>/datastatistics',methods=['GET', 'POST'])
def datastas(user):
    if 'user' in session:
        if request.method != 'POST':
            data = db.session.query(distinct(Product.pname))\
                .join(Up, Product.pid == Up.pid)\
                .join(User, Up.uid == User.uid).filter_by(uname=user)
            return render_template('datastas.html', user=user, data=data)
        else:
            rtn = []
            p = Product.query.filter_by(pname=request.form['pname']).first()
            u = User.query.filter_by(uname=request.form['uname']).first()
            up1 = db.session.query(Up.date,Up.count).filter_by(pid=p.pid,uid=u.uid)
            for up in up1:

                rtn.append(up)
            return json.dumps(rtn,cls=DateEnconding)
    else:
        return redirect(url_for('signin'))

@app.route('/apis/numeralrecognition',methods=['POST'])
def api1():
    try:
        p = Product.query.filter_by(pname='numeralrecognition').first()
        u = User.query.filter_by(uname=request.form['user']).first()
        up = Up.query.filter_by(uid=u.uid, pid=p.pid, date=datetime.date.today()).first()
        img = request.files.get('file')
        im = Image.open(img)
    except BaseException:
        abort(400)
    else:
        if Up.query.filter_by(uid=u.uid,pid=p.pid).first() is not None:
            if up is None:
                db.session.add(Up(u.uid, p.pid,datetime.date.today()))
                db.session.commit()
            else:
                up.count += 1
            db.session.commit()
            w = np.load("myapp/networks/w.npy")
            w_h = np.load("myapp/networks/w_h.npy")
            imdata = loadImage(im)
            y = rtnY(imdata,w,w_h)
            return jsonify(str(y))
        else:
            abort(400)