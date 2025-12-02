from abc import ABC, abstractmethod
from INavegable import INavegable

class Embarcacion(ABC, INavegable):
    # Atributos de clase (solo accesibles desde Embarcacion)
    __num_barcos = 0
    __num_barcos_navegando = 0
    __tiempo_total_navegacion_acumulado = 0  # en minutos

    # Constantes públicas
    PATRON_POR_DEFECTO = "Sin patrón"
    RUMBO_POR_DEFECTO = "Sin rumbo"
    MIN_TRIPULANTES = 0  # excluye al patrón

    # Constructor con dos parámetros
    def __init__(self, nombre, num_max_tripulantes):
        # Validación del nombre
        if nombre is None:
            raise Exception("El nombre de la embarcación es obligatorio.")
        if isinstance(nombre, str) and nombre.strip() == "":
            raise Exception("El nombre de la embarcación no puede estar vacío.")
        # (si no es str, dejamos que Python lance su propio error o lo tratamos igual que None)

        # Validación del número máximo de tripulantes
        if num_max_tripulantes < Embarcacion.MIN_TRIPULANTES:
            raise Exception(
                f"El número de tripulantes debe ser, como mínimo, {Embarcacion.MIN_TRIPULANTES}."
            )

        # Atributos "constantes" de objeto (solo Embarcacion)
        self.__nombre_barco = nombre
        self.__num_max_tripulantes = num_max_tripulantes

        # Atributos de estado accesibles desde subclases (protegidos)
        self._navegando = False
        self._velocidad = 0
        self._rumbo = Embarcacion.RUMBO_POR_DEFECTO
        self._patron = Embarcacion.PATRON_POR_DEFECTO
        self._num_tripulantes = 0
        self._tiempo_total_navegacion = 0  # en minutos

        # Actualizar atributos de clase
        Embarcacion.__num_barcos += 1

    # --- Getters de objeto ---

    def get_nombre_barco(self):
        return self.__nombre_barco

    def get_num_max_tripulantes(self):
        return self.__num_max_tripulantes

    def is_navegando(self):
        return self._navegando

    def get_velocidad(self):
        return self._velocidad

    def get_rumbo(self):
        return self._rumbo

    def get_patron(self):
        return self._patron

    def get_tripulacion(self):
        return self._num_tripulantes

    def get_tiempo_total_navegacion(self):
        return self._tiempo_total_navegacion  # en minutos

    # --- Métodos de clase (información global) ---

    @classmethod
    def get_num_barcos(cls):
        return cls.__num_barcos

    @classmethod
    def get_num_barcos_navegando(cls):
        return cls.__num_barcos_navegando

    @classmethod
    def get_tiempo_total_navegancion_acumulado(cls):
        return cls.__tiempo_total_navegacion_acumulado  # en minutos

    # --- Modificación de atributos ---

    def set_rumbo(self, nuevo_rumbo):
        if not self._navegando:
            raise Exception(
                f"La embarcación {self.__nombre_barco} no está navegando, no se puede cambiar el rumbo."
            )
        if nuevo_rumbo == self._rumbo:
            raise Exception(
                f"La embarcación {self.__nombre_barco} ya está navegando con ese rumbo "
                f"({self._rumbo}), debes indicar un rumbo distinto para poder modificarlo."
            )

        self._rumbo = nuevo_rumbo

    # --- Métodos de la interfaz Navegable ---

    def iniciar_navegacion(self, velocidad, rumbo, patron, num_tripulantes):
        if self._navegando:
            raise Exception(
                f"La embarcación {self.__nombre_barco} ya está navegando y se encuentra fuera de puerto."
            )

        if isinstance(rumbo, str) and rumbo.strip() == "":
            raise Exception("Debes indicar el rumbo para iniciar la navegación.")

        if isinstance(patron, str) and patron.strip() == "":
            raise Exception(
                "El patrón de la embarcación no puede estar vacío, se necesita un patrón para iniciar la navegación."
            )

        if num_tripulantes < Embarcacion.MIN_TRIPULANTES or \
           num_tripulantes > self.__num_max_tripulantes:
            raise Exception(
                f"El número de tripulantes debe estar entre {Embarcacion.MIN_TRIPULANTES} "
                f"y {self.__num_max_tripulantes}."
            )

        # Asignar estado de navegación
        self._velocidad = velocidad
        self._rumbo = rumbo
        self._patron = patron
        self._num_tripulantes = num_tripulantes
        self._navegando = True

        Embarcacion.__num_barcos_navegando += 1

    def parar_navegacion(self, tiempo_minutos):
        if not self._navegando:
            raise Exception(f"La embarcación {self.__nombre_barco} no está navegando.")

        if tiempo_minutos <= 0:
            raise Exception("Tiempo navegando incorrecto, debe ser mayor que cero.")

        # Actualizar tiempos
        self._tiempo_total_navegacion += tiempo_minutos
        Embarcacion.__tiempo_total_navegacion_acumulado += tiempo_minutos

        # Resetear estado de navegación
        self._navegando = False
        self._velocidad = 0
        self._rumbo = Embarcacion.RUMBO_POR_DEFECTO
        self._patron = Embarcacion.PATRON_POR_DEFECTO
        self._num_tripulantes = 0

        Embarcacion.__num_barcos_navegando -= 1

    # --- Método abstracto de señalización ---

    @abstractmethod
    def señalizar(self):
        pass

    # --- Representación en texto ---

    def __str__(self):
        navegando_txt = "Sí" if self._navegando else "No"

        partes = [
            f"Nombre de la embarcación: {self.__nombre_barco}",
            f"Tripulación: {self._num_tripulantes}",
            f"Navegando: {navegando_txt}",
        ]

        if self._navegando:
            partes.append(
                f"con el patrón {self._patron} en {self._rumbo} a {self._velocidad} nudos"
            )

        horas = self._tiempo_total_navegacion / 60.0
        partes.append(f"Tiempo total de navegación del barco: {horas} horas")

        return ", ".join(partes)
