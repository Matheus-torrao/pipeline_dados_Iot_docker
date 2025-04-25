# Imagem base do Python
FROM python:3.11-slim

# Instalações de dependências de sistema e Poetry
RUN apt-get update && apt-get install -y curl gcc libpq-dev && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos do projeto
COPY . .

# Desativa a criação de virtualenv (usaremos o ambiente global do container)
ENV POETRY_VIRTUALENVS_CREATE=false

# Instala as dependências com Poetry
RUN poetry install --no-root

# Define variáveis de ambiente a partir do .env (se necessário)
ENV PYTHONUNBUFFERED=1

# Comando padrão para rodar o script
CMD ["python","streamlit", "run", "insercao.py"]
