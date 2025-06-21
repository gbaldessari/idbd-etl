# ETL Multifuente con Python, MySQL y PostgreSQL

Este proyecto implementa un pipeline ETL (Extract, Transform, Load) en Python que extrae datos desde múltiples fuentes heterogéneas y los carga en una base de datos PostgreSQL para su posterior análisis.

## Estructura del Proyecto

``` sh
etl_tarea/
├── main.py                # Script principal que ejecuta el proceso ETL
├── config.py              # Configuración de rutas y credenciales
├── requirements.txt       # Dependencias del proyecto
├── docker-compose.yml     # Orquestación de contenedores MySQL, PostgreSQL y Adminer
├── extract/               # Módulos de extracción por fuente
│   ├── db.py              # Extracción desde MySQL
│   ├── api.py             # Extracción desde API REST
│   ├── csv.py             # Extracción desde archivo CSV
│   ├── json.py            # Extracción desde archivo JSON
│   └── kafka.py           # Simulación de extracción desde Kafka
├── load/
│   └── load.py            # Funciones para cargar datos en PostgreSQL
├── data/
│   ├── sales_data.csv     # Datos de ventas (CSV)
│   └── user_profiles.json # Perfiles de usuario (JSON)
├── mysql-init/
│   └── init.sql           # Script de inicialización de MySQL
├── postgres-init/
│   └── init.sql           # Script de inicialización de PostgreSQL
└── README.md              # Este archivo
```

## Fuentes de Datos

1. **MySQL**: Clientes (tabla `customers`)
2. **API REST**: Usuarios ([https://jsonplaceholder.typicode.com/users](https://jsonplaceholder.typicode.com/users))
3. **CSV**: Ventas (`data/sales_data.csv`)
4. **JSON**: Perfiles de usuario (`data/user_profiles.json`)
5. **Kafka (simulado)**: Eventos de usuario

Todos los datos se cargan en tablas de staging en PostgreSQL.

## Requisitos

- Python 3.8+
- Docker y Docker Compose

## Instalación

1. Instala las dependencias de Python:

   ```sh
   pip install -r requirements.txt
   ```

2. Levanta los servicios de bases de datos y Adminer:

   ```sh
   docker-compose up -d
   ```

3. Ejecuta el pipeline ETL:

   ```sh
   python main.py
   ```

4. (Opcional) Accede a Adminer para explorar las bases de datos:

   - Ingresa a [http://localhost:8080](http://localhost:8080)
   - Para conectarte a **MySQL** usa:
     - Sistema: MySQL
     - Servidor: mysql-source
     - Usuario: etl_user
     - Contraseña: etl_password
     - Base de datos: ecommerce_db
   - Para conectarte a **PostgreSQL** usa:
     - Sistema: PostgreSQL
     - Servidor: postgres-destination
     - Usuario: etl_user
     - Contraseña: etl_password
     - Base de datos: etl_repository

5. Cuando termines, apaga los servicios:

   ```sh
   docker-compose down
   ```

## Notas

- Los scripts de inicialización (`init.sql`) crean las tablas necesarias y datos de ejemplo.
- El pipeline es incremental para MySQL (solo extrae registros recientes).
- El módulo Kafka es una simulación y no requiere un broker real.

## Autor

- Giacomo Baldessari
