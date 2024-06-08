from modelo.base import Base

class Estudiante(Base):
    def __init__(self, db_path, codigoEstudiante, edad, nombre, carrera, promedio):
        super().__init__(db_path)
        self.codigoEstudiante = codigoEstudiante
        self.edad = edad
        self.nombre = nombre
        self.carrera = carrera
        self.promedio = promedio

    def actualizarPromedio(self, nuevo_promedio):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE estudiante
            SET promedio = ?
            WHERE codigoEstudiante = ?
        ''', (nuevo_promedio, self.codigoEstudiante))
        self.conn.commit()

    def cambiarCarrera(self, nueva_carrera):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE estudiante
            SET carrera = ?
            WHERE codigoEstudiante = ?
        ''', (nueva_carrera, self.codigoEstudiante))
        self.conn.commit()
