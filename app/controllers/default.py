from app import app, db, lm
from flask_login import login_user, logout_user
from flask import render_template, flash, redirect, url_for

from app.models.tables import User
from app.models.forms import LoginForm, SinginForm

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

#1ª rota
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=["GET","POST"])
def login():

    form = LoginForm()
   
    
    if form.validate_on_submit():
        print("ok") 
        user = User.query.filter_by(username=form.username.data).first()
        
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in.")

            #print(type(user))
            return redirect(url_for('index'))
        else:
            flash("Invalid login.")
          
    return render_template('login.html', form=form)


@app.route("/singin", methods=["GET","POST"])
def singin():
    form = SinginForm()

    if form.validate_on_submit():
        newUser = User(name=form.name.data,email=form.email.data,username=form.username.data,password=form.password.data)
        #objetos de comparacao
        user = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.username.data).first()
        
        if not user and  not email:
            db.session.add(newUser)
            db.session.commit()
            login_user(newUser)
            flash('conta criada com sucesso!')
            return redirect(url_for('profile', username=newUser.username))
        else:
            flash('Usuário já existe!')
        print("ok")
    return render_template('singin.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash('Logout.')
    return redirect(url_for('index'))

@app.route("/<username>")
def profile(username):
    return render_template('profile.html')

@app.route("/teste/<info>")
@app.route("/teste", defaults={"info":None})
def teste(info):
    #delete
    #d = User.query.filter_by(username='neoHead').first()
    #db.session.delete(d)
    #db.session.commit()

    #update
    #u = User.query.filter_by(password="1234").first()
    #u.password = "123"
    #db.session.add(u)
    #db.session.commit()
    
    #SELECT
    #r = User.query.filter_by(password='1234').first()
    #print(r.username)
    #return "ok"
    #INSERT
    #i = User("silascastro","1234","silascastro15","silascastro15@gmail.com")
    #db.session.add(i)
    #db.session.commit()
    #update
    return "ok"