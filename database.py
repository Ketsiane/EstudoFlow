from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Sua URL oficial do Render conectada diretamente via driver psycopg2
URL_BANCO = "postgresql://estudoflow_db_user:fiVzZzIkzCuhhRwYV39SIZNcw7maUlCs@dpg-d8bp496l51nc73e1ul5g-a.oregon-postgres.render.com/estudoflow_db"

engine = create_engine(URL_BANCO)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Função usada pelas rotas para abrir e fechar as conexões
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()