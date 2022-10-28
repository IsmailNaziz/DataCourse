from abstract_entity import Entity

class MarketingManager(object):

    def run(self):
        pass

class Marketing(Entity):

    def __init__(self):
        self.ID = None
        self.client_ID = None
        self.consultation_date = None
        self.acquisition_channel = None
