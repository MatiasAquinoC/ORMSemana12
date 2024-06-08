from modelo.base import Base

class Curso(Base):
    def __init__(self, db_path, codigoCurso, nombre, descripcion, creditos, profesor, aula):
        super().__init__(db_path)
        self.codigoCurso = codigoCurso
        self.nombre = nombre
        self.descripcion = descripcion
        self.creditos = creditos
        self.profesor = profesor
        self.aula = aula

    def inscribirEstudiante(self, codigoEstudiante):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO curso_estudiante (codigoCurso, codigoEstudiante)
            VALUES (?, ?)
        ''', (self.codigoCurso, codigoEstudiante))
        self.conn.commit()

    def retirarEstudiante(self, codigoEstudiante):
        cursor = self.conn.cursor()
        cursor.execute('''
            DELETE FROM curso_estudiante
            WHERE codigoCurso = ? AND codigoEstudiante = ?
        ''', (self.codigoCurso, codigoEstudiante))
        self.conn.commit()

    def cambiarProfesor(self, nuevo_profesor):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE curso
            SET profesor = ?
            WHERE codigoCurso = ?
        ''', (nuevo_profesor, self.codigoCurso))
        self.conn.commit()
