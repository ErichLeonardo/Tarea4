from embarcacion import Embarcacion
class Velero(Embarcacion):
    #Constantes
    NUM_MASTILES= 1
    NUM_MASTILES_MAX= 4
    NUM_MASTILES_MIN= 1
    VELOCIDAD_MINIMA= 2  # nudos
    VELOCIDAD_MAXIMA= 30 # nudos
    #Atributo de clase
    num_veleros= 0
    #Constructor
    def __init__(self, nombre=None, num_max_tripulantes=None):
        if nombre is None:
            nombre = "Nave sin nombre"
        if num_max_tripulantes is None:
            num_max_tripulantes = 10
        super().__init__(nombre, num_max_tripulantes)
