from abc import ABC, abstractmethod

class Inavegable(ABC):

    @abstractmethod
    def iniciar_navegacion(self):
        pass

    @abstractmethod
    def parar_navegacion(self):
        pass