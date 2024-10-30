import sqlite3
from ClsEstudiante import Estudiante
from ClsCalificacion import Calificacion
from ClsMateria import Materia
from ClsProfesor import Profesor

def conectar_db():
    # Conectar a la base de datos 'escuela.db'
    conn = sqlite3.connect('escuela.db')
    return conn

def menu():
    # Muestra el menú de opciones para el usuario
    menuInicio = '''
    -----------------------------------------
    |    Sistema de Gestión Escolar         |
    |     1 - Agregar estudiante            |
    |     2 - Agregar profesor              |
    |     3 - Agregar materia               |
    |     4 - Agregar calificación          |
    |     5 - Mostrar estudiantes           |
    |     6 - Mostrar profesores            |
    |     7 - Mostrar materias              |
    |     8 - Mostrar calificaciones        |
    |     9 - Modificar estudiante          |
    |    10 - Modificar profesor            |
    |    11 - Modificar materia             |
    |    12 - Modificar calificación        |
    |    13 - Borrar materia                |
    |    14 - Borrar calificación           |
    |    15 - Salir                         |
    ----------------------------------------- '''
    print(menuInicio)

def main():
    conn = conectar_db()  # Crear conexión a la base de datos
    cursor = conn.cursor()  # Crear un cursor para interactuar con la base de datos

    while True:
        menu()  # Mostrar el menú de opciones
        opcion = int(input("Ingrese la opción seleccionada: "))  # Leer opción del usuario

        # Opción 1: Agregar estudiante
        if opcion == 1:
            legajo_id = input('Legajo del estudiante: ')
            dni = input('DNI del estudiante: ')
            nombre = input("Nombre del estudiante: ")
            apellido = input('Apellido del estudiante: ')
            edad = input("Edad del estudiante: ")
            fecha_nacimiento = input('Fecha de nacimiento del estudiante: ')
            curso = input('Curso del estudiante: ')
            estado = input('Estado del estudiante: ')
            email = input('Email del estudiante: ')
            # Llama al método agregar para guardar el estudiante
            Estudiante.guardar(conn, legajo_id, dni, nombre, apellido, edad, fecha_nacimiento, curso, estado, email)

        # Opción 2: Agregar profesor
        elif opcion == 2:
            dni_id = input('DNI del profesor: ')
            nombre_profesor = input('Nombre del profesor: ')
            apellido_profesor = input('Apellido del profesor: ')
            curso_profesor = input('Curso del profesor: ')
            estado_profesor = input('Estado del profesor: ')
            email_profesor = input('Email del profesor: ')
            # Llama al método agregar para guardar el profesor
            Profesor.guardar(conn, dni_id, nombre_profesor, apellido_profesor, curso_profesor, estado_profesor, email_profesor)

        # Opción 3: Agregar materia
        elif opcion == 3:
            id_materia = input('ID de la materia: ')
            nombre_materia = input('Nombre de la materia: ')
            curso_materia = input('Curso de la materia: ')
            descripcion = input('Descripción de la materia: ')
            horario = input('Horario de la materia: ')
            # Llama al método agregar para guardar la materia
            Materia.guardar(conn, id_materia, nombre_materia, curso_materia, descripcion, horario)

        # Opción 4: Agregar calificación
        elif opcion == 4:
            legajo_id = input('Legajo del estudiante: ')
            id_materia = input('ID de la materia: ')
            nota = input('Nota: ')
            fecha = input('Fecha: ')
            # Llama al método agregar para guardar la calificación
            Calificacion.guardar(conn, legajo_id, id_materia, nota, fecha)

        # Opción 5: Mostrar estudiantes
        elif opcion == 5:
            Estudiante.mostrar_todos(conn)

        # Opción 6: Mostrar profesores
        elif opcion == 6:
            Profesor.mostrar_todos(conn)

        # Opción 7: Mostrar materias
        elif opcion == 7:
            Materia.mostrar_todas(conn)

        # Opción 8: Mostrar calificaciones
        elif opcion == 8:
            Calificacion.mostrar_todas(conn)

        # Opción 9: Modificar estudiante
        elif opcion == 9:
            legajo_id = input('Ingrese el legajo del estudiante a modificar: ')
            dni = input('Nuevo DNI del estudiante: ')
            nombre = input("Nuevo nombre del estudiante: ")
            apellido = input('Nuevo apellido del estudiante: ')
            edad = input("Nueva edad del estudiante: ")
            fecha_nacimiento = input('Nueva fecha de nacimiento del estudiante: ')
            curso = input('Nuevo curso del estudiante: ')
            estado = input('Nuevo estado del estudiante: ')
            email = input('Nuevo email del estudiante: ')
            # Llama al método modificar para actualizar el estudiante
            Estudiante.modificar(conn, legajo_id, dni, nombre, apellido, edad, fecha_nacimiento, curso, estado, email)

        # Opción 10: Modificar profesor
        elif opcion == 10:
            dni_id = input('Ingrese el DNI del profesor a modificar: ')
            nuevo_nombre_profesor = input('Nuevo nombre del profesor: ')
            nuevo_apellido_profesor = input('Nuevo apellido del profesor: ')
            curso_profesor = input('Nuevo curso del profesor: ')
            estado_profesor = input('Nuevo estado del profesor: ')
            email_profesor = input('Nuevo email del profesor: ')
            # Llama al método modificar para actualizar el profesor
            Profesor.modificar(conn, dni_id, nuevo_nombre_profesor, nuevo_apellido_profesor, curso_profesor, estado_profesor, email_profesor)

        # Opción 11: Modificar materia
        elif opcion == 11:
            id_materia = input('Ingrese el ID de la materia a modificar: ')
            nuevo_nombre_materia = input('Nuevo nombre de la materia: ')
            nuevo_curso_materia = input('Nuevo curso de la materia: ')
            nueva_descripcion = input('Nueva descripción de la materia: ')
            nuevo_horario = input('Nuevo horario de la materia: ')
            # Llama al método modificar para actualizar la materia
            Materia.modificar(conn, id_materia, nuevo_nombre_materia, nuevo_curso_materia, nueva_descripcion, nuevo_horario)

        # Opción 12: Modificar calificación
        elif opcion == 12:
            legajo_id = input('Ingrese el legajo del estudiante de la calificación a modificar: ')
            id_materia = input('Ingrese el ID de la materia: ')
            nueva_nota = input('Nueva nota: ')
            nueva_fecha = input('Nueva fecha: ')
            # Llama al método modificar para actualizar la calificación
            Calificacion.modificar(conn, legajo_id, id_materia, nueva_nota, nueva_fecha)

        # Opción 15: Borrar materia
        elif opcion == 13:
            id_materia = input('Ingrese el ID de la materia a borrar: ')
            # Llama al método borrar para eliminar la materia
            Materia.borrar(conn, id_materia)

        # Opción 16: Borrar calificación
        elif opcion == 14:
            legajo_id = input('Ingrese el legajo del estudiante: ')
            id_materia = input('Ingrese el ID de la materia: ')
            # Llama al método borrar para eliminar la calificación
            Calificacion.borrar(conn, legajo_id, id_materia)

        # Opción 17: Salir del sistema
        elif opcion == 15:
            print('Saliendo del sistema...')
            break  # Termina el bucle y cierra el programa

        else:
            print('Opción no válida, intente nuevamente.')  # Mensaje de error si la opción no es válida

    conn.close()  # Cierra la conexión a la base de datos al final

# Punto de entrada del programa, ejecuta la función principal
if __name__ == "__main__":
    main()