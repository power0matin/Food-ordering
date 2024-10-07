class Admin:
    def __init__(self, admin_id, name, email, password):
        self.admin_id = admin_id
        self.name = name
        self.email = email
        self.password = password

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter
    def name(self):
        self._name = None
