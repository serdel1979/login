from click import password_option
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from datetime import datetime

# id, username, password, nombre, apellido, dni, telefono, mail, fecha_nacimiento, tiene_dosis, factor_riesgo 

class User(UserMixin):
    def __init__(self, id, username, password, nombre="", apellido="", dni=321, telefono="", mail="", fecha_nacimiento=datetime.now(), tiene_dosis=0, factor_riesgo=0, tipo=2):
        self.id = id
        self.username = username
        self.password = password
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono= telefono
        self.mail = mail
        self.fecha_nacimiento = fecha_nacimiento
        self.tiene_dosis = tiene_dosis
        self.factor_riesgo = factor_riesgo 
        self.tipo = tipo
        
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

    @classmethod
    def genera_hash_password(self, password):
        return generate_password_hash(password)


#print(generate_password_hash("admin"))