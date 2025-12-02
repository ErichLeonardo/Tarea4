class Embarcacion:

    # atributos de clase
    __numero_barcos = 0
    __numero_barcos_navegando = 0
    __tiempo_total_navegacion_acumulado = 0  # en minutos

    # constantes publicas
    MIN_MASTILES = 1
    MAX_MASTILES = 4
    MIN_VELOCIDAD = 2   # en nudos
    MAX_VELOCIDAD = 30  # en nudos
    PATRON_POR_DEFECTO = "Sin patrón"
    RUMBO_POR_DEFECTO = "Sin rumbo"
    MIN_TRIPULANTES = 0  # excluye al patrón

    # constructor sin parametros / con parametros
    def __init__(self, nombre=None, numero_mastiles=None, num_max_tripulantes=None):

        # constructor sin parametros (no lanza excepciones)
        if nombre is None and numero_mastiles is None and num_max_tripulantes is None:
            Embarcacion.__numero_barcos += 1
            self.__nombre = f"Embarcacion {Embarcacion.__numero_barcos}"
            self.__numero_mastiles = Embarcacion.MIN_MASTILES
            self.__num_max_tripulantes = Embarcacion.MIN_TRIPULANTES

        # constructor con parametros (valida y puede lanzar excepciones)
        else:
            # validar nombre
            if not isinstance(nombre, str):
                raise Exception("El nombre de la embarcación es obligatorio.")
            if nombre.strip() == "":
                raise Exception("El nombre de la embarcación no puede estar vacío.")

            # controlar que sea entero el numero de mastiles y tripulantes max
            if not isinstance(numero_mastiles, int):
                raise Exception("El número de mástiles debe ser un entero")
            if not isinstance(num_max_tripulantes, int):
                raise Exception("El número de mástiles debe ser un entero")

            # validar rangos
            if numero_mastiles < Embarcacion.MIN_MASTILES or numero_mastiles > Embarcacion.MAX_MASTILES:
                raise Exception(f"El número de mástiles debe estar entre {Embarcacion.MIN_MASTILES} y {Embarcacion.MAX_MASTILES}")
            if num_max_tripulantes < Embarcacion.MIN_TRIPULANTES:
                raise Exception(f"El número máximo de tripulantes debe ser, como mínimo, {Embarcacion.MIN_TRIPULANTES}.")

            Embarcacion.__numero_barcos += 1
            self.__nombre = nombre
            self.__numero_mastiles = numero_mastiles
            self.__num_max_tripulantes = num_max_tripulantes


    # atributos estado objeto en cada instante
        self.__esta_navegando = False
        self.__tiempo_total_navegacion = 0 

    # atributos de navegación
        self.__velocidad = 0
        self.__nombre_patron = Embarcacion.PATRON_POR_DEFECTO
        self.__rumbo = Embarcacion.RUMBO_POR_DEFECTO
        self.__numero_tripulantes = 0  

    # getters
    def get_nombre_barco(self):
        return self.__nombre

    def get_num_mastiles(self):
        return self.__numero_mastiles

    def get_max_tripulantes(self):
        return self.__num_max_tripulantes

    def is_navegando(self):
        return self.__esta_navegando

    def get_tiempo_total_navegacion_barco(self):
        return self.__tiempo_total_navegacion  # minutos

    def get_velocidad(self):
        return self.__velocidad

    def get_rumbo(self):
        return self.__rumbo

    def get_patron(self):
        return self.__nombre_patron

    def get_tripulacion(self):
        return self.__numero_tripulantes

    # Metodos que devuelven información genérica
    @classmethod
    def get_num_barcos(cls):
        return cls.__numero_barcos

    @classmethod
    def get_num_barcos_navegando(cls):
        return cls.__numero_barcos_navegando

    @classmethod
    def get_tiempo_total_navegacion(cls):
        return cls.__tiempo_total_navegacion_acumulado  # minutos
    
    # setters
    def set_rumbo(self, nuevo_rumbo):
        if not self.__esta_navegando:
            raise Exception(f"La embarcación {self.__nombre} no está navegando, no se puede cambiar el rumbo.")
        if not isinstance(nuevo_rumbo, str) or nuevo_rumbo.strip() == "" or nuevo_rumbo not in ("ceñida", "empopada"):
            raise Exception("El rumbo no es correcto, debes indicar el rumbo (ceñida o empopada) para poder modificarlo.")
        if nuevo_rumbo == self.__rumbo:
            raise Exception(f"La embarcación {self.__nombre} ya está navegando con ese rumbo ({self.__rumbo}), debes indicar un rumbo distinto para poder modificarlo.")
        self.__rumbo = nuevo_rumbo
    
     # iniciar navegacion
    def iniciar_navegacion(self, velocidad, rumbo, patron, num_tripulantes):
        # validar estado
        if self.__esta_navegando:
            raise Exception(f"La embarcacion {self.__nombre} ya está navegando y se encuentra fuera de puerto.")

        # validar parametros
        if not isinstance(velocidad, (int, float)) or velocidad < Embarcacion.MIN_VELOCIDAD or velocidad > Embarcacion.MAX_VELOCIDAD:
            raise Exception(f"La velocidad de navegación de {velocidad} nudos es incorrecta.")
        if not isinstance(rumbo, str) or rumbo.strip() == "":
            raise Exception("El rumbo no puede estar vacío, debes indicar el rumbo para iniciar la navegación.")
        if not isinstance(patron, str) or patron.strip() == "":
            raise Exception("El patrón del barco no puede estar vacío, se necesita un patrón para iniciar la navegación.")
        if not isinstance(num_tripulantes, int) or num_tripulantes < Embarcacion.MIN_TRIPULANTES or num_tripulantes > self.__num_max_tripulantes:
            raise Exception(f"El número de tripulantes debe estar entre {Embarcacion.MIN_TRIPULANTES} y {self.__num_max_tripulantes}.")

        # asignar estado de navegacion
        self.__velocidad = int(velocidad)
        self.__rumbo = rumbo
        self.__nombre_patron = patron
        self.__numero_tripulantes = num_tripulantes
        self.__esta_navegando = True

        Embarcacion.__numero_barcos_navegando += 1

    # parar navegacion
    def parar_navegacion(self, tiempo_minutos):
        if not self.__esta_navegando:
            raise Exception(f"La embarcacion {self.__nombre} no está navegando.")
        if not isinstance(tiempo_minutos, (int, float)) or tiempo_minutos < 1:
            raise Exception("Tiempo navegando incorrecto, debe ser mayor que cero.")

        # acumular tiempo
        tiempo_minutos = int(tiempo_minutos)
        self.__tiempo_total_navegacion += tiempo_minutos
        Embarcacion.__tiempo_total_navegacion_acumulado += tiempo_minutos

        # reset de navegacion
        self.__esta_navegando = False
        self.__velocidad = 0
        self.__rumbo = Embarcacion.RUMBO_POR_DEFECTO
        self.__nombre_patron = Embarcacion.PATRON_POR_DEFECTO
        self.__numero_tripulantes = 0

        Embarcacion.__numero_barcos_navegando -= 1


    def señalizar():
        pass

    # representacion del objeto
    def __str__(self):
        navegando_txt = "Sí" if self.__esta_navegando else "No"
        partes = [
            f"Nombre del barco: {self.__nombre}",
            f"Número de mástiles: {self.__numero_mastiles}",
            f"Tripulación: {self.__numero_tripulantes}",
            f"Navegando: {navegando_txt}"
        ]
        if self.__esta_navegando:
            partes.append(f"con el patrón {self.__nombre_patron} en {self.__rumbo} a {self.__velocidad} nudos")
        horas = self.__tiempo_total_navegacion / 60.0
        partes.append(f"Tiempo total de navegación del barco: {horas:.2f} horas")
        if self.__esta_navegando:
            return f"{', '.join(partes[:-1])}, {partes[-1]}"
        else:
            return f"{', '.join(partes)}"
    