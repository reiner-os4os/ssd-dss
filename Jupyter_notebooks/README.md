# ssd-jupyter — A collection of Jupyter notebooks to analyse the data sets ✅

This folder contains Jupyter notebooks used for geospatial data analysis and for uploading selected datasets to a PostGIS database. The notebooks target datasets provided by the City of Montréal and Statistics Canada and include exploratory analysis, data cleaning, translations/mappings, and scripts to push data into PostGIS.

**Quick structure**
- **Census_to_PostGIS/** — Notebooks and helper scripts to prepare and upload census tract data to PostGIS.
- **Food_aid_requests/** — Notebooks analysing requests for food aid (211 dataset): requests, follow-ups, needs and business linkage.
- **Food_establishments/** — Notebooks analysing City of Montréal food-establishment data (shapefile/csv/geojson).

**Notebooks (short descriptions)**
- `Census_to_POSTGIS/Census_select_data.ipynb`: Basic script to load census tract shapes and census variables (merge by DGUID), export GeoJSON and upload selected tables to a PostGIS database.
- `Census_to_POSTGIS/census_select.py`: Helper functions used by the census notebook to select and prepare variables.
- `Census_to_POSTGIS/libraries.txt`: List of libraries used/required for the census workflow.

- `Food_aid_requests/Food_aid_request.ipynb`: Main analysis of 211 food-aid requests for 2021–2022 — loads requests, follow-ups, needs and performs exploratory analysis and visualisations.
- `Food_aid_requests/Food_aid_request_age_analysis.ipynb`: Aggregation and mapping of median age (requests grouped by borough) and related figures.
- `Food_aid_requests/Food_aid_request_businesses.ipynb`: Links 211 requests to nearby food establishments and performs spatial analyses.
- `Food_aid_requests/Food_aid_request_follow_up.ipynb`: Processes follow‑up records (translations and cleaning) and inspects follow-up outcomes.
- `Food_aid_requests/Food_aid_request_needs.ipynb`: Analyses the 'needs' dataset (requested supports / resources) from 211.

- `Food_establishments/Food_establishments.ipynb`: Full analysis of food establishments dataset (geospatial and attribute exploration, clustering, maps).
- `Food_establishments/Food_establishments_simple_analysis.ipynb`: Lightweight exploratory analysis and counts by category.
- `Food_establishments/Food_establishments_time_analysis.ipynb`: Time-based / temporal analysis and translation/mapping of categories.

**Getting started**
Ensure the project `Data` folder is available and contains the expected datasets (CSV, shapefiles, GeoJSON). Many notebooks expect a base data path environment variable named `Data_folder`.

**Notes & tips**
- Many notebooks contain code to set `folder_path = "/home/jovyan/work/Data/"` — replace that with the `Data_folder` path (or set the env var) when running locally.
- Some source files / datasets come in English (`*_EN.csv`) and French. Notebooks sometimes use the English files; check file names in the first code cells before running.
- `Census_to_POSTGIS` uses a small helper script (`census_select.py`) and requires a PostGIS connection; configure DB credentials in the notebook or in a `config.py` following existing patterns.