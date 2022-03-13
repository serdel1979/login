from flask_login import UserMixin



class Vacuna(UserMixin):
    def __init__(self, id, vacuna, cantidad):
        self.id = id
        self.vacuna = vacuna
        self.cantidad = cantidad