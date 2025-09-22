class Tarea:
    def __init__(self, descripcion: str):
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True


class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar(self, descripcion):
        self.tareas.append(Tarea(descripcion))

    def listar(self):
        return self.tareas

    def eliminar(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas.pop(indice)
        else:
            raise IndexError("Tarea no encontrada")

    def completar(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].marcar_completada()
        else:
            raise IndexError("Tarea no encontrada")
