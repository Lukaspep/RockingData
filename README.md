# Ejercicio RockingData

Ejercicio script de python para puesto DevOps Jr.

## Requirements

Flask==3.0.0
Werkzeug==3.0.1

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/Lukaspep/RockingData.git

2. Navegar al directorio:

   ```bash
   cd "Script Archivos"
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