from flask_login import UserMixin



class Vacuna(UserMixin):
    def __init__(self, id, vacuna):
        self.id = id
        self.vacuna = vacuna