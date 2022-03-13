from .entities.Solicitud import Solicitud


class ModelSolicitud():
    @classmethod
    def get_all(self,db):
        try:
            cursor = db.connection.cursor()
            sql="""SELECT id, id_user, id_vacuna, vacuna, fecha_solicitud, fecha_turno FROM solicitud_turnos""".format()
            cursor.execute(sql)
            solicitudes = cursor.fetchall()
            if solicitudes != None:
                return solicitudes
            else:
                return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_solicitudes_usuario(self,db,id_usuario):
        try:
            cursor = db.connection.cursor()
            sql="""SELECT id, id_user, id_vacuna, vacuna, fecha_solicitud, fecha_turno FROM solicitud_turnos 
            WHERE id_user = '{}'""".format(id_usuario)
            cursor.execute(sql)
            solicitudes = cursor.fetchall()
            if solicitudes != None:
                return solicitudes
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def guardar_solicitud(self,db,id_user,id_vacuna,vacuna,fecha_solicitud,fecha_turno = None):
        try:
            cursor = db.connection.cursor()
            cursor.execute("INSERT INTO `solicitud_turnos` (`id`,`id_user`,`id_vacuna`,`vacuna`,`fecha_solicitud`,`fecha_turno`) VALUES (NULL,'{}','{}','{}','{}',NULL)".format(id_user,id_vacuna,vacuna,fecha_solicitud))
            cursor.fetchone()
            db.connection.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def asignar_turno(self,db,id,fecha_turno):
        try:
            cursor = db.connection.cursor()
            cursor.execute("UPDATE solicitud_turnos SET fecha_turno=%s WHERE id=%s", (fecha_turno, id))
            cursor.fetchone()
            db.connection.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)

    #"DELETE FROM `users` WHERE `users`.`id` = 24"

"""
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
"""


    


    #cur.execute("UPDATE vacunas SET vacuna=%s, cantidad=%s WHERE id=%s", (vacuna, cantidad, id))

    