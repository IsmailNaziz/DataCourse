class EntitiesCatalogue(object):
    Entities = {}

    @staticmethod
    def register(obj):
        EntitiesCatalogue.Entities[obj.table_name] = obj

    @staticmethod
    def get_class_from_name(table_name):
        return EntitiesCatalogue.Entities[table_name]
