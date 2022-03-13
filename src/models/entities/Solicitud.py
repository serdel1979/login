from flask_login import UserMixin



class Solicitud(UserMixin):
    def __init__(self, id, id_user, id_vacuna, vacuna, fecha_solicitud, fecha_turno):
        self.id = id
        self.id_user = id_user
        self.id_vacuna = id_vacuna
        self.vacuna = vacuna
        self.fecha_solicitud = fecha_solicitud
        self.fecha_turno = fecha_turno
