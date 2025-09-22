from model.tareas_model import GestorTareas
from view.tareas_view import TareasView

class TareasController:
    def __init__(self):
        self.model = GestorTareas()
        self.view = TareasView()

    def ejecutar(self):
        while True:
            opcion = self.view.menu()
            if opcion == "1":
                descripcion = self.view.pedir_texto()
                self.model.agregar(descripcion)
                self.view.mostrar_mensaje("📝 Tarea agregada.")
            elif opcion == "2":
                self.view.mostrar_tareas(self.model.listar())
            elif opcion == "3":
                try:
                    idx = self.view.pedir_indice()
                    self.model.completar(idx)
                    self.view.mostrar_mensaje("✅ Tarea completada.")
                except Exception as e:
                    self.view.mostrar_mensaje(str(e))
            elif opcion == "4":
                try:
                    idx = self.view.pedir_indice()
                    self.model.eliminar(idx)
                    self.view.mostrar_mensaje("🗑️ Tarea eliminada.")
                except Exception as e:
                    self.view.mostrar_mensaje(str(e))
            elif opcion == "5":
                self.view.mostrar_mensaje("👋 Saliendo del gestor de tareas.")
                break
            else:
                self.view.mostrar_mensaje("❌ Opción inválida.")
