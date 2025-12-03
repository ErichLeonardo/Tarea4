from embarcacion import Embarcacion
class Velero(Embarcacion):
    #Constantes
    NUM_MASTILES= 1
    NUM_MASTILES_MAX= 4
    NUM_MASTILES_MIN= 1
    VELOCIDAD_MINIMA= 2  # nudos
    VELOCIDAD_MAXIMA= 30 # nudos
    #Atributo de clase (solo Velero)
    __num_veleros= 0
    #Constructor
    def __init__(self, nombre=None, num_max_tripulantes=None, num_mastiles=NUM_MASTILES):
        # Constructor sin parámetros
        if nombre is None and num_mastiles is None and num_max_tripulantes is None:
            Velero.__num_veleros += 1
            nombre = f"Velero {Velero.__num_veleros} +1"
            num_mastiles = Velero.NUM_MASTILES_MIN
            num_max_tripulantes = Embarcacion.MIN_TRIPULANTES

        # Constructor CON parámetros
        else:
            if num_mastiles < Velero.NUM_MASTILES_MIN or num_mastiles > Velero.NUM_MASTILES_MAX:
                raise ValueError(f"El número de mástiles debe estar entre {Velero.NUM_MASTILES_MIN} y {Velero.NUM_MASTILES_MAX}.")
            Velero.__num_veleros += 1

        # Llamada al constructor base
        super().__init__(nombre, num_max_tripulantes)

        # Atributos del velero
        self.__num_mastiles = num_mastiles

    #--- Getters de objeto ---
    def get_num_veleros(self):
        return self.__num_veleros
    
    def get_num_mastiles(self):
        return self.__num_mastiles
    
    # ---Setters---

    #Metodos de la superclase
    def set_rumbo(self, nuevo_rumbo):
        # 1. Validación adicional: parámetro nulo
        if nuevo_rumbo is None:
            raise Exception(
                "El rumbo no puede ser nulo, debes indicar el rumbo (ceñida o empopada) para poder modificarlo."
            )

        # 2. Validación adicional: rumbo no válido
        if nuevo_rumbo not in ("ceñida", "empopada"):
            raise Exception(
                "El rumbo no es correcto, debes indicar el rumbo (ceñida o empopada) para poder modificarlo."
            )

        # 3. Llamamos al método original de la superclase
        super().set_rumbo(nuevo_rumbo)
    
    def iniciar_navegacion(self, velocidad, rumbo, patron, num_tripulantes):

        # --- VALIDACIÓN EXTRA DE VELERO ---
        if velocidad < self.VELOCIDAD_MIN or velocidad > self.VELOCIDAD_MAX:
            raise Exception(f"La velocidad de navegación de {velocidad} nudos es incorrecta.")

        # --- VALIDACIÓN EXTRA DEL RUMBO ---
        if rumbo is None:
            raise Exception("El rumbo no puede ser nulo, debes indicar el rumbo (ceñida o empopada).")

        if rumbo not in ("ceñida", "empopada"):
            raise Exception("El rumbo no es correcto, debes indicar el rumbo (ceñida o empopada).")

        # Llamar al método original de Embarcacion (validaciones generales)
        super().iniciar_navegacion(velocidad, rumbo, patron, num_tripulantes)

 
    def iniciar_regata(self, otro_velero):

        # 1. Validar parámetro
        if otro_velero is None:
            raise Exception("El barco con el que se intenta regatear no existe")

        # 2. Ambos barcos deben estar navegando
        if not self.is_navegando():
            raise Exception(f"No se puede iniciar la regata, el barco {self.get_nombre_barco()} no está navegando.")

        if not otro_velero.is_navegando():
            raise Exception(f"No se puede iniciar la regata, el barco {otro_velero.get_nombre_barco()} no está navegando.")

        # 3. Deben llevar el mismo rumbo
        if self.get_rumbo() != otro_velero.get_rumbo():
            raise Exception(
                f"No se puede iniciar la regata, los barcos "
                f"{self.get_nombre_barco()} y {otro_velero.get_nombre_barco()} "
                "deben navegar con el mismo rumbo."
            )

        # 4. Deben tener el mismo número de mástiles
        if self.num_mastiles != otro_velero.num_mastiles:
            raise Exception(
                f"No se puede iniciar la regata, los barcos "
                f"{self.get_nombre_barco()} y {otro_velero.get_nombre_barco()} "
                "no tienen el mismo numero de mástiles."
            )

        # 5. Se puede realizar la regata → determina el ganador
        if self.get_velocidad() > otro_velero.get_velocidad():
            return f"El barco {self.get_nombre_barco()} ha llegado antes a la línea de llegada."

        elif self.get_velocidad() < otro_velero.get_velocidad():
            return f"El barco {otro_velero.get_nombre_barco()} ha llegado antes a la línea de llegada."

        else:
            return (
                f"Los barcos {self.get_nombre_barco()} y {otro_velero.get_nombre_barco()} "
                "han llegado a la vez a la línea de llegada."
            )

        def señalizar(self):
            print(f"AVISO del velero {self.get_nombre_barco()} con banderas de señalización marítima.")

        def __str__(self):
            # Obtener la cadena base que genera la clase Embarcacion
            base = super().__str__()

            # Añadir la información específica del velero
            return f"{base}, Número de mástiles: {self.num_mastiles}"