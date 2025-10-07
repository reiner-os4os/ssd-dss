# Documentation
Welcome, in this GitHub page you can find the code documentation of my Phd thesis. 
I tried to document as acurate as possible, in case you want to use the simulation models and you find in the documentation is something missing you can always conatct me.  this repository all necessary steps are documented to run the simulation models.
The focus of this thesis is on the modeling of sustainable food production in urban areas to evaluate food insecurity for vulnerable people. 
Methods of spatial analysis and simulation of dynamic interactions between actors are applied to answer the following research questions . 

RQ1: How can sustainable food production be quantified in cities and what variables have the main impact on production quantities?
RQ2: How do dietary choices impact the food production carbon footprint? 
RQ3: How can a system model be developed to describe the interdependencies of urban food production and policy changes to increase food security for vulnerable people.

The eaxmples provide a step by step how to create your own models and intergrate it into the simulation environment.

## Folder qgisbptksd
In this folder you can find the Dockerfile, docker-compose file and a documentaion on how to start and connect QGIS, the python based system dynamics environment BTPK and a jupyter notebook.

## Folder REST_API
In this folder you will find an example on how two modify the REST API example provided in the bptk_into.  

## Folder Data_analysis
Script to upload census data into PostGIS and create local .geojson

## run follwing commnads inside the container
cd work/bptk_intro
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## start jupyter notebook
pip install Flask-Cors 

## Foler Vensim_models
In this folder the Vensim models are stored 

## Relevant publications
More information on the motivation and background on why "I think" we need that kind of simulation environment please see following publications:

Jani, Anant; Exner, Andreas; Braun, Reiner; Braun, Brigitte; Torri, Luisa; Verhoeven, Sofie et al. (2022): Transitions to food democracy through multilevel governance. In: Frontiers in Sustainable Food Systems 6. DOI: 10.3389/fsufs.2022.1039127.

Braun, Reiner; Hertweck, Dieter; Eicker, Ursula (2022): An approach to cluster the research field of the food-energy-water nexus to determine modeling capabilities at different levels using text mining and cluster analysis. In: Energy Nexus, S. 100101. DOI: 10.1016/j.nexus.2022.100101.

Braun, Reiner; Padsala, Rushikesh; Malmir, Tahereh; Mohammadi, Soufia; Eicker, Ursula (2021): Using 3D CityGML for the Modeling of the Food Waste and Wastewater Generation-A Case Study for the City of Montréal. In: Frontiers in big data 4, S. 662011. DOI: 10.3389/fdata.2021.662011.

Eicker, Ursula; Weiler, Verena; Schumacher, Jürgen; Braun, Reiner (2020): On the design of an urban data and modeling platform and its application to urban district analyses. In: Energy and Buildings 217, S. 109954. DOI: 10.1016/j.enbuild.2020.109954.

A. D. M. Sawyer et al., "Dynamics of the complex food environment underlying dietary intake in low-income groups: a systems map of associations extracted from a systematic umbrella literature review," International Journal of Behavioral Nutrition and Physical Activity, vol. 18, no. 1, p. 96, 2021, doi: 10.1186/s12966-021-01164-1.
