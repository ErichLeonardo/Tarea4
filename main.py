from embarcacion import Embarcacion
from lancha import Lancha
from velero import Velero


class Main:
    @staticmethod
    def main():

        # ===========================================================
        # 1. COMPROBACIÓN DE CONSTRUCTORES Y ATRIBUTOS
        # ===========================================================
    

        vel1 = Velero()
        vel2 = Velero("Náutico", 6, 2)

        lan1 = Lancha()
        lan2 = Lancha("TurboJet", 4, 2, 40)

        print("Velero generado sin parámetros:", vel1)
        print("Velero generado con parámetros:", vel2)
        print("Lancha generada sin parámetros:", lan1)
        print("Lancha generada con parámetros:", lan2)

        # ===========================================================
        # 2. GETTERS Y MÉTODOS DE CLASE
        # ===========================================================
    

        print("Mástiles vel1:", vel1.get_num_mastiles())
        print("Total veleros:", vel1.get_num_veleros())

        print("Motores lan2:", lan2.get_num_motores())
        print("Combustible lan2:", lan2.get_cantidad_combustible())
        print("Total lanchas creadas:", Lancha.get_num_lanchas())

        # ===========================================================
        # 3. INICIO Y PARADA DE LA NAVEGACIÓN
        # ===========================================================


        print("\nIniciando navegación vel2...")
        vel2.iniciar_navegacion(10, "ceñida", "Patrón A", 3)
        print("Velero en navegación:", vel2)

        print("\nIniciando navegación lan2...")
        lan2.iniciar_navegacion(20, "norte", "Patrón B", 2)
        print("Lancha en navegación:", lan2)

        print("\nParando navegación lan2 (30 minutos)...")
        lan2.parar_navegacion(30)
        print("Lancha tras parar:", lan2)

        # ===========================================================
        # 4. CAMBIO DE RUMBO
        # ===========================================================
    

        print("\nCambiando rumbo vel2 a empopada...")
        vel2.set_rumbo("empopada")
        print("Nuevo rumbo vel2:", vel2.get_rumbo())

        print("\nCambiando rumbo lan1 (no navegando) debe FALLAR...")
        try:
            lan1.set_rumbo("sur")
        except Exception as e:
            print("Excepción esperada:", e)

        # ===========================================================
        # 5. REGATAS Y SEÑALIZACIÓN
        # ===========================================================


        
        vA = Velero("Regata A", 4, 2)
        vB = Velero("Regata B", 4, 2)

        vA.iniciar_navegacion(15, "ceñida", "X", 3)
        vB.iniciar_navegacion(12, "ceñida", "Y", 3)

        print("Velero A:", vA)
        print("Velero B:", vB)

        print("\nRegata:")
        print(vA.iniciar_regata(vB))

        print("\nSeñalización velero:")
        vA.señalizar()

        print("\nSeñalización lancha:")
        lan1.señalizar()

        # ===========================================================
        # 6. MÉTODOS __str__
        # ===========================================================
        

        print("vel1:", vel1)
        print("vel2:", vel2)
        print("lan1:", lan1)
        print("lan2:", lan2)


if __name__ == "__main__":
    Main.main()        