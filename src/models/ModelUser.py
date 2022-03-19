from .entities.User import User


class ModelUser():
    @classmethod
    def login(self,db,user):
        try:
            cursor = db.connection.cursor()
            sql="""SELECT id, username, password, nombre, tipo FROM users 
            WHERE username = '{}'""".format(user.username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0],row[1],User.check_password(row[2],user.password),row[3], row[4])
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
    def guardar_usuario(self,db,username,password,nombre):
        try:
            tipo = 2
            cursor = db.connection.cursor()
            password = User.genera_hash_password(password)
            cursor.execute("INSERT INTO `users` (`id`,`username`,`password`,`nombre`,`tipo`) VALUES (NULL,'{}','{}','{}','{}')".format(username, password, nombre, tipo))
            cursor.fetchone()
            db.connection.commit()
            cursor.close()
            
        except Exception as ex:
            raise Exception(ex)