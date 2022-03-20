from .entities.Vacuna import Vacuna


class ModelVacuna():
    @classmethod
    def get_all(self,db):
        try:
            cursor = db.connection.cursor()
            sql="""SELECT id, vacuna FROM vacunas""".format()
            cursor.execute(sql)
            vacunas = cursor.fetchall()
            if vacunas != None:
                return vacunas
            else:
                return None

        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_by_id(self,db,id):
        try:
            cursor = db.connection.cursor()
            sql="""SELECT id, vacuna FROM vacunas 
            WHERE id = '{}'""".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return Vacuna(row[0],row[1])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)



    @classmethod
    def get_by_nombre_vacuna(self,db,vacuna):
        try:
            cursor = db.connection.cursor()
            sql="""SELECT id, vacuna FROM vacunas 
            WHERE vacuna = '{}'""".format(vacuna)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return Vacuna(row[0],row[1])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)



    #"DELETE FROM `users` WHERE `users`.`id` = 24"

    
    @classmethod
    def eliminar_vacuna(self,db,id):
        try:
            cursor = db.connection.cursor()
            cursor.execute("DELETE FROM `vacunas`  WHERE id = '{}'".format(id))
            cursor.fetchone()
            db.connection.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)




    @classmethod
    def guardar_vacuna(self,db,vacuna):
        try:
            cursor = db.connection.cursor()
            cursor.execute("INSERT INTO `vacunas` (`id`,`vacuna`) VALUES (NULL,'{}','{}')".format(vacuna))
            cursor.fetchone()
            db.connection.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)


    #cur.execute("UPDATE vacunas SET vacuna=%s, cantidad=%s WHERE id=%s", (vacuna, cantidad, id))

    @classmethod
    def guardar_edicion(self,db,id,vacuna):
        try:
            cursor = db.connection.cursor()
            cursor.execute("UPDATE vacunas SET vacuna=%s WHERE id=%s", (vacuna, id))
            cursor.fetchone()
            db.connection.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)
