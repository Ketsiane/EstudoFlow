from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import models, schemas, database

app = FastAPI(
    title="EstudoFlow API", 
    description="Sistema de gestão e monitorização de fluxos de estudo"
)

# Cria automaticamente a tabela no banco de dados do Render ao iniciar a API
models.Base.metadata.create_all(bind=database.engine)

# --- ROTAS DO CRUD ---

# 1. CRIAR UMA DISCIPLINA (POST)
@app.post("/disciplinas/", response_model=schemas.DisciplinaResponse, status_code=status.HTTP_201_CREATED)
def criar_disciplina(disciplina: schemas.DisciplinaCreate, db: Session = Depends(database.get_db)):
    nova_disciplina = models.Disciplina(**disciplina.model_dump())
    db.add(nova_disciplina)
    db.commit()
    db.refresh(nova_disciplina)
    return nova_disciplina

# 2. LISTAR TODAS AS DISCIPLINAS (GET)
@app.get("/disciplinas/", response_model=List[schemas.DisciplinaResponse])
def listar_disciplinas(db: Session = Depends(database.get_db)):
    return db.query(models.Disciplina).all()

# 3. BUSCAR UMA DISCIPLINA POR ID (GET)
@app.get("/disciplinas/{disciplina_id}", response_model=schemas.DisciplinaResponse)
def obter_disciplina(disciplina_id: int, db: Session = Depends(database.get_db)):
    disciplina = db.query(models.Disciplina).filter(models.Disciplina.id == disciplina_id).first()
    if not disciplina:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    return disciplina

# 4. ATUALIZAR UMA DISCIPLINA POR ID (PUT)
@app.put("/disciplinas/{disciplina_id}", response_model=schemas.DisciplinaResponse)
def atualizar_disciplina(disciplina_id: int, disciplina_atualizada: schemas.DisciplinaCreate, db: Session = Depends(database.get_db)):
    disciplina_query = db.query(models.Disciplina).filter(models.Disciplina.id == disciplina_id)
    disciplina = disciplina_query.first()
    
    if not disciplina:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    
    disciplina_query.update(disciplina_atualizada.model_dump(), synchronize_session=False)
    db.commit()
    return d_query.first() if (d_query := db.query(models.Disciplina).filter(models.Disciplina.id == disciplina_id)) else disciplina_query.first()

# 5. APAGAR UMA DISCIPLINA POR ID (DELETE)
@app.delete("/disciplinas/{disciplina_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_disciplina(disciplina_id: int, db: Session = Depends(database.get_db)):
    disciplina_query = db.query(models.Disciplina).filter(models.Disciplina.id == disciplina_id)
    disciplina = disciplina_query.first()
    
    if not disciplina:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    
    disciplina_query.delete(synchronize_session=False)
    db.commit()
    return None