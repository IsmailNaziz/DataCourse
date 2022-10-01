from abstract_entity import Entity

class WareHouseManager(object):

    def run(self):
        pass

class WareHouse(Entity):

    def __init__(self):
        self.ware_house_ID = None
        self.product_ID = None
        self.entry_date = None
        self.quantity = None
        self.provider = None
        self.address = None
        self.exit_date = None
