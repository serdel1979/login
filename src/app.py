from flask import Flask, flash, redirect, render_template, request, url_for
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from config import config
from models.ModelUser import ModelUser
from models.entities.User import User
from flask_login import LoginManager, login_user, logout_user, login_required

app=Flask(__name__)

csrf=CSRFProtect()

#Hace conexión con bd
db = MySQL(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        user = User(0,username,password)
        logged_user=ModelUser.login(db,user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Datos incorrectos...")
                return render_template('auth/login.html')
        else:
            flash("Usuario no encontrado...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))



@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.route('/pagina1')
@login_required
def pagina1():
    return render_template('pagina1.html')

@app.route('/pagina2')
@login_required
def pagina2():
    return render_template('pagina2.html')


def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>Página no encontrada</h1>"


if __name__=='__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401,status_401)
    app.register_error_handler(404,status_404)
    app.run()