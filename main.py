import json
import time

def save_data(tasks, exp, lvl):
    data = {'tasks': tasks, 'exp': exp, 'lvl': lvl}
    with open('todo_data.json', 'w') as file:
        json.dump(data, file, indent=4)

def load_data():
    try:
        with open('todo_data.json', 'r') as file:
            data = json.load(file)
            return data['tasks'], data['exp'], data['lvl']
    except FileNotFoundError:
        return [], 0, 1  # Retorna valores predeterminados si el archivo no existe

# Al iniciar la aplicación, cargamos los datos
tasks, exp, lvl = load_data()


class TaskList:
    def __init__(self):
        self.tasks = []  # Lista para almacenar las tareas
        self.exp = 0  # Experiencia inicial
        self.level = 1  # Nivel inicial

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Tarea '{task}' agregada.")
        save_data(self.tasks, self.exp, self.level)

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks) and not self.tasks[task_index]["completed"]:
            self.tasks[task_index]["completed"] = True
            self.exp += 10  # Añade 10 EXP por tarea completada
            print(f"Tarea '{self.tasks[task_index]['task']}' completada.")
            self.check_level_up()
            save_data(self.tasks, self.exp, self.level)
        else:
            print("Índice de tarea inválido o tarea ya completada.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            deleted_task = self.tasks.pop(task_index)
            print(f"Tarea '{deleted_task['task']}' eliminada.")
            save_data(self.tasks, self.exp, self.level)
        else:
            print("Índice de tarea inválido.")

    def check_level_up(self):
        if self.exp >= 100:
            self.exp -= 100  # Resta 100 EXP y sube de nivel
            self.level += 1
            print(f"Felicidades! Has subido al nivel {self.level}.")

    def show_tasks(self):
        if self.tasks:
            for i, task in enumerate(self.tasks):
                status = "Completada" if task["completed"] else "Pendiente"
                print(f"{i}. {task['task']} - {status}")
        else:
            print("No hay tareas pendientes.")

    def show_status(self):
        print(f"Nivel: {self.level}, EXP: {self.exp}/100")

# Función principal para ejecutar la aplicación
def main():
    task_list = TaskList()
    # Cargamos las tareas, experiencia y nivel guardados
    task_list.tasks = tasks
    task_list.exp = exp
    task_list.level = lvl
    
    while True:
        print("\n--- Lista de Tareas ---")
        task_list.show_tasks()
        task_list.show_status()
        print("1. Agregar tarea\n2. Completar tarea\n3. Eliminar tarea\n4. Salir")
        choice = input("Elige una opción: ")

        if choice == "1":
            task = input("Ingresa la descripción de la tarea: ")
            task_list.add_task(task)
        elif choice == "2":
            task_index = int(input("Ingresa el índice de la tarea a completar: "))
            task_list.complete_task(task_index)
        elif choice == "3":
            task_index = int(input("Ingresa el índice de la tarea a eliminar: "))
            task_list.delete_task(task_index)
        elif choice == "4":
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
