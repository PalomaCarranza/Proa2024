import sqlite3 #Nesecesario para trabajar con la base de datos SQLite

class Profesor:
    def __init__(self, dni_id, nombre_profesor, apellido_profesor, curso_profesor, estado_profesor, email_profesor):
        self.dni_id = dni_id
        self.nombre_profesor = nombre_profesor 
        self.apellido_profesor = apellido_profesor
        self.curso_profesor = curso_profesor
        self.estado_profesor = estado_profesor
        self.email_profesor = email_profesor

    def guardar(self):
        # Conectar a la base de datos 'escolar.db'.
        conn = sqlite3.connect('escolar.db.sql')
        c = conn.cursor() # Crear un cursor para interactuar con la base de datos.

        # Ejecutar una consulta SQL para insertar los datos del profesor. 
        c.execute('INSERT INTO Profesor ( dni_id, nombre_profesor, apellido_profesor, curso_profesor, estado_profesor, email_profesor) VALUES (?,?,?)',
                (self.dni_id, self.nombre_profesor, self.apellido_profesor, self.curso_profesor, self.estado_profesor, self.email_profesor))

        conn.commit() # Guardar(confirmar) los cambios en la base de datos .
        conn.close() # Cerrar la conexión a la base de datos.

    # Método estático para obtener todos los profesores registrados en la base de datos.
    @staticmethod
    def obtener_profesores():
        #Cónectar a la base de datos 'escolar.db'
        conn = sqlite3.connect('escolar.db.sql')
        c = conn.cursor() # Crear un cursor para interactuar con la base de datos.

        # Ejecutar una consulta SQL para seleccionar todos los registros de la tabla 'Profesores'.
        c.execute('SELECT * FROM Profesor')

        profesores = c.fetchall() # Obtener todos los registros encontrados.
        conn.close() # Cerrar la conexión a la base de datos.

        return profesores # Devolver la lista de profesores. 

    # Método para modificar la información de un profesor en la base de datos.
    def modificar(self):
        # Conectar a la base de datos 'escolar.db'.
        conn = sqlite3.connect('escolar.db.sql')
        c = conn.cursor()  # Crear un cursor para interactuar con la base de datos.

        # Actualizar los datos del profesor en la fila que tiene el dni_id especificado.
        c.execute('''
            UPDATE Profesor SET nombre_profesor = ?, apellido_profesor = ?, curso_profesor = ?, 
            estado_profesor = ?, email_profesor = ? WHERE dni_id = ?''',
            (self.nombre_profesor, self.apellido_profesor, self.curso_profesor, self.estado_profesor, self.email_profesor, self.dni_id))

        conn.commit()  # Guardar (confirmar) los cambios en la base de datos.
        conn.close()  # Cerrar la conexión a la base de datos.
