# tipos_vehiculo.py
from Vehiculo import Vehiculo

class Automovil(Vehiculo): # Heredamos de vehículo, ahora podemos usar sus atributos
    def __init__(self, marca, modelo, anio, numero_serie, numero_puertas):
        super().__init__(marca, modelo, anio, numero_serie)
        self.numero_puertas = numero_puertas

    def mostrar_informacion(self):
        print(f"Automóvil: {self.marca} {self.modelo} ({self.anio})")
        print(f"Número de puertas: {self.numero_puertas}")
        print(f"Número de serie: {self.get_numero_serie()}")
        print("-" * 40)


class Camion(Vehiculo):
    def __init__(self, marca, modelo, anio, numero_serie, capacidad_carga):
        super().__init__(marca, modelo, anio, numero_serie)
        self.capacidad_carga = capacidad_carga

    def mostrar_informacion(self):
        print(f"Camión: {self.marca} {self.modelo} ({self.anio})")
        print(f"Capacidad de carga: {self.capacidad_carga} toneladas")
        print(f"Número de serie: {self.get_numero_serie()}")
        print("-" * 40)


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, numero_serie, electrica):
        super().__init__(marca, modelo, anio, numero_serie)
        self.electrica = electrica

    def mostrar_informacion(self):
        tipo = "Eléctrica" if self.electrica else "Gasolina"
        print(f"Motocicleta: {self.marca} {self.modelo} ({self.anio})")
        print(f"Tipo: {tipo}")
        print(f"Número de serie: {self.get_numero_serie()}")
        print("-" * 40)


# Ejemplo de uso con polimorfismo
if __name__ == "__main__":
    vehiculos = [
        Automovil("Toyota", "Corolla", 2020, "A12345", 4),
        Camion("Volvo", "FH16", 2018, "C67890", 18),
        Motocicleta("Yamaha", "MT-07", 2021, "M11223", False),
        Motocicleta("Zero", "SR/F", 2022, "M44556", True)
    ]

    for v in vehiculos:
        v.mostrar_informacion()
    
