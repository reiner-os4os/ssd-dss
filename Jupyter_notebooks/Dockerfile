# ================================================================================
# Dockerfile for JupyterLab + Python 3.9.13 + main libs (conda + pip)
# Base: jupyter/base-notebook:python-3.9 (includes conda at /opt/conda)
# ================================================================================

FROM jupyter/base-notebook:python-3.9
# Switch to root for apt installs
USER root

RUN sudo apt-get update -y && sudo apt-get upgrade -y

# 
RUN pip install --upgrade pip

# Install GeaoAlchemy, sqlalchemy and nipython-sql needed to work with POSTGIS database
# see https://pypi.org/project/GeoAlchemy2/0.15.1/
RUN pip install GeoAlchemy2==0.15.1

RUN pip install sqlalchemy==1.4.41
RUN pip install SQLAlchemy-Utils==0.41.2
RUN pip install ipython-sql==0.5.0


# Install pandas, see https://pypi.org/project/pandas/
RUN pip install pandas==2.1.3
# Install geopandas from conda-forge, see https://anaconda.org/conda-forge/geopandas
RUN conda install -c conda-forge geopandas==0.14.2
# Install python modules required for GIS work
# see https://anaconda.org/conda-forge/contextily
RUN conda install -c conda-forge contextily==1.4.0
# see https://anaconda.org/anaconda/openpyxl
RUN conda install -c conda-forge openpyxl==3.0.10
# see https://anaconda.org/conda-forge/ipyleaflet
RUN conda install -c conda-forge ipyleaflet==0.17.4
# see https://anaconda.org/conda-forge/osmnx
RUN conda install -c conda-forge osmnx=1.7.1
# see https://anaconda.org/conda-forge/descartes
RUN conda install -c conda-forge descartes==1.1.0
# see https://anaconda.org/anaconda/seaborn
RUN conda install -c anaconda seaborn=0.12.2
RUN conda install -y conda-build -c conda-forge