from sqlalchemy import create_engine, Column, Integer, String, DateTime, text
from sqlalchemy.orm import sessionmaker, declarative_base
import pandas as pd
from sqlalchemy.exc import IntegrityError
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Configurações do banco de dados
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Criar conexão com o banco de dados
Url = os.getenv('DATABASE_URL')
engine = create_engine(Url)

Session = sessionmaker(bind=engine)
session = Session()

# Definir modelo ORM
Base = declarative_base()

class IOTTemp(Base):
    __tablename__ = "iot_temp"
    id = Column(Integer, primary_key=True, autoincrement=True)
    record_id = Column(String, unique=True)
    room_id = Column(String)
    noted_date = Column(DateTime)
    temp = Column(Integer)
    location = Column(String)

# Criar tabela se não existir
Base.metadata.create_all(engine)

# Ler dados do CSV
df = pd.read_csv("/set_data/IOT-temp.csv")

# Ajusta nomes das colunas 
df = df.rename(columns={"id": "record_id", "room_id/id": "room_id", "out/in": "location"})

# Converte a coluna de data para TIMESTAMP
df["noted_date"] = pd.to_datetime(df["noted_date"], format="%d-%m-%Y %H:%M")

# Cria lista de objetos para inserção
records = [
    IOTTemp(
        record_id=row["record_id"],
        room_id=row["room_id"],
        noted_date=row["noted_date"],
        temp=row["temp"],
        location=row["location"]
    )
    for _, row in df.iterrows()
]

# Inserir os dados no banco de dados
try:
    session.bulk_save_objects(records)
    session.commit()
    print("Dados inseridos com sucesso!")
except IntegrityError as e:
    session.rollback()
    print(f"Erro de integridade ao inserir os dados: {e}")
except Exception as e:
    session.rollback()
    print(f"Erro ao inserir os dados: {e}")

# Consultar para verificar inserção
try:
    result = session.execute(text("SELECT COUNT(*) FROM iot_temp"))
    count = result.scalar()
    print(f"Total de registros na tabela 'iot_temp': {count}")
except Exception as e:
    print(f"Erro ao consultar a tabela: {e}")

session.close()
