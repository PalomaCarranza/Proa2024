import sqlite3

class Estudiante:
    def __init__(self, nombre, edad, anho_id):
        self.nombre = nombre
        self.edad = edad
        self.anho_id = anho_id
        
    def guardar (self):
        conn = sqlite3.connect ('escolar.db')
        c = conn.cursor()

        c.execute('INSERT INTO Estudiantes (nombre, edad, año_id) VALUES (?, ?, ?)',
        (self.nombre, self.edad, self.anho_id))

        conn.commit
        conn.close

    
    staticmethod
    def obtener_estudiantes():
        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()

        c.execute('SELECT * FROM Estudiantes')