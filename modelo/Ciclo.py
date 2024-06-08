from modelo.base import Base

class Ciclo(Base):
    def __init__(self, db_path, idCiclo, año, fechaInicio, fechaFin):
        super().__init__(db_path)
        self.idCiclo = idCiclo
        self.año = año
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin

    def agregarCurso(self, codigoCurso):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO ciclo_curso (idCiclo, codigoCurso)
            VALUES (?, ?)
        ''', (self.idCiclo, codigoCurso))
        self.conn.commit()

    def eliminarCurso(self, codigoCurso):
        cursor = self.conn.cursor()
        cursor.execute('''
            DELETE FROM ciclo_curso
            WHERE idCiclo = ? AND codigoCurso = ?
        ''', (self.idCiclo, codigoCurso))
        self.conn.commit()

    def actualizarEstado(self, fechaInicio, fechaFin):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE ciclo
            SET fechaInicio = ?, fechaFin = ?
            WHERE idCiclo = ?
        ''', (fechaInicio, fechaFin, self.idCiclo))
        self.conn.commit()
