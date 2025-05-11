# SecureSaaS Project

Proyecto de implementación segura de una aplicación SaaS con FastAPI, Docker, Nginx, Prometheus, Grafana, Loki y CI/CD con GitHub Actions. Este proyecto simula un entorno de producción aplicando principios DevSecOps.

## Características Principales

* **Backend:** API RESTful con FastAPI (Python).

* **Contenerización:** Docker y Docker Compose para todos los servicios.

* **Proxy Inverso:** Nginx para gestionar el tráfico y como punto de entrada.

* **Autenticación:** Basada en tokens Bearer para endpoints seguros.

* **Observabilidad:**

    * **Prometheus:** Recolección de métricas.
    * **Grafana:** Visualización de métricas y logs.
    * **Loki:** Agregación centralizada de logs.
    
* **CI/CD:** Pipeline básico con GitHub Actions para instalación de dependencias y ejecución de pruebas.
* **Seguridad:**
    * Modelado de amenazas (STRIDE).
    * Gestión de secretos con archivos `.env`.
    * Script de backup y cifrado con GPG.
    * Pruebas de seguridad (DAST, SAST, escaneo de dependencias y secretos - conceptualizadas).
* **Logging:** Configuración del driver de logging de Docker para enviar logs del backend a Loki.


## 📁 Estructura del Proyecto

```text

📁 SecureSaaS
├── 📄 docker-compose.yml
├── 📁 backend
│   ├── 📄 Dockerfile
│   ├── 📄 requirements.txt
│   ├── 📄 .env
│   ├── 📁 app
│   │   ├── 📄 auth.py
│   │   ├── 📄 config.py
│   │   ├── 📄 main.py
│   │   ├── 📄 models.py
│   │   └── 📄 routers.py
│   └── 📁 tests
│       └── 📄 test_app.py
├── 📁 .github
│   └── 📁 workflows
│       └── 📄 ci-cd.yml
├── 📁 infra
│   ├── 📁 grafana
│   │   └── 📁 provisioning
│   │       ├── 📁 dashboards
│   │       │   └── 📄 dashboard.json
│   │       └── 📁 datasources
│   │           └── 📄 datasources.yml
│   ├── 📁 loki
│   │   ├── 📄 config.yaml
│   │   ├── 📁 boltdb-cache
│   │   │   └── 📁 index_20218
│   │   │       └── 📁 fake
│   │   ├── 📁 chunks
│   │   │   └── 📄 loki_cluster_seed.json
│   │   ├── 📁 compactor
│   │   ├── 📁 index
│   │   │   └── 📁 uploader
│   │   │       └── 📄 name
│   │   └── 📁 wal
│   │       ├── 📄 00000065
│   │       └── 📁 checkpoint.000064
│   │           └── 📄 00000000
│   ├── 📁 nginx
│   │   └── 📄 default.conf
│   └── 📁 prometheus
│       └── 📄 prometheus.yml
└── 📁 scripts
    ├── 📄 backup_and_encrypt.sh
    └── 📄 run_tests.sh
```

## Prerrequisitos

* Docker Engine (v20.10+)
* Docker Compose (v1.29+ o `docker compose` CLI v2+)
* Git
* GnuPG (GPG) (para el script de backup)

## Despliegue Local

1.  **Clonar el repositorio:**

    git clone [https://github.com/rgommez/SecureSaaS.git](https://github.com/rgommez/SecureSaaS.git)
    
    cd SecureSaaS
    

3.  **Configurar variables de entorno para el backend:**

    cp backend/.env.example backend/.env

    *(Puedes editar `backend/.env` si es necesario, pero el `SECRET_KEY=changeme` por defecto funciona con el token `secret-token`)*

4.  **Construir y levantar los contenedores:**

    docker-compose up --build

    *(Para ejecutar en segundo plano: `docker-compose up -d --build`)*


## Acceso a los Servicios

* **API Docs (Swagger UI):** `http://localhost/docs`

* **Endpoint Seguro (ejemplo con `curl` y token correcto):**

    curl -H "Authorization: Bearer secret-token" http://localhost/secure-endpoint

* **Prometheus UI:** `http://localhost:9090`

* **Grafana UI:** `http://localhost:3000` (login: `admin/admin`, pedirá cambio de contraseña)

* **Loki:** Los logs se consultan a través de Grafana (datasource Loki).


## Ejecución de Scripts

* **Ejecutar Pruebas:**

    ./scripts/run_tests.sh

    *(Asegúrate de que tenga permisos de ejecución: `chmod +x ./scripts/run_tests.sh`)*

* **Crear Backup Cifrado:**

    ./scripts/backup_and_encrypt.sh

    *(Asegúrate de que tenga permisos de ejecución: `chmod +x ./scripts/backup_and_encrypt.sh`). Te pedirá una passphrase para GPG.*

## Stack Tecnológico Principal

* Python, FastAPI, Uvicorn
* Docker, Docker Compose
* Nginx
* Prometheus, Grafana, Loki
* GitHub Actions
* GPG
