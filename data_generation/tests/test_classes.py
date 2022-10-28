from model.abstract_entity import Entity

class MockEntity0(Entity):
    @property
    def table_name(self):
        return 'mock_class_0'


class MockEntity1(Entity):
    @property
    def table_name(self):
        return 'mock_class_1'


class MockEntity2(Entity):
    @property
    def table_name(self):
        return 'mock_class_2'
