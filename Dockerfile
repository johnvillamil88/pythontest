# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY requirements.txt .
COPY app.py .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que la aplicación se ejecutará
EXPOSE 5000

# Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["python", "app.py"]
