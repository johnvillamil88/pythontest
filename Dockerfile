# Usa una imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo app.py al contenedor en el directorio /app
COPY app.py .

# Instala las dependencias
# Si tu aplicación tiene un archivo requirements.txt, cámbialo según sea necesario
RUN pip install flask

# Expone el puerto 5000 para la aplicación Flask
EXPOSE 5000

# Define la variable de entorno FLASK_APP y establece la aplicación como app.py
ENV FLASK_APP=app.py

# Ejecuta la aplicación cuando se inicia el contenedor
CMD ["flask", "run", "--host", "0.0.0.0"]
