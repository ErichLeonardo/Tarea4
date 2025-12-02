from abc import ABC, abstractmethod

class IRegateable(ABC):
    @abstractmethod
    def iniciar_regata(self):
        pass