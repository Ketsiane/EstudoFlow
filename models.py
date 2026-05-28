from sqlalchemy import Column, Integer, String
from database import Base

class Disciplina(Base):
    __tablename__ = "disciplinas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    carga_horaria = Column(Integer, default=0)  # Tempo planejado em horas
    tempo_estudado = Column(Integer, default=0) # Tempo já executado em minutos