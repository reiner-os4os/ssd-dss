# SSD-DSS REST Server Deployment

A Docker-based deployment for the System Dynamics Simulation - Decision Support System (SSD-DSS) with Jupyter Notebook and REST API server capabilities.

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
| **.env_template** | Environment configuration (container name, ports, volume paths) |

## Building Your Own Image

To build a custom image, run:

```bash
docker build -f Dockerfile -t yourname/ssd-server:1 .
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