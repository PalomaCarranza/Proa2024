import sqlite3 #Nesecesario para trabajar con la base de datos SQLite

class Estudiante:
    # Método constructor que inicializa las propiedades del objeto Estudiante.
    def __init__(self, nombre, edad, anno, dni_id):
        self.nombre = nombre # Nombre del estudiante.
        self.edad = edad # Edad del estudiante.
        self.anno = anno # ID del año academico del estudiante.
        self.dni_id = dni_id

    # Método para guardar la información del estudiante en la base de datos.
    def guardar(self):
        # Conectar a la base de datos 'escolar.db'.
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor() # Crear un cursor para interactuar con la base de datos.

        # Ejecutar una consulta SQL para insertar los datos del estudiate. 
        c.execute('INSERT INTO Estudiante (nombre, edad, anno, dni_id) VALUES (?,?,?)',
                (self.nombre, self.edad, self.anno, self.dni_id))

        conn.commit() # Guardar(confirmar) los cambios en la base de datos .
        conn.close() # Cerrar la conexión a la base de datos.

    # Método estático para obtener todos los estudiantes registrados en la base de datos.
    @staticmethod
    def obtener_estudiantes():
        #Cónectar a la base de datos 'escolar.db'
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor() # Crear un cursor para interactuar con la base de datos.

        # Ejecutar una consulta SQL para seleccionar todos los registros de la tabla 'Estudiantes'.
        c.execute('SELECT * FROM Estudiantes')

        estudiantes = c.fetchall() # Obtener todos los registros encontrados.
        conn.close() # Cerrar la conexión a la base de datos.

        return estudiantes # Devolver la lista de estudiantes. 