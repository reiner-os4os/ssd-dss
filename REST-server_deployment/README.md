# SSD-DSS REST Server Deployment

A Docker-based deployment for the Spatial System Dynamics Simulation - Decision Support System (SSD-DSS) with Jupyter Notebook and REST API server capabilities.

## Overview

This deployment provides:
- **Jupyter Notebook** environment for interactive data analysis and system dynamics modeling
- **BPTK-Py** (Business Process Thinking Kit for Python) for system dynamics simulations
- **Flask REST API Server** for exposing simulation models as REST endpoints
- **PostGIS Database Support** for spatial data operations with geospatial extensions
- **SQLAlchemy ORM** for database abstraction and query operations

## Getting Started

There are two ways to deploy the system:

1. **Use the pre-built image from Docker Hub** (recommended for quick start)
   - Image: `reineros4os/ssd-server:1`
   - Visit: https://hub.docker.com/u/reineros4os

2. **Build your own image locally** using the provided Dockerfile

## Files in This Directory

| File | Purpose |
|------|---------|
| **Dockerfile** | Container image definition with all dependencies and Python packages |
| **docker-compose.yml** | Orchestration file defining services, volumes, ports, and environment variables |
| **.env_template** | Environment configuration template (copy to `.env` and edit) |

## Building Your Own Image

To build a custom image, run:

```bash
docker build -f Dockerfile -< yourname/ssd-server:1 .
```

Or with Docker Compose:

```bash
docker-compose build
```

## Using Pre-built Image

The pre-built image includes:
- Python 3.9 with Jupyter Base Notebook
- BPTK-Py 1.9.0 for system dynamics modeling
- Flask-Cors 4.0.0 for REST API cross-origin support
- Werkzeug 2.3.0 for HTTP request handling
- GeoAlchemy2, SQLAlchemy, and ipython-sql for database operations

## Start the BPTK REST API Server
For reference see this documentation:
https://github.com/transentis/bptk_intro/tree/master

### Install the required packages
Open a new terminal in Juptyer Lab 
    !!Note as we have it in a container it needs to be a terminal in Jupyter, do not work from your local terminal!!
Install the required packages with pip install -r requirements.txt

### Start the REST API server 
As we are using docker we need to modify the run_server.sh file.
Therefore we need to integrate the --host=0.0.0.0 --port=5000 into the file.

Follow these steps to run the server locally
- Open a new terminal in Juptyer lab 
    !!Note as we have it in a container it needs to be a terminal in Jupyter, do not work from your local terminal!!
- Change into the rest-api directory: cd rest-api
Make the run_server.sh script exectuable: chmod +x run_server.sh
Start the server via ./run_server.sh

_______
You can check the server is running by point your browser at localhost:5000 which should return the page “BPTK-Py REST API Server”

### Test some queries
Test queries using the api-usage notebook

## Environment (`.env`)

This repository includes `.env_template` as an example. Before running `docker-compose`:

1. Copy the template to a local `.env` file in the same directory:

```bash
cp .env_template .env
```

2. Edit `.env` to set values appropriate for your host (container name, port mappings, and
     a host path for persistent data).

Important variables:
- `IMAGE_VERSION` — Docker image to use (default: `reineros4os/ssd-server:1`).
- `JUPYTER_PORT` — Host:container port mapping for Jupyter (e.g. `8012:8888`).
- `FLASK_PORT` — Host:container port mapping for the Flask API (e.g. `5000:5000`).
- `PATH_PERSISTENT_VOLUME` — Host path mounted into the container at `/home/jovyan/work/`.

Windows notes for `PATH_PERSISTENT_VOLUME`:
- With Docker Desktop on Windows, prefer a path under your user directory and ensure
    the drive is shared with Docker (e.g. `C:\Users\you\ssd-data`). Use forward slashes
    or escape backslashes in the `.env` file if needed. Example:

```dotenv
PATH_PERSISTENT_VOLUME=C:/Users/you/ssd-data
```

After updating `.env`, start the services with:

```bash
docker-compose up -d
```

To apply changes to `.env`, recreate containers with:

```bash
docker-compose down
docker-compose up -d --build
```