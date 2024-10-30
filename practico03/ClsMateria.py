import sqlite3 #Nesecesario para trabajar con la base de datos SQLite

class Materia:
    def __init__(self, id_materia, nombre_materia, curso_materia, descripcion, horario):
        self.id_materia = id_materia
        self.nombre_materia = nombre_materia
        self.curso_materia = curso_materia
        self.descripcion = descripcion
        self.horario = horario

    def guardar(self):
        # Conectar a la base de datos 'escolar.db'.
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor() # Crear un cursor para interactuar con la base de datos.

        # Ejecutar una consulta SQL para insertar los datos de la materia. 
        c.execute('INSERT INTO Materia (id_materia, nombre_materia, curso_materia, descripcion, horario) VALUES (?,?,?)',
                (self.id_materia, self.nombre_materia, self.curso_materia, self.descripcion, self.horario))

        conn.commit() # Guardar(confirmar) los cambios en la base de datos .
        conn.close() # Cerrar la conexión a la base de datos.

    # Método estático para obtener todas las materias registradas en la base de datos.
    @staticmethod
    def obtener_materias():
        #Cónectar a la base de datos 'escolar.db'
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor() # Crear un cursor para interactuar con la base de datos.

        # Ejecutar una consulta SQL para seleccionar todos los registros de la tabla 'Materias'.
        c.execute('SELECT * FROM Materias')

        materias = c.fetchall() # Obtener todos los registros encontrados.
        conn.close() # Cerrar la conexión a la base de datos.

        return materias # Devolver la lista de materias.

    # Método para borrar una materia en la base de datos por id_materia.
    def borrar(self):
        # Conectar a la base de datos 'escolar.db'.
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()  # Crear un cursor para interactuar con la base de datos.

        # Eliminar el registro de la materia usando su id_materia.
        c.execute('DELETE FROM Materia WHERE id_materia = ?', (self.id_materia,))

        conn.commit()  # Guardar (confirmar) los cambios en la base de datos.
        conn.close()  # Cerrar la conexión a la base de datos.

    # Método para modificar la información de una materia en la base de datos.
    def modificar(self):
        # Conectar a la base de datos 'escolar.db'.
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()  # Crear un cursor para interactuar con la base de datos.

        # Actualizar los datos de la materia en la fila que tiene el id_materia especificado.
        c.execute('''
            UPDATE Materia SET nombre_materia = ?, curso_materia = ?, descripcion = ?, 
            horario = ? WHERE id_materia = ?''',
            (self.nombre_materia, self.curso_materia, self.descripcion, self.horario, self.id_materia))

        conn.commit()  # Guardar (confirmar) los cambios en la base de datos.
        conn.close()  # Cerrar la conexión a la base de datos.