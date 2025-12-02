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
       
