from abstract_entity import Entity

class ProductManager(object):

    def run(self):
        pass

class Product(Entity):

    def __init__(self):
        self.ID = None
        self.category = None
        self.price = None
        self.cost = None
        self.expiry_date = None
        self.volume = None
        self.fragile = None
        self.provider = None
