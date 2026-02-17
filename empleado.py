from abc import abstractmethod, ABCMeta


class Empleado(metaclass=ABCMeta):
    def __init__(self, nombre: str, salario_base: float) -> None:
        self.nombre = nombre
        self.salario_base = salario_base

    # En este caso, no podemos usar try except para comprobar que los valores sean de dicha categoria. Asi que tenemos que usar propiedades
    # Es bastante parecido a los getters setters de Java en mi opinion
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not isinstance(value, str):
            # Para parar la ejecucion del programa, hay que utilizar un raise, no un break o print
            raise ValueError("El nombre debe ser un conjunto de caracteres")
        self._nombre = value

    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("El salario tiene que ser un número entero o decimal")
        if value <= 0:
            raise ValueError("El salario base debe ser mayor a cero")
        self._salario_base = value

    @abstractmethod
    def calcular_salario_mensual(self) -> float:
        pass

    @abstractmethod
    def mostrar_informacion(self) -> None:
        pass
