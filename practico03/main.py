import sqlite3
from ClsEstudiante import Estudiante
from ClsCalificacion import Calificacion
from ClsMateria import Materia
from ClsProfesor import Profesor

def conectar_db():
    conn = sqlite3.connect('escuela.db')
    return conn

def main():
    conn = conectar_db()
    conn = conn.cursor()

def menu():
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
    |     9 - Salir                         |
    ----------------------------------------- '''
    print(menuInicio)

while True:
    opcion = int(input("Ingrese la opción seleccionada: "))
    if opcion == '1':
        legajo_id = input('Legajo del estudiante: ')
        dni = input('DNI del estudiante: ')
        nombre = input("Nombre del estudiante: ")
        apellido = input('Apellido del estudiante: ')
        edad = input("Edad del estudiante: ")
        fecha_nacimiento = input('Fecha de nacimiento del estudiante. ')
        curso = input('Curso del estudiante: ')
        estado = input('Estado del estudiante: ')
        email = input('Email del estudiante: ')
        Estudiante.agregar (conn, legajo_id, dni, nombre, apellido, edad, fecha_nacimiento, curso, estado, email)

    elif opcion == '2':
        dni_id = input('DNI del profesor: ')
        nombre_profesor = input('Nombre del profesor: ')
        apellido_profesor = input('Apellido del profesor: ')
        curso_profesor = input('Curso del profesor: ')
        estado_profesor = input('Estado del profesor: ')
        email_profesor = input('Email del profesor: ')
