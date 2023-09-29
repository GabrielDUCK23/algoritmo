import random

class Antigeno:
    def __init__(self, nombre, fortaleza):
        """
        Inicializa un antígeno con un nombre y una fortaleza.

        Args:
            nombre (str): El nombre del antígeno.
            fortaleza (float): La fortaleza del antígeno, un valor entre 0 y 1.
        """
        self.nombre = nombre
        self.fortaleza = fortaleza

class Anticuerpo:
    def __init__(self, nombre, especificidad):
        """
        Inicializa un anticuerpo con un nombre y una especificidad.

        Args:
            nombre (str): El nombre del anticuerpo.
            especificidad (str): La especificidad del anticuerpo para atacar ciertos antígenos.
        """
        self.nombre = nombre
        self.especificidad = especificidad

class SistemaInmunologico:
    def __init__(self):
        """
        Inicializa un sistema inmunológico con una lista vacía de anticuerpos.
        """
        self.anticuerpos = []

    def agregar_anticuerpo(self, anticuerpo):
        """
        Agrega un anticuerpo al sistema inmunológico.

        Args:
            anticuerpo (Anticuerpo): El anticuerpo que se va a agregar al sistema.
        """
        self.anticuerpos.append(anticuerpo)

    def atacar(self, antigeno):
        """
        Intenta que los anticuerpos del sistema inmunológico ataquen un antígeno dado.

        Args:
            antigeno (Antigeno): El antígeno que se va a atacar.
        """
        for anticuerpo in self.anticuerpos:
            if anticuerpo.especificidad == antigeno.nombre:
                if random.random() > 0.5:
                    print(f"El anticuerpo {anticuerpo.nombre} neutralizó con éxito el antígeno {antigeno.nombre}.")
                    return
                else:
                    print(f"El anticuerpo {anticuerpo.nombre} no pudo neutralizar el antígeno {antigeno.nombre}.")

def main():
    # Crear un sistema inmunológico
    sistema_inmunologico = SistemaInmunologico()

    # Agregar anticuerpos al sistema inmunológico
    anticuerpo1 = Anticuerpo("Ab1", "VirusA")
    anticuerpo2 = Anticuerpo("Ab2", "BacteriaB")
    sistema_inmunologico.agregar_anticuerpo(anticuerpo1)
    sistema_inmunologico.agregar_anticuerpo(anticuerpo2)

    # Introducir antígenos al sistema
    antigeno1 = Antigeno("VirusA", 0.7)
    antigeno2 = Antigeno("BacteriaB", 0.6)

    # Simular ataques del sistema inmunológico
    sistema_inmunologico.atacar(antigeno1)
    sistema_inmunologico.atacar(antigeno2)

if __name__ == "__main__":
    main()
