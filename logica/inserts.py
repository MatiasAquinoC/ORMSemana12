import sqlite3

def insertar_estudiante(db_path, codigoEstudiante, edad, nombre, carrera, promedio):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO estudiante (codigoEstudiante, edad, nombre, carrera, promedio)
        VALUES (?, ?, ?, ?, ?)
    ''', (codigoEstudiante, edad, nombre, carrera, promedio))
    conn.commit()
    conn.close()

def insertar_ciclo(db_path, idCiclo, año, fechaInicio, fechaFin):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO ciclo (idCiclo, año, fechaInicio, fechaFin)
        VALUES (?, ?, ?, ?)
    ''', (idCiclo, año, fechaInicio, fechaFin))
    conn.commit()
    conn.close()

def insertar_curso(db_path, codigoCurso, nombre, descripcion, creditos, profesor, aula):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO curso (codigoCurso, nombre, descripcion, creditos, profesor, aula)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (codigoCurso, nombre, descripcion, creditos, profesor, aula))
    conn.commit()
    conn.close()
