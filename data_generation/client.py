from abstract_entity import Entity

class ClientManager(object):

    def run(self):
        pass

class Client(Entity):

    def __init__(self):
        self.client_ID = self._init_client_ID()
        self.first_name = self._init_first_name()
        self.last_name = self._init_last_name()
        self.birthday = self._init_birthday()
        self.address = self._init_address()
        self.gender = self._init_gender()
        self.phone_number = self._init_phone_number()
        self.email = self._init_gender()
        self.account_creation_date = self._init_account_creation_date()

    @staticmethod
    def _init_ID():
        return

    @staticmethod
    def _init_birthday():
        pass

    @staticmethod
    def _init_address():
        pass

    @staticmethod
    def _init_first_name():
        pass

    @staticmethod
    def _init_last_name():
        pass

    @staticmethod
    def _init_gender():
        pass

    @staticmethod
    def _init_phone_number():
        pass

    @staticmethod
    def _init_account_creation_date():
        pass