from data_generation.model.abstract_entity import Entity
import pandas as pd
import logging

from data_generation.entities.utils import CleanDataUtils, DirtyDataUtils

logging.basicConfig(level=logging.INFO)

"""
How to create an entity that will correspond to a table ?
Definition:
it is called entity because it is a table corresponding to a reality 
and it can be set with parameters that you can chose 

How to:
Define the dependencies with other entities
Define the mode of generation
Create a json that describes your entity with parameters
Create the functions to generate each column of your entity for either clean or dirty generation mode
Register your entity in the catalogue in __init__.py
Create a custom populate function to manage the IDs
"""

class Template(Entity):

    @property
    def table_name(self):
        return 'FIll the right name'

    def __init__(self):
        super().__init__()

    def populate(self):
        data = []
        self.generate_dependency_tables()
        utils_class = CleanDataUtils if self.configuration.mode == 'clean' else DirtyDataUtils
        record = []
        data.append(record)
        table = pd.DataFrame(data)