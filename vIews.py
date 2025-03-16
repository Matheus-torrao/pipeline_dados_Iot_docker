from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configuração da conexão
Url = os.getenv('DATABASE_URL')
engine = create_engine(Url)

Session = sessionmaker(bind=engine)
session = Session()

# Criação das views no banco de dados
create_view_max_temp_por_dispositivo_periodo = text("""
DROP VIEW IF EXISTS max_temp_por_dispositivo_periodo;
CREATE VIEW max_temp_por_dispositivo_periodo AS
SELECT 
    room_id AS dispositivo,
    MAX(temp) AS max_temp,
    DATE_TRUNC('week', noted_date) AS semana
FROM iot_temp
GROUP BY room_id, DATE_TRUNC('week', noted_date)
ORDER BY semana DESC, dispositivo;
""")

create_view_temp_max_min_por_dia = text("""
DROP VIEW IF EXISTS temp_max_min_por_dia;
CREATE VIEW temp_max_min_por_dia AS
SELECT 
    DATE(noted_date) AS data,
    MAX(temp) AS max_temp,
    MIN(temp) AS min_temp
FROM iot_temp
GROUP BY DATE(noted_date)
ORDER BY data;
""")
create_view_leituras_por_hora = text("""
DROP VIEW IF EXISTS leituras_por_hora;
CREATE VIEW leituras_por_hora AS
SELECT 
    DATE_TRUNC('hour', noted_date) AS hora, 
    COUNT(*) AS contagem
FROM iot_temp
GROUP BY DATE_TRUNC('hour', noted_date)
ORDER BY hora;
""")

try:
    session.execute(create_view_max_temp_por_dispositivo_periodo)
    session.execute(create_view_temp_max_min_por_dia)
    session.execute(create_view_leituras_por_hora)
    session.commit()
    print("Views criadas com sucesso!")
except Exception as e:
    session.rollback()
    print(f"Erro ao criar as views: {e}")

# Função para consultar uma view
def consultar_view(view_name):
    try:
        result = session.execute(text(f"SELECT * FROM {view_name}"))
        for row in result:
            print(row)
    except Exception as e:
        print(f"Erro ao consultar a view {view_name}: {e}")

