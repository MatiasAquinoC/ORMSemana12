import sqlite3

class Base:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS estudiante (
                codigoEstudiante INTEGER PRIMARY KEY,
                edad INTEGER,
                nombre TEXT,
                carrera TEXT,
                promedio REAL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ciclo (
                idCiclo INTEGER PRIMARY KEY,
                año INTEGER,
                fechaInicio TEXT,
                fechaFin TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS curso (
                codigoCurso INTEGER PRIMARY KEY,
                nombre TEXT,
                descripcion TEXT,
                creditos INTEGER,
                profesor TEXT,
                aula TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ciclo_curso (
                idCiclo INTEGER,
                codigoCurso INTEGER,
                FOREIGN KEY (idCiclo) REFERENCES ciclo(idCiclo),
                FOREIGN KEY (codigoCurso) REFERENCES curso(codigoCurso)
            )
        ''')
        self.conn.commit()

    def close(self):
        self.conn.close()
