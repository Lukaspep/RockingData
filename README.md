# Ejercicio RockingData

Ejercicio script de python para puesto DevOps Jr. 
- Utilize Flask para crear el microservicio, y tambien se adaptaba muy bien a las consignas dadas.
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
   Con este comando, estamos construyendo la imagen de nuestra aplicacion, y con -t le damos un nombre.
   ```
4. Correr la app :

   ```bash
   docker build -p 5000:5000 pythonscript1
   La app va a estar habilitada en localhost:5000
   Una vez que quieran dejar de utilizarla con Ctrl + C la app deja de correr (presionar mismo en la terminal).
   ```

5. Docker Start y Docker Stop:

  ```bash
  Para que la app deje de correr y tambien cuando la quieren comenzar a utilizar: 

  Docker stop (nombre del contenedor)
  Docker start (nombre del contenedor)
  ```
