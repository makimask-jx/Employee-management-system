from empleado import Empleado


class EmpleadoPorHoras(Empleado):
    def __init__(
        self,
        nombre: str,
        salario_base: float,
        horas_trabajadas: float,
        tarifa_por_hora: float,
    ) -> None:
        super().__init__(nombre, salario_base)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario_mensual(self) -> float:
        return self.horas_trabajadas * self.tarifa_por_hora

    def mostrar_informacion(self) -> None:
        print(f"Nombre: {self.nombre}")
        print("Tipo: Por Horas")
        print(f"Horas trabajadas: {self.horas_trabajadas}")
        print(f"Tarifa por hora: {self.tarifa_por_hora}")
        print(f"Salario mensual: {self.calcular_salario_mensual()}")
