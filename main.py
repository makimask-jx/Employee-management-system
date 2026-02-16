from empleado_comision import EmpleadoComision
from empleado_por_horas import EmpleadoPorHoras
from empleado_tiempo_completo import EmpleadoTiempoCompleto


def simulacion_empresa() -> None:
    empleado_1 = EmpleadoComision("Ashley", float(49000), 723, 20)
    empleado_2 = EmpleadoPorHoras("Elizabeth", float(40000), 10, 3333)
    empleado_3 = EmpleadoTiempoCompleto("Lesley", float(600000))

    """
    Podriamos crear una lista con empleados y usar un bucle para mostrar la información de cada uno,
    pero por simplicidad lo dejaremos con prints de forma manual
    """

    print(f"Información de: {empleado_1.nombre}:\n {empleado_1.mostrar_informacion}")
    print(f"Información de: {empleado_2.nombre}:\n {empleado_2.mostrar_informacion}")
    print(f"Información de: {empleado_3.nombre}:\n {empleado_3.mostrar_informacion}")


if __name__ == "__main__":
    simulacion_empresa()
