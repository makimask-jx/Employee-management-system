from abc import ABC, abstractmethod


class Empleado(ABC):
    def __init__(self, nombre: str, salario_base: float) -> None:
        self.nombre = nombre
        self.salario_base = salario_base

    @abstractmethod
    def calcular_salario_mensual(self) -> float:
        pass

    @abstractmethod
    def mostrar_informacion(self) -> None:
        pass
