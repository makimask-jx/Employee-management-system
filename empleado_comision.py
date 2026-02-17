from empleado import Empleado


class EmpleadoComision(Empleado):
    def __init__(
        self,
        nombre: str,
        salario_base: float,
        ventas_realizadas: int,
        comision_por_venta: float,
    ) -> None:
        super().__init__(nombre, salario_base)
        self.ventas_realizadas = ventas_realizadas
        self.comision_por_venta = comision_por_venta

    def calcular_salario_mensual(self) -> float:
        salario_mensual: float = self.salario_base + (
            self.ventas_realizadas * self.comision_por_venta
        )
        return salario_mensual

    def mostrar_informacion(self) -> None:
        print(f"Nombre: {self.nombre}")
        print("Tipo: Comisionista")
        print(f"Ventas realizadas: {self.ventas_realizadas}")
        print(f"Salario base: {self.salario_base}")
        print(f"Salario mensual: {self.calcular_salario_mensual()}")
        print("-------------------")
