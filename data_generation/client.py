from abstract_entity import Entity, EntityManager
import pandas as pd
import os

class ClientManager(EntityManager):

    @property
    def table_name(self):
        return 'Client'

    def __init__(self, nb_clients=300):
        super().__init__()
        self.nb_clients = nb_clients
        self.table = pd.DataFrame()

    def populate(self):
        data = []
        clients = [Client() for _ in range(self.nb_clients)]
        for client in clients:
            data.append(client.__dict__)
        self.table = pd.DataFrame(data)

    def export_csv(self, target_folder, mode='append'):
        assert mode in ("append", "reset")
        file_name = os.path.join(target_folder, f'{self.table_name}.csv')
        if mode == 'append':
            self.table.to_csv(file_name, mode='a', index=False)
        else:
            self.table.to_csv(file_name, index=False)

class Client(Entity):

    def __init__(self):
        self.client_ID = 4
        self.first_name = 'po'
        self.last_name = 'ma'
        self.birthday = '02/07/1984'
        self.address = 'somewhere'
        self.gender = 'Male'
        self.email = 'o@smth.com'
        self.account_creation_date ='08/12/2015'
        self.profession = 'tester'

    @property
    def prefix(self):
        return 'CL'

    @property
    def name(self):
        return 'Client'

if __name__ == "__main__":
    target_folder = r'C:\Users\33768\Documents\Data course\datawarehouse'
    CM = ClientManager()
    CM.populate()
    CM.export_csv(target_folder, mode='reset')
