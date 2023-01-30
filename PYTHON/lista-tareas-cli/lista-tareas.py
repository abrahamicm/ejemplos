import json
import argparse
import curses

def agregar_tarea(tarea):
    # código para agregar una tarea al archivo JSON

def ver_tareas():
    # código para mostrar las tareas en la terminal de comandos

def eliminar_tarea(tarea):
    # código para eliminar una tarea del archivo JSON

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--agregar", help="Agregar una tarea")
    parser.add_argument("-v", "--ver", help="Ver las tareas existentes", action="store_true")
    parser.add_argument("-e", "--eliminar", help="Eliminar una tarea")
    args = parser.parse_args()

    if args.agregar:
        agregar_tarea(args.agregar)
    elif args.ver:
        ver_tareas()
    elif args.eliminar:
        eliminar_tarea(args.eliminar)
    else:
        print("No se ha seleccionado ninguna acción. Utilice -h para obtener ayuda.")

if __name__ == "__main__":
    main()
