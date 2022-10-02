from abc import ABC, abstractmethod

class EntityManager(ABC):
    @property
    @abstractmethod
    def table_name(self):
        pass

    @abstractmethod
    def populate(self):
        pass

class Entity(ABC):
    @property
    @abstractmethod
    def prefix(self):
        pass
    @property
    @abstractmethod
    def name(self):
        pass

class Test(Entity):
    pass


if __name__ == "__main__":
    t = Test()