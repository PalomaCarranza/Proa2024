import sqlite3 #Nesecesario para trabajar con la base de datos SQLite

class Estudiante:
    # Método constructor que inicializa las propiedades del objeto Estudiante.
    def __init__(self, legajo_id, dni, nombre, apellido, edad, fecha_nacimiento, curso, estado, email):
        self.legajo_id = legajo_id
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.curso = curso
        self.estado = estado
        self.email = email

    # Método para guardar la información del estudiante en la base de datos.
    def guardar(self):
        # Conectar a la base de datos 'escolar.db'.
        conn = sqlite3.connect('escolar.db.sql')
        c = conn.cursor() # Crear un cursor para interactuar con la base de datos.

        # Ejecutar una consulta SQL para insertar los datos del estudiate. 
        c.execute('INSERT INTO Estudiante (legajo_id, dni, nombre, apellido, edad, fecha_nacimiento, curso, estado, email) VALUES (?,?,?)',
                (self.legajo_id, self.dni, self.nombre, self.apellido, self.edad, self.fecha_nacimiento, self.curso, self.estado, self.email ))

        conn.commit() # Guardar(confirmar) los cambios en la base de datos .
        conn.close() # Cerrar la conexión a la base de datos.

    # Método estático para obtener todos los estudiantes registrados en la base de datos.
    @staticmethod
    def obtener_estudiantes():
        #Cónectar a la base de datos 'escolar.db'
        conn = sqlite3.connect('escolar.db.sql')
        c = conn.cursor() # Crear un cursor para interactuar con la base de datos.

        # Ejecutar una consulta SQL para seleccionar todos los registros de la tabla 'Estudiantes'.
        c.execute('SELECT * FROM Estudiantes')

        estudiantes = c.fetchall() # Obtener todos los registros encontrados.
        conn.close() # Cerrar la conexión a la base de datos.

        return estudiantes # Devolver la lista de estudiantes.

    # Método para modificar la información de un estudiante en la base de datos.
    def modificar(self):
        # Conectar a la base de datos 'escolar.db'
        conn = sqlite3.connect('escolar.db.sql')
        c = conn.cursor()  # Crear un cursor para ejecutar comandos en la base de datos

        # Actualizar los datos del estudiante usando su legajo_id
        c.execute('''
            UPDATE Estudiante SET dni = ?, nombre = ?, apellido = ?, edad = ?, 
            fecha_nacimiento = ?, curso = ?, estado = ?, email = ? WHERE legajo_id = ?''',
            (self.dni, self.nombre, self.apellido, self.edad, self.fecha_nacimiento, self.curso, self.estado, self.email, self.legajo_id))

        conn.commit()  # Guardar (confirmar) los cambios en la base de datos
        conn.close()  # Cerrar la conexión a la base de datos

    # Método estático para mostrar todos los estudiantes registrados.
    @staticmethod
    def mostrar_todos(conn):
        # Llama al método obtener_estudiantes, que trae todos los estudiantes de la base de datos.
        estudiantes = Estudiante.obtener_estudiantes()
    
    # Recorre la lista de estudiantes que se obtuvo de la base de datos.
        for estudiante in estudiantes:
        # Imprime los datos de cada estudiante en un formato fácil de leer.
            print(f"Legajo: {estudiante[0]}, DNI: {estudiante[1]}, Nombre: {estudiante[2]} {estudiante[3]}, "
                f"Edad: {estudiante[4]}, Fecha de nacimiento: {estudiante[5]}, Curso: {estudiante[6]}, "
                f"Estado: {estudiante[7]}, Email: {estudiante[8]}")