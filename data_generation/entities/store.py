from abstract_entity import Entity

class StoreManager(object):

    def run(self):
        pass

class Store(Entity):

    def __init__(self):
        self.store_ID = None
        self.address = None
        self.size = None
        self.repository_ID = None

