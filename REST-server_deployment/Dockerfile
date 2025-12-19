# ================================================================================
# Dockerfile for SSD-DSS REST Server
# ================================================================================
# This Dockerfile creates a container image for running the SSD-DSS REST server
# with Jupyter notebook support and system dynamics modeling capabilities.
#
# Base Image: jupyter/base-notebook (includes Jupyter and Python)
# Python Version: 3.9
# Note: Python 3.10.9 is available but not currently used (see commented line below)
# ================================================================================

# Use Jupyter base notebook image with Python 3.9
#FROM jupyter/base-notebook:python-3.10.9
FROM jupyter/base-notebook:python-3.9

# Switch to root user to install system dependencies
USER root

# ================================================================================
# System Package Updates
# ================================================================================
# Update package manager repositories and upgrade existing packages
# -y flag: automatically answer "yes" to prompts without user interaction
RUN sudo apt-get update -y && sudo apt-get upgrade -y

# ================================================================================
# Python Package Manager Setup
# ================================================================================
# Upgrade pip to the latest version for better package installation reliability
RUN pip install --upgrade pip

# ================================================================================
# System Dynamics Modeling Dependencies
# ================================================================================
# Install BPTK-Py (Business Process Thinking Kit for Python)
# Version 1.9.0: Core library for system dynamics simulation and modeling
RUN pip install BPTK-Py==1.9.0

# ================================================================================
# REST API Framework Dependencies
# ================================================================================
# Flask-Cors 4.0.0: Enable Cross-Origin Resource Sharing for REST API endpoints
RUN pip install Flask-Cors==4.0.0

# Werkzeug 2.3.0: WSGI utility library for HTTP request/response handling
# Used as the underlying HTTP server for Flask applications
RUN pip install Werkzeug==2.3.0

# ================================================================================
# Geospatial & Database Dependencies
# ================================================================================
# These packages enable interaction with PostGIS (PostgreSQL spatial database)
# and support SQL-based queries from Jupyter notebooks

# GeoAlchemy2 0.15.1: SQLAlchemy extension for spatial databases
# Provides ORM support for geographic data types (geometry, geography)
RUN pip install GeoAlchemy2==0.15.1

# SQLAlchemy 1.4.41: Python ORM (Object-Relational Mapping) library
# Enables database abstraction and query building across different database systems
RUN pip install sqlalchemy==1.4.41

# SQLAlchemy-Utils 0.41.2: Utility functions and data types for SQLAlchemy
# Provides additional functionality like JSON types and validators
RUN pip install SQLAlchemy-Utils==0.41.2

# ipython-sql 0.5.0: IPython magic commands for SQL queries
# Allows running raw SQL queries directly in Jupyter notebook cells using %%sql syntax
RUN pip install ipython-sql==0.5.0
