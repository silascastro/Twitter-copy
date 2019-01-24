from app import app, db, lm
from flask_login import login_user, logout_user, current_user
from flask import render_template, flash, redirect, url_for, request

from app.models.tables import User, Post
from app.models.forms import LoginForm, SinginForm, Toilt



@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

#1ª rota
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/submit', methods=["POST"])
def submit():
    #return "{}".format(request.form['texto'])
    lista = request.referrer.split('/')
    #print(lista)

    if request.form['texto'] != '':
        p = Post(request.form['texto'],current_user.id)
        db.session.add(p)
        db.session.commit()
        #if current_user.is_authenticated:
        #   print(current_user.id)
        #else:
        #    print('não')

    if len(lista)==5:
        return redirect(url_for( lista[4], username=lista[3],))
    else:
        if len(lista)==4:
            if lista[3]=='':
                return redirect(url_for('index'))
            if lista[3]!='':
                return redirect(url_for('profile',username=lista[3]))
            

@app.route('/login', methods=["GET","POST"])
def login():

    form = LoginForm()

    if current_user.is_authenticated:
        print(current_user.name)
        return redirect(url_for('profile',username=current_user.username))
    else:
        if form.validate_on_submit():
            print("ok") 
            user = User.query.filter_by(username=form.username.data).first()
            
            if user and user.password == form.password.data:
                login_user(user)
                flash("Logged in.")

                #print(type(user))
                return redirect(url_for('profile',username=user.username))
            else:
                flash("Invalid login.")

            
        return render_template('login.html', form=form)


@app.route("/singin", methods=["GET","POST"])
def singin():
    form = SinginForm()

    if current_user.is_authenticated:
        return redirect(url_for('profile', username=current_user.username))
    else:
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
    posts = Post.query.filter_by(user_id=current_user.id).all()
    print(posts)
    return render_template('profile.html',posts=posts)

@app.route("/<username>/followers")
def followers(username):
    return render_template('followers.html')

@app.route("/<username>/following")
def following(username):
    return render_template('following.html')











#@app.route("/teste/<info>")
#@app.route("/teste", defaults={"info":None})
#def teste(info):
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
    #return "ok"