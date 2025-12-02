from embarcacion import Embarcacion

class Lancha(Embarcacion):
    # Atributos de clase
    __num_lanchas = 0                 # número de lanchas creadas
    __num_lanchas_navegando = 0       # número de lanchas navegando

    # Constantes de clase
    MIN_MOTORES = 1
    MAX_MOTORES = 2

    MIN_COMBUSTIBLE = 8               # litros
    MAX_COMBUSTIBLE = 50              # litros

    FACTOR_COMBUSTIBLE = 0.026

    MIN_VELOCIDAD_LANCHA = 1          # nudos
    MAX_VELOCIDAD_LANCHA = 50         # nudos

    # Constructor
    def __init__(self, nombre=None, num_max_tripulantes=None,
                 num_motores=None, nivel_combustible=None):
        """
        Lancha()  -> constructor sin parámetros:
            nombre = 'Lancha X'       (X = número de lanchas creadas + 1)
            num_max_tripulantes = Embarcacion.MIN_TRIPULANTES
            num_motores = MIN_MOTORES
            nivel_combustible = MAX_COMBUSTIBLE
            NO lanza excepciones.

        Lancha(nombre, num_max_tripulantes, num_motores, nivel_combustible)
            -> constructor con parámetros:
               valida num_motores y nivel_combustible y, si son incorrectos,
               lanza las excepciones indicadas en el enunciado.
        """

        # Constructor sin parámetros
        if (nombre is None and num_max_tripulantes is None and
            num_motores is None and nivel_combustible is None):

            Lancha.__num_lanchas += 1
            nombre_auto = f"Lancha {Lancha.__num_lanchas}"

            # llamar al constructor de la superclase
            super().__init__(nombre_auto, Embarcacion.MIN_TRIPULANTES)

            # atributos propios de lancha
            self.__num_motores = Lancha.MIN_MOTORES
            self.__nivel_combustible = Lancha.MAX_COMBUSTIBLE

        # Constructor con parámetros
        else:
            # primero, que Embarcacion valide nombre y tripulantes
            super().__init__(nombre, num_max_tripulantes)

            # validar número de motores
            if (not isinstance(num_motores, int) or
                num_motores < Lancha.MIN_MOTORES or
                num_motores > Lancha.MAX_MOTORES):
                raise Exception(
                    f"El número de motores debe estar entre "
                    f"{Lancha.MIN_MOTORES} y {Lancha.MAX_MOTORES}."
                )

            # validar nivel de combustible
            if (not isinstance(nivel_combustible, (int, float)) or
                nivel_combustible < Lancha.MIN_COMBUSTIBLE or
                nivel_combustible > Lancha.MAX_COMBUSTIBLE):
                raise Exception(
                    f"El nivel de combustible debe estar entre "
                    f"{Lancha.MIN_COMBUSTIBLE} y {Lancha.MAX_COMBUSTIBLE}."
                )

            # si todo va bien, asignamos atributos propios
            self.__num_motores = int(num_motores)
            self.__nivel_combustible = int(nivel_combustible)

            Lancha.__num_lanchas += 1

    # Getters
    def get_num_motores(self):
        """Devuelve el número de motores de la lancha."""
        return self.__num_motores

    def get_cantidad_combustible(self):
        """Devuelve la cantidad de combustible actual (int)."""
        return self.__nivel_combustible

    @classmethod
    def get_num_lanchas(cls):
        """Devuelve el número total de lanchas creadas."""
        return cls.__num_lanchas

    @classmethod
    def get_num_lanchas_navegando(cls):
        """(Opcional) número de lanchas navegando en este momento."""
        return cls.__num_lanchas_navegando

    # Método set_rumbo

    def set_rumbo(self, nuevo_rumbo):
        # control extra de la subclase
        if nuevo_rumbo is None:
            raise Exception(
                "El rumbo no puede ser nulo, debes indicar el rumbo "
                "(norte, sur, este u oeste) para poder modificarlo."
            )

        if nuevo_rumbo not in ("norte", "sur", "este", "oeste"):
            raise Exception(
                "El rumbo no es correcto, debes indicar el rumbo "
                "(norte, sur, este u oeste) para poder modificarlo."
            )

        # delegamos el resto de comprobaciones (no navegando / mismo rumbo)
        super().set_rumbo(nuevo_rumbo)

    # Método iniciar_navegación

    def iniciar_navegacion(self, velocidad, rumbo, patron, num_tripulantes):
        # Validaciones adicionales de Lancha:

        # combustible dentro de rango permitido
        if (self.__nivel_combustible < Lancha.MIN_COMBUSTIBLE or
            self.__nivel_combustible > Lancha.MAX_COMBUSTIBLE):
            raise Exception(
                f"La lancha {self.get_nombre_barco()} no tiene un nivel de "
                f"combustible válido para iniciar la navegación. El nivel de "
                f"combustible debe estar entre {Lancha.MIN_COMBUSTIBLE} y "
                f"{Lancha.MAX_COMBUSTIBLE}."
            )

        # velocidad de lancha dentro de sus propios límites
        if (velocidad < Lancha.MIN_VELOCIDAD_LANCHA or
            velocidad > Lancha.MAX_VELOCIDAD_LANCHA):
            raise Exception(
                f"La velocidad de navegación de {velocidad} nudos asignada a "
                f"{self.get_nombre_barco()} es incorrecta."
            )

        # resto de validaciones + cambios de estado los hace la superclase
        super().iniciar_navegacion(velocidad, rumbo, patron, num_tripulantes)

        Lancha.__num_lanchas_navegando += 1

    def parar_navegacion(self, tiempo_minutos):
        # Guardamos la velocidad antes de que la superclase la ponga a 0
        velocidad_actual = self._velocidad

        # Validaciones generales + actualización de tiempos y estado
        super().parar_navegacion(tiempo_minutos)

        # Cálculo del combustible consumido:
        # consumo = velocidad * tiempo * FACTOR_COMBUSTIBLE
        combustible_consumido = velocidad_actual * tiempo_minutos * Lancha.FACTOR_COMBUSTIBLE
        combustible_consumido = int(round(combustible_consumido))

        nueva_cantidad = self.__nivel_combustible - combustible_consumido
        if nueva_cantidad < 0:
            nueva_cantidad = 0

        self.__nivel_combustible = nueva_cantidad

        Lancha.__num_lanchas_navegando -= 1

    # Señalizar

    def señalizar(self):
        print(
            f"AVISO de señalización de la lancha {self.get_nombre_barco()} "
            f"con bocinas y luces intermitentes."
        )

    # Método __str__

    def __str__(self):
        base = super().__str__()
        return (
            f"{base}, Número de motores: {self.__num_motores}, "
            f"Nivel de combustible: {self.__nivel_combustible}"
        )
