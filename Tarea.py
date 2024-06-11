class Tarea:
    def __init__(self, nombre, descripcion, fecha_vencimiento=None, prioridad=1):
        if not nombre or not descripcion:
            raise ValueError("El nombre y la descripción no pueden estar vacíos")
        if not isinstance(prioridad, int) or prioridad < 1 or prioridad > 5:
            raise ValueError("La prioridad debe ser un entero entre 1 y 5")

        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.prioridad = prioridad
        self.completada = False

    def marcar_completada(self):
        self.completada = True
