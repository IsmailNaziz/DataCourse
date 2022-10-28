from abstract_entity import Entity

class TicketManager(object):

    def run(self):
        pass

class Ticket(Entity):

    def __init__(self):
        self.ID = None
        self.store_ID = None
        self.client_ID = None
        self.date = None
        self.payment_type = None # in coherence with transactions
