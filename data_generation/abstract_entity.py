from abc import ABC, abstractmethod


class Entity(ABC):

    @property
    @abstractmethod
    def name(self):
        pass


class Test(Entity):
    pass


if __name__ == "__main__":
    t = Test()