#FROM jupyter/base-notebook:python-3.10.9
FROM jupyter/base-notebook:python-3.9
USER root
# Update and upgrade the system, -y option is used for automatic execution
# the user will not asked for response
RUN sudo apt-get update -y && sudo apt-get upgrade -y

# 
RUN pip install --upgrade pip

# Install the BPTK-Py python libraries
RUN pip install BPTK-Py==1.9.0
RUN pip install Flask-Cors==4.0.0
RUN pip install Werkzeug==2.3.0

# Install GeaoAlchemy, sqlalchemy and nipython-sql needed to work with POSTGIS database
RUN pip install GeoAlchemy2==0.15.1
RUN pip install sqlalchemy==1.4.41
RUN pip install SQLAlchemy-Utils==0.41.2
RUN pip install ipython-sql==0.5.0

# failed, check version number RUN pip install psycopg2==2.9.9
#USER 1001

# Delete later, not needed for the REST server
# Install the libgl1-mesa-glx library, this is needed to start QGIS from Jupyter
# also here -y command is required
#RUN sudo apt install -y libgl1-mesa-glx
# Install QGIS from conda-forge, see https://anaconda.org/conda-forge/qgis
#RUN conda install -c conda-forge qgis=3.22.16
# Path for python 3.10.9
#RUN conda develop -n base ['/opt/conda/share/qgis/python', '/home/jovyan/.local/share/QGIS/QGIS3/profiles/default/python', '/home/jovyan/.local/share/QGIS/QGIS3/profiles/default/python/plugins', '/opt/conda/share/qgis/python/plugins', '/opt/conda/share/qgis/python/plugins', '/opt/conda/share/qgis/python', '/home/jovyan/work', '/opt/conda/lib/python310.zip', '/opt/conda/lib/python3.10', '/opt/conda/lib/python3.10/lib-dynload', '/opt/conda/lib/python3.10/site-packages', '/home/jovyan/.local/share/QGIS/QGIS3/profiles/default/python']
# Path for python 3.9
#RUN conda develop -n base ['/opt/conda/share/qgis/python', '/home/jovyan/.local/share/QGIS/QGIS3/profiles/default/python', '/home/jovyan/.local/share/QGIS/QGIS3/profiles/default/python/plugins', '/opt/conda/share/qgis/python/plugins', '/opt/conda/share/qgis/python/plugins', '/opt/conda/share/qgis/python', '/home/jovyan', '/opt/conda/lib/python39.zip', '/opt/conda/lib/python3.9', '/opt/conda/lib/python3.9/lib-dynload', '/opt/conda/lib/python3.9/site-packages', '/home/jovyan/.local/share/QGIS/QGIS3/profiles/default/python']

# Install pandas, see https://pypi.org/project/pandas/
#RUN pip install pandas==2.1.3
# Install geopandas from conda-forge, see https://anaconda.org/conda-forge/geopandas
#RUN conda install -c conda-forge geopandas==0.14.2
# Install python modules required for GIS work
# see https://anaconda.org/conda-forge/contextily
#RUN conda install -c conda-forge contextily==1.4.0
# see https://anaconda.org/anaconda/openpyxl
#RUN conda install -c conda-forge openpyxl==3.0.10
# see https://anaconda.org/conda-forge/ipyleaflet
#RUN conda install -c conda-forge ipyleaflet==0.17.4
# see https://anaconda.org/conda-forge/osmnx
#RUN conda install -c conda-forge osmnx=1.7.1
# see https://anaconda.org/conda-forge/descartes
#RUN conda install -c conda-forge descartes==1.1.0
# see https://anaconda.org/anaconda/seaborn
#RUN conda install -c anaconda seaborn=0.12.2
#RUN conda install -y conda-build -c conda-forge