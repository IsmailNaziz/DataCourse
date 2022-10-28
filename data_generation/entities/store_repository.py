from abstract_entity import Entity

class StoreRepositoryManager(object):

    def run(self):
        pass

class StoreRepository(Entity):

    def __init__(self):
        self.store_ID = None
        self.store_repository_ID = None
        self.product_ID = None
        self.quantity = None