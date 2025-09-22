class TareasView:
    def menu(self):
        print("\n1. Agregar tarea\n2. Ver tareas\n3. Completar tarea\n4. Eliminar tarea\n5. Salir")
        return input("Opción: ")

    def pedir_texto(self):
        return input("Descripción de la tarea: ")

    def pedir_indice(self):
        return int(input("Número de tarea: ")) - 1

    def mostrar_tareas(self, tareas):
        if not tareas:
            print("📭 No hay tareas.")
        for i, tarea in enumerate(tareas, 1):
            estado = "✅" if tarea.completada else "⌛"
            print(f"{i}. {tarea.descripcion} [{estado}]")

    def mostrar_mensaje(self, msg):
        print(msg)
