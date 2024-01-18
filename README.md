# Ejercicio RockingData

Ejercicio script de python para puesto DevOps Jr. Utilize Flask por que se me era mas comodo para crear el microservicio y fue una herramienta que me ayudo a optimizar el tiempo.
- Algo a aclarar que me falto en el video, es que a medida que el usuario sube archivos se van alojando en la carpeta uploads.
- Me fue de ayuda esta documentacion: https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/
- Algo que me di cuenta despues de terminarlo, y que podia usar era el multi-stage builds de Docker para optimizar la imagen. https://docs.docker.com/build/building/multi-stage/

## Requirements

- Flask==3.0.0
- Werkzeug==3.0.1

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/Lukaspep/RockingData.git

2. Navegar al directorio:

   ```bash
   cd "RockingData"
   ```
3. Docker Build:

   ```bash
   docker build -t pythonscript1 .
   ```
4. Correr la app :

   ```bash
   docker build -p 5000:5000 pythonscript1
   La app va a estar habilitada en localhost:5000
   ```

5. Docker Start y Docker Stop:

  ```bash
  Para parar la app deben correr el comando Docker ps -a 

  Docker stop (nombre del contenedor)
  Docker start (nombre del contenedor)
  ```
