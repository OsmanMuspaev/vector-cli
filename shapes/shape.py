from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def info(self):
        pass

    def update(self, params):
        pass

    def __str__(self):
        return self.info()