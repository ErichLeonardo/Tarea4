from embarcacion import Embarcacion

class Lancha(Embarcacion):
    # ---------- ATRIBUTOS DE CLASE ----------
    __num_lanchas = 0          # número de lanchas creadas

    # ---------- CONSTANTES PÚBLICAS ----------
    MIN_MOTORES = 1
    MAX_MOTORES = 2

    MIN_COMBUSTIBLE = 8        # litros
    MAX_COMBUSTIBLE = 50       # litros

    FACTOR_COMBUSTIBLE = 0.026

    MIN_VELOCIDAD_LANCHA = 1   # nudos
    MAX_VELOCIDAD_LANCHA = 50  # nudos

    # ---------- CONSTRUCTOR (0 ó 4 PARÁMETROS) ----------
    def __init__(self, nombre=None, num_max_tripulantes=None,
                 num_motores=None, nivel_combustible=None):
        """
        Si se llama como Lancha():
            - nombre = 'Lancha X' (X = número de lanchas creadas + 1)
            - num_max_tripulantes = MIN_TRIPULANTES de Embarcacion
            - num_motores = MIN_MOTORES
            - nivel_combustible = MAX_COMBUSTIBLE
            - NO lanza excepciones

        Si se llama como Lancha(nombre, num_max_tripulantes,
                                num_motores, nivel_combustible):
            - valida num_motores y nivel_combustible
            - si son incorrectos, lanza las excepciones pedidas
        """

        # --- CONSTRUCTOR SIN PARÁMETROS ---
        if (nombre is None and num_max_tripulantes is None and
            num_motores is None and nivel_combustible is None):

            # incrementamos el contador de lanchas para generar el nombre
            Lancha.__num_lanchas += 1
            nombre_auto = f"Lancha {Lancha.__num_lanchas}"

            # llamamos al constructor de Embarcacion con valores seguros
            super().__init__(nombre_auto, Embarcacion.MIN_TRIPULANTES)

            # atributos propios "constantes" de la lancha
            self.__num_motores = Lancha.MIN_MOTORES
            self.__nivel_combustible = Lancha.MAX_COMBUSTIBLE

        # Constructor con parámetros 
        else:
            # primero llamamos al constructor de Embarcacion
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
            self.__num_motores = num_motores
            self.__nivel_combustible = float(nivel_combustible)

            # actualizamos contador de lanchas
            Lancha.__num_lanchas += 1

    # Getters 
    def get_num_motores(self): return self.__num_motores  

    def get_nivel_combustible(self): return self.__nivel_combustible

    def get_num_lanchas(self): return Lancha.__num_lanchas

    def set_rumbo(self, nuevo_rumbo):
        return super().set_rumbo(nuevo_rumbo)
    
    

