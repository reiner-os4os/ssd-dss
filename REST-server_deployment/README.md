# Creation of a Docker image on which Conda QGIS, Jupyter Notebook and System Dynamics simulations run
**There are two ways to start the systemen**
1. Build your own image using the Dockerfile provided here
2. Use the already build image from docker hub https://hub.docker.com/u/reineros4os

**You can find following files in this folder:**
**Dockerfile** - Contains the logic and all the commands to assemble the image. <br>
**docker-compose_template.yml** - YAML file defining the services, networks, and volumes for the Docker application. To start the system by your own you should rename the  docker-compose_template.yml to docker-compose.yml and start it with docker-compose up<br>

## Build your own image
To build your own image you need to run the docker build command <br>
sudo docker build -< Dockerfile -t yourusername/qgisbptksd:1  <br>

## Use the already build image from docker hub
See here https://hub.docker.com/u/reineros4os

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

!!! The directory rest-api contains a simple REST API server for the [here the hello fod model will be integrated] using BPTK and Flask. 

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


# Building a docker image where Conda QGIS, Jupyter Notebook and System dynamics simulation is running 
sudo apt update
sudo apt install libgl1-mesa-glx
https://github.com/conda-forge/pygridgen-feedstock/issues/10