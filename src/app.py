from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from config import config
from models.ModelSolicitudes import ModelSolicitud
from models.ModelUser import ModelUser
from models.entities.Solicitud import Solicitud
from models.entities.User import User
from flask_login import LoginManager, login_user, logout_user, login_required
from datetime import datetime

from models.entities.Vacuna import Vacuna
from models.ModelVacuna import ModelVacuna

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
                session["tipo"]= logged_user.tipo
                session["id_user"] = logged_user.id
                return render_template('home.html',tipo = session["tipo"])
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
    return render_template('home.html',tipo = session["tipo"])


@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/guarda_usuario', methods=['GET','POST'])
@login_required
def guardar_usuario():
    if request.method=='POST':
        username = request.form['username']
        user = ModelUser.get_by_username(db,username)
        if user != None:
            flash("El usuario ya existe...")
            return render_template('registro.html')
        fullname = request.form['fullname']
        password = request.form['password1']
        password2 = request.form['password2']
        if(password != password2):
            flash("Las contraseñas no coinciden...")
            return render_template('registro.html')
        ModelUser.guardar_usuario(db,username,password,fullname)
        flash("Registrado...")
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    

@app.route('/vacunas')
@login_required
def vacunas():
    vacunas = []
    tabla = list(ModelVacuna.get_all(db))
    for i in tabla:
        vacunas.append(list(i))
    print(vacunas)
    return render_template('vacunas.html', tipo = session["tipo"], vacunas = vacunas)

@app.route('/vacuna/<int:id>')
@login_required
def editarVacuna(id):
    vacuna = ModelVacuna.get_by_id(db,id)
    return render_template('editar_vacuna.html', tipo = session["tipo"], vacuna = vacuna, id = id)

@app.route('/guarda_edicion_vacuna/<int:id>', methods=['GET','POST'])
@login_required
def guarda_edicion_vacuna(id):
    if request.method=='POST':
        vacuna = request.form['vacuna']
        cantidad = request.form['cantidad']
        ModelVacuna.guardar_edicion(db,id,vacuna,cantidad)
    return redirect(url_for('vacunas'))


@app.route('/eliminar_vacuna/<int:id>', methods=['GET','POST'])
@login_required
def eliminar_vacuna(id):
    ModelVacuna.eliminar_vacuna(db,id)
    flash("Eliminada...")
    return redirect(url_for('vacunas'))


@app.route('/agregar_vacuna')
@login_required
def agregar_vacuna():
    return render_template('form_agregar_vacuna.html', tipo = session["tipo"])  



@app.route('/guarda_vacuna', methods=['GET','POST'])
@login_required
def guardar_vacuna():
    if request.method=='POST':
        nvacuna = request.form['vacuna']
        vacuna = ModelVacuna.get_by_nombre_vacuna(db,nvacuna)
        if vacuna != None:
            flash("La vacuna ya existe!!!...")
            return render_template('form_agregar_vacuna.html')
        cantidad = request.form['cantidad']
        ModelVacuna.guardar_vacuna(db,nvacuna,cantidad)
        flash("Vacuna guardada...")
    return redirect(url_for('vacunas'))
    
@app.route('/solicitar_turno/<int:id>')
@login_required
def guarda_solicitud_turno(id):
    vacunas = []
    id_vacuna = id
    id_user = session["id_user"]
    vacuna = ModelVacuna.get_by_id(db,id)
    vacuna = vacuna.vacuna
    fecha_solicitud = datetime.now()
    ModelSolicitud.guardar_solicitud(db,id_user,id_vacuna,vacuna,fecha_solicitud)
    tabla = list(ModelVacuna.get_all(db))
    for i in tabla:
        vacunas.append(list(i))
    flash("Solicitud aceptada!!...")
    return render_template('solicitar_turno.html', tipo = session["tipo"], vacunas = vacunas)

@app.route('/solicitar_turno')
@login_required
def solicitar_turno():
    vacunas = []
    tabla = list(ModelVacuna.get_all(db))
    for i in tabla:
        vacunas.append(list(i))
    return render_template('solicitar_turno.html', tipo = session["tipo"], vacunas = vacunas)

@app.route('/mis_turnos')
@login_required
def mis_turnos():
    id = session["id_user"]
    solicitudes = []
    tabla = list(ModelSolicitud.get_solicitudes_usuario(db,id))
    for i in tabla:
        solicitudes.append(list(i))
    return render_template('mis_turnos.html', tipo = session["tipo"], solicitudes = solicitudes)


@app.route('/ver_solicitudes')
@login_required
def ver_solicitudes():
    solicitudes=ModelSolicitud.get_all(db)
    return render_template('solicitudes.html', tipo = session["tipo"], solicitudes = solicitudes)


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