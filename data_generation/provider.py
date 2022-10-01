from abstract_entity import Entity

class ProviderManager(object):

    def run(self):
        pass

class Provider(Entity):

    def __init__(self):
        self.provider_ID = None
        self.product_ID = None
        self.end_of_date_contract = None
