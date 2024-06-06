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

class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def editar_tarea(self, indice, nueva_descripcion):
        self.tareas[indice].descripcion = nueva_descripcion

    def marcar_completada(self, indice):
        self.tareas[indice].marcar_completada()

    def eliminar_tarea(self, indice):
        del self.tareas[indice]

    def mostrar_tareas_pendientes(self):
        for i, tarea in enumerate(self.tareas):
            if not tarea.completada:
                print(f"{i + 1}. {tarea.nombre}")

    def filtrar_por_prioridad(self, prioridad):
        for tarea in self.tareas:
            if tarea.prioridad == prioridad:
                print(f"{tarea.nombre}: {tarea.descripcion}")

if __name__ == "__main__":
    lista_tareas = ListaTareas()

    # Crear algunas tareas
    try:
        tarea1 = Tarea("Hacer ejercicio", "Correr durante 30 minutos")
        tarea2 = Tarea("", "Ir al supermercado")  # Esto debe generar una excepción
        tarea3 = Tarea("Estudiar para el examen", "Repasar los apuntes", prioridad=6)  # Esto también

        lista_tareas.agregar_tarea(tarea1)
        lista_tareas.agregar_tarea(tarea2)
        lista_tareas.agregar_tarea(tarea3)
    except ValueError as e:
        print(f"Error al crear tarea: {e}")

    # Mostrar tareas pendientes
    print("Tareas pendientes:")
    lista_tareas.mostrar_tareas_pendientes()
