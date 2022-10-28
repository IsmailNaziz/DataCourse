import os
from abc import ABC, abstractmethod
import json
import logging

import pandas as pd

from entities_catalogue import EntitiesCatalogue
from utils import CleanDataUtils, DirtyDataUtils


class Entity(ABC):
    """
    for the moment, no checks of circular dependencies, only direct dependencies are accepted
    """
    TARGET_FOLDER = r'C:\Users\33768\Documents\Projects\DataCourse\data_generation\datawarehouse'
    CONFIGURATION_FOLDER = r'C:\Users\33768\Documents\Projects\DataCourse\data_generation\configuration_files'

    @property
    def configuration(self):
        #TODO: validate schema
        if os.path.exists(fr"{self.CONFIGURATION_FOLDER}/{self.table_name}.json"):
            with open(rf'{self.CONFIGURATION_FOLDER}/{self.table_name}.json', 'r') as j:
                return json.loads(j.read())
        else:
            raise Exception(f'Please, create a configuration file named {self.table_name}.json '
                            f'in the folder {self.CONFIGURATION_FOLDER} to create your class')

    @property
    @abstractmethod
    def table_name(self):
        pass

    def populate(self):
        data = {}
        self.generate_dependency_tables()
        utils_class = CleanDataUtils if self.configuration["generation_mode"] == 'clean' else DirtyDataUtils
        population_mode = self.configuration["population_mode"]
        beg_ID = 0 if population_mode == 'reset' else self.get_beg_ID()
        for ID in range(beg_ID, beg_ID + self.configuration["nb_records"]):
            record = [ID]
            for col_information in self.configuration["parameters"].values():
                func_name = col_information['values']['function']
                args = col_information['values']['args']
                if args is None:
                    record.append(getattr(utils_class, func_name)())
                else:
                    record.append(getattr(utils_class, func_name)(args))
            data[ID] = record
        table = pd.DataFrame.from_dict(data,
                                       orient='index',
                                       columns=[f'{self.table_name}_ID'] + [col for col in
                                                                            self.configuration["parameters"].keys()])
        self.export_csv(table, mode=population_mode)

    def generate_dependency_tables(self):
        if self.configuration["required_entities"]:
            remaining_files = self.get_remaining_dependencies()
            if remaining_files:
                for entity_name in remaining_files:
                    entity_obj = EntitiesCatalogue.get_class_from_name(entity_name)
                    entity_instance = entity_obj()
                    if entity_instance.get_remaining_dependencies():
                        raise Exception(f'Only direct dependencies are accepted, '
                                        f'create the tables {entity_instance.get_remaining_dependencies()} '
                                        f'in order to create {entity_instance} table')
                    try:
                        entity_obj.populate()
                        logging.warning(f'{entity_name} table created')
                    except Exception as e:
                        logging.error(f'Please check the implementation of the class related to the table {entity_name}')
                        raise e

    def get_remaining_dependencies(self):
        existing_files = [f.split('.')[0] for f in os.listdir(self.TARGET_FOLDER)
                          if f.split('.')[0] in self.configuration["required_entities"]]
        return list(set(self.configuration["required_entities"]) - set(existing_files))

    def get_beg_ID(self):
        if os.path.exists(f'{self.TARGET_FOLDER}/{self.table_name}.csv'):
            df = pd.read_csv(f'{self.TARGET_FOLDER}/{self.table_name}.csv')
            return max(df[f'{self.table_name}_ID'].astype(int))+1
        else:
            return 0

    def export_csv(self, table, mode='append'):
        assert mode in ("append", "reset")
        file_name = os.path.join(self.TARGET_FOLDER, f'{self.table_name}.csv')
        if mode == 'append':
            header = False
            if os.path.exists(file_name):
                header = True if os.path.getsize(file_name) == 0 else False
            table.to_csv(file_name, mode='a', index=False, header=header)
        else:
            table.to_csv(file_name, index=False)


#TODO add tests using entity mocks