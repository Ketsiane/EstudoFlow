from pydantic import BaseModel

# O que o sistema recebe quando criamos ou atualizamos uma disciplina
class DisciplinaBase(BaseModel):
    nome: str
    carga_horaria: int
    tempo_estudado: int

class DisciplinaCreate(DisciplinaBase):
    pass

# O que a nossa API vai devolver de resposta (incluindo o ID automático do banco)
class DisciplinaResponse(DisciplinaBase):
    id: int

    class Config:
        from_attributes = True