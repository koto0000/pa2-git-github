# Imagen base
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código
COPY . /app

# Exponer puerto
EXPOSE 5000

# Comando de ejecución
CMD ["python", "app.py"]
