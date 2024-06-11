# Use a imagem oficial do Python como base
FROM python:3.11-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação para o diretório de trabalho
COPY . .

# Comando para rodar a aplicação
CMD ["python", "app.py"]
