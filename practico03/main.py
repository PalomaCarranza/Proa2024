import sqlite3
import ClsEstudiante
import ClsCalificacion
import ClsMateria
import ClsProfesor 

def conectar_db():
    conn = sqlite3.connect('escuela.db')
    return conn

def main():
    conn = conectar_db()
    conn = conn.cursor