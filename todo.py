#!/usr/bin/env python3
import json
import os
import sys

TASKS_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def list_tasks(tasks):
    if not tasks:
        print("No hay tareas.")
        return
    print("\n--- Lista de Tareas ---")
    for i, task in enumerate(tasks, 1):
        status = "✓ completada" if task["done"] else "○ pendiente"
        print(f"  {i}. [{status}] {task['title']}")
    print()


def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Tarea agregada: '{title}'")


def complete_task(tasks, number):
    if not 1 <= number <= len(tasks):
        print("Número de tarea inválido.")
        return
    tasks[number - 1]["done"] = True
    save_tasks(tasks)
    print(f"Tarea {number} marcada como completada.")


def delete_task(tasks, number):
    if not 1 <= number <= len(tasks):
        print("Número de tarea inválido.")
        return
    removed = tasks.pop(number - 1)
    save_tasks(tasks)
    print(f"Tarea eliminada: '{removed['title']}'")


def print_help():
    print("""
Uso: python todo.py <comando> [argumentos]

Comandos:
  list                  Ver todas las tareas
  add <título>          Agregar una nueva tarea
  done <número>         Marcar tarea como completada
  delete <número>       Eliminar una tarea
  help                  Mostrar esta ayuda
""")


def main():
    if len(sys.argv) < 2:
        print_help()
        return

    tasks = load_tasks()
    command = sys.argv[1].lower()

    if command == "list":
        list_tasks(tasks)

    elif command == "add":
        if len(sys.argv) < 3:
            print("Uso: python todo.py add <título>")
            return
        title = " ".join(sys.argv[2:])
        add_task(tasks, title)

    elif command == "done":
        if len(sys.argv) < 3:
            print("Uso: python todo.py done <número>")
            return
        try:
            number = int(sys.argv[2])
        except ValueError:
            print("El número de tarea debe ser un entero.")
            return
        complete_task(tasks, number)

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Uso: python todo.py delete <número>")
            return
        try:
            number = int(sys.argv[2])
        except ValueError:
            print("El número de tarea debe ser un entero.")
            return
        delete_task(tasks, number)

    elif command == "help":
        print_help()

    else:
        print(f"Comando desconocido: '{command}'")
        print_help()


if __name__ == "__main__":
    main()
