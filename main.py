import pandas as pd
import plotly.express as px
import streamlit as st
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv


# Carregar variáveis de ambiente
load_dotenv()

# Conexão com o banco de dados
Url = os.getenv('DATABASE_URL')
engine = create_engine(Url) 

# Função para carregar dados de uma view com tratamento de erro
def load_data(view_name):
    try:
        data = pd.read_sql(f"SELECT * FROM {view_name}", engine)
        return data
    except Exception as e:
        st.error(f"Erro ao carregar a view '{view_name}': {e}")
        return None

# Título do dashboard
st.title('Dashboard de Temperaturas IoT')

# Gráfico 1: Média de temperatura por dispositivo
st.header('Média de Temperatura por Dispositivo')
df_avg_temp = load_data('max_temp_por_dispositivo_periodo')
if df_avg_temp is not None:
    fig1 = px.bar(df_avg_temp, x='dispositivo', y='max_temp', title='Média de Temperatura por Dispositivo')
    st.plotly_chart(fig1)
else:
    st.write('df_avg_temp')

# Gráfico 2: Contagem de leituras por hora
st.header('Leituras por Hora do Dia')
df_leituras_hora = load_data('leituras_por_hora')
if df_leituras_hora is not None:
    fig2 = px.line(df_leituras_hora, x='hora', y='contagem', title='Leituras por Hora do Dia')
    st.plotly_chart(fig2)

# Gráfico 3: Temperaturas máximas e mínimas por dia
st.header('Temperaturas Máximas e Mínimas por Dia')
df_temp_max_min = load_data('temp_max_min_por_dia')
if df_temp_max_min is not None:
    fig3 = px.line(df_temp_max_min, x='data', y=['max_temp', 'min_temp'], title='Temperaturas Máximas e Mínimas por Dia')
    st.plotly_chart(fig3)