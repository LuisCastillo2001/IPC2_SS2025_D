# vehiculo.py
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo, anio, numero_serie):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.__numero_serie = numero_serie  

    # Getter del número de serie
    def get_numero_serie(self):
        return self.__numero_serie

    # Setter del número de serie
    def set_numero_serie(self, nuevo_numero):
        self.__numero_serie = nuevo_numero

    # Método abstracto
    @abstractmethod
    def mostrar_informacion(self):
        pass
