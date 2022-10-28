from abstract_entity import Entity

class TransactionManager(object):

    def run(self):
        pass

class Transaction(Entity):

    def __init__(self):
        self.ID = None
        self.ticket_ID = None
        self.product_ID = None
        self.date = None
        self.amount = None
        self.payment_type = None