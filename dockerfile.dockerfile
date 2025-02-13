# Use uma imagem base do Python
FROM python:3.9

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da API para o diretório de trabalho
COPY . .

# Exponha a porta em que a API está rodando
EXPOSE 5000

# Comando para iniciar a API
CMD ["python", "app.py"]
