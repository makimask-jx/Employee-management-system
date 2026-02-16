from empleado import Empleado


class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre: str, salario_base: float) -> None:
        super().__init__(nombre, salario_base)

    def calcular_salario_mensual(self) -> float:
        return self.salario_base / 12

    def mostrar_informacion(self) -> None:
        print(
            f"Nombre: {self.nombre}, salario mensual: {self.calcular_salario_mensual()}"
        )
