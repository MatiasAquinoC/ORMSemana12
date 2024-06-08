import sqlite3

def obtener_estudiantes(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM estudiante')
    estudiantes = cursor.fetchall()
    conn.close()
    return estudiantes

def obtener_ciclos(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ciclo')
    ciclos = cursor.fetchall()
    conn.close()
    return ciclos

def obtener_cursos(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM curso')
    cursos = cursor.fetchall()
    conn.close()
    return cursos

def obtener_cursos_ciclo(db_path, idCiclo):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT curso.* FROM curso
        INNER JOIN ciclo_curso ON curso.codigoCurso = ciclo_curso.codigoCurso
        WHERE ciclo_curso.idCiclo = ?
    ''', (idCiclo,))
    cursos = cursor.fetchall()
    conn.close()
    return cursos
