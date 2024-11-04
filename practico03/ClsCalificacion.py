import sqlite3 #Nesecesario para trabajar con la base de datos SQLite

class Calificacion:
    def __init__(self, legajo_id, id_materia, nota, fecha):
        self.legajo_id = legajo_id
        self.id_materia = id_materia
        self.nota = nota
        self.fecha = fecha

    def guardar(self):
        # Conectar a la base de datos 'escolar.db'.
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor() # Crear un cursor para interactuar con la base de datos.

        # Ejecutar una consulta SQL para insertar los datos del estudiate. 
        c.execute('INSERT INTO Calificación (nombre, edad, anno, dni_id) VALUES (?,?,?)',
                (self.nombre, self.edad, self.anno, self.dni))

        conn.commit() # Guardar(confirmar) los cambios en la base de datos .
        conn.close() # Cerrar la conexión a la base de datos.

    # Método estático para obtener todas las calificaciones registradas en la base de datos.
    @staticmethod
    def obtener_calificaciones():
        #Cónectar a la base de datos 'escolar.db'
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor() # Crear un cursor para interactuar con la base de datos.

        # Ejecutar una consulta SQL para seleccionar todos los registros de la tabla 'Calificaciones'.
        c.execute('SELECT * FROM Estudiante')

        calificaciones = c.fetchall() # Obtener todos los registros encontrados.
        conn.close() # Cerrar la conexión a la base de datos.

        return calificaciones # Devolver la lista de calificaciones.

    # Método para borrar una calificación de la base de datos por legajo_id e id_materia.
    def borrar(self):
        # Conectar a la base de datos 'escolar.db'.
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()  # Crear un cursor para interactuar con la base de datos.

        # Eliminar el registro de la calificación usando legajo_id e id_materia.
        c.execute('DELETE FROM Calificacion WHERE legajo_id = ? AND id_materia = ?', (self.legajo_id, self.id_materia))

        conn.commit()  # Guardar (confirmar) los cambios en la base de datos.
        conn.close()  # Cerrar la conexión a la base de datos.

    # Método para modificar la información de una calificación en la base de datos.
    def modificar(self):
        # Conectar a la base de datos 'escolar.db'.
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()  # Crear un cursor para interactuar con la base de datos.

        # Actualizar la nota y la fecha de la calificación en la fila que tiene el legajo_id e id_materia especificados.
        c.execute('''
            UPDATE Calificacion SET nota = ?, fecha = ? 
            WHERE legajo_id = ? AND id_materia = ?''',
            (self.nota, self.fecha, self.legajo_id, self.id_materia))

        conn.commit()  # Guardar (confirmar) los cambios en la base de datos.
        conn.close()  # Cerrar la conexión a la base de datos. 