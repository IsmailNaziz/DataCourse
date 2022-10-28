from model.abstract_entity import Entity
import pandas as pd
import logging

from entities.utils import CleanDataUtils, DirtyDataUtils

logging.basicConfig(level=logging.INFO)


class Client(Entity):

    @property
    def table_name(self):
        return 'client'




if __name__ == "__main__":
    target_folder = r'C:\Users\33768\Documents\Data course\datawarehouse'
    C = Client()
    C.populate()
