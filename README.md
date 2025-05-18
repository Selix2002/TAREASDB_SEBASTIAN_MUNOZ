# Gestor de Dispositivos IoT con SQLAlchemy y Alembic

## Descripción

Este proyecto desarrolla un backend para administrar dispositivos IoT, junto con sus sensores y lecturas, apoyándose en **SQLAlchemy** como ORM y en **Alembic** para la gestión de versiones del esquema de la base de datos. Ofrece funcionalidades para dar de alta y organizar dispositivos, configurar sensores, almacenar sus datos de lectura y conservar registros de estado.


---

## Estructura del Proyecto

```
TAREAN1_SEBASTIAN_MUNOZ/
│
├── alembic/                # Migraciones de Alembic
│   ├── versions/           # Scripts de migración generados
    ├── env.py/             # Script de arranque de Alembic
├── app/
│   ├── __init__.py
│   ├── crud.py             # Funciones CRUD
│   ├── database.py         # Configuración de la base de datos
│   ├── main.py             # Script de ejemplo de uso
│   └── models.py           # Modelos SQLAlchemy
├── alembic.ini             # Configuración de Alembic
├── dump.sql                # Dump de la base de datos
├── pyproject.toml          # Dependencias del proyecto
├── .python-version         # Versión de Python usada
├── uv.lock                 # Lockfile de dependencias
└── README.md               # Este archivo
```

---

## Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/HisokaMorow1/BaseDeDatosIot.git
cd "TAREAN1_SEBASTIAN_MUNOZ"
```

### 2. Crear y activar un entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
uv pip install -r pyproject.toml
```

Asegúrate de tener instalados:
- SQLAlchemy
- Alembic
- psycopg2-binary

### 4. Configurar la base de datos PostgreSQL

Crea una base de datos y un usuario en PostgreSQL:

```sql
-- En psql como usuario postgres:
CREATE DATABASE tarea1_db;
CREATE USER postgres WITH PASSWORD 'sebas';
GRANT ALL PRIVILEGES ON DATABASE tarea1_db TO postgres;
```

Asegúrate de que la URL de conexión en `alembic.ini` y `app/database.py` sea:

```
postgresql+psycopg2://postgres:sebas@localhost/tarea1_db
```

---

## Migraciones de Base de Datos

### 1. Generar la migración inicial (ya incluida)

```bash
alembic revision --autogenerate -m "Initial schema"
```

### 2. Aplicar las migraciones

```bash
alembic upgrade head
```

---

## Restaurar la base de datos desde el dump

Si necesitas restaurar la base de datos a partir del dump:

```bash
PGPASSWORD=sebas psql -U postgres -h localhost -d tarea1_db < dump.sql
```

---

## Uso del sistema

Puedes ejecutar el script de ejemplo para probar las operaciones CRUD:

```bash
python main.py > print.txt
```

Esto demostrará la creación de tipos de dispositivos, grupos, dispositivos, sensores, lecturas y logs de estado, escribiendo los print en un documento de texto.

---

## Modificaciones de Esquema

- Se añadió la columna `umbral_alerta` a `Sensor`.
- Se añadió la columna `estado_actual` a `Dispositivo` para acceso rápido al estado.
- Se renombró `ubicacion` a `descripcion_ubicacion` y se añadió `coordenadas_gps` a `Dispositivo`.

---

## Dependencias

Incluidas en `pyproject.toml`:
- SQLAlchemy
- Alembic
- psycopg2-binary

---

## Autor

- [HisokaMorow1](https://github.com/HisokaMorow1)