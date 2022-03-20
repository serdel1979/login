from .entities.User import User
from datetime import datetime


class ModelUser():
    @classmethod
    def login(self,db,user):
        try:
            cursor = db.connection.cursor()
            sql="""SELECT * FROM users 
            WHERE username = '{}'""".format(user.username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0],row[1],User.check_password(row[2],user.password),row[3], row[4],row[5],row[6],row[7],row[8],row[9])
                return user
            else:
                return None

        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_by_id(self,db,id):
        try:
            cursor = db.connection.cursor()
            sql="""SELECT id, username, nombre FROM users 
            WHERE id = '{}'""".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0],row[1],None,row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_username(self,db,username):
        try:
            cursor = db.connection.cursor()
            sql="""SELECT id, username, nombre FROM users 
            WHERE username = '{}'""".format(username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0],row[1],None,row[2])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_dni(self,db,dni):
        try:
            cursor = db.connection.cursor()
            sql="""SELECT id, username, password, nombre, apellido, dni, telefono, mail, fecha_nacimiento, tiene_dosis, factor_riesgo FROM users 
            WHERE dni = '{}'""".format(dni)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                # id, username, password, nombre, apellido, dni, telefono, mail, fecha_nacimiento, tiene_dosis, factor_riesgo 
                return User(row[0],row[1],None,row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_mail(self,db,mail):
        try:
            cursor = db.connection.cursor()
            sql="""SELECT id, username, password, nombre, apellido, dni, telefono, mail, fecha_nacimiento, tiene_dosis, factor_riesgo FROM users 
            WHERE mail = '{}'""".format(mail)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                # id, username, password, nombre, apellido, dni, telefono, mail, fecha_nacimiento, tiene_dosis, factor_riesgo 
                return User(row[0],row[1],None,row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)



    @classmethod
    def guardar_usuario(self,db,username,password,nombre="",apellido="",dni="",telefono="",mail="",fecha_nacimiento=datetime.now(),tiene_dosis=1,factor_riesgo=0):
        try:
            tipo = 2
            cursor = db.connection.cursor()
            password = User.genera_hash_password(password)
            cursor.execute("INSERT INTO `users` (`id`,`username`,`password`,`nombre`,`apellido`,`dni`,`telefono`,`mail`,`fecha_nacimiento`,`tiene_dosis`,`factor_riesgo`,`tipo`) VALUES (NULL,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"
            .format(username, password, nombre,apellido,dni,telefono,mail,fecha_nacimiento,tiene_dosis,factor_riesgo, tipo))
            cursor.fetchone()
            db.connection.commit()
            cursor.close()
            
        except Exception as ex:
            raise Exception(ex)