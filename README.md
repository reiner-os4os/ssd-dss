# ssd-dss — System Dynamics & Decision Support for Sustainable Food Systems ✅

This repository contains code, models, and example notebooks developed as part of work on modeling sustainable urban food production and food security. Below is a concise description of what you'll find in the top-level folders and what to expect when exploring the project.

---

## Repository structure & what to expect 📁

- **`Jupyter_notebooks/`** 🔬
	- Contains exploratory and reproducible notebooks used for data analysis and visualisation.
	- **`Food_establishments/`**: example notebooks such as `Food_establishments.ipynb`, `Food_establishments_simple_analysis.ipynb`, and `Food_establishments_time_analysis.ipynb` with analyses of food establishment datasets, temporal trends, and example plots.

- **`REST-server_deployment/`** 🚀
	- Infrastructure for deploying a lightweight REST service used to serve or collect simulation data.
	- Includes `docker-compose.yml`, `Dockerfile`, and a small `README.md` with instructions for building and running the containerised service.

- **`SSD_model_library/`** 📦
	- Library of system dynamics models used in the project (model files and variants).
	- Examples: `food_security.xmile`, `food_security47.mdl` (model definitions that can be loaded by standard SD tools that support XMILE/Vensim formats).

- **`SSD_run_simulation/`** ▶️
	- Notebooks to run simulations and inspect outputs.
	- Key files: `Run_simulation.ipynb` (run scenarios), `Analyse_simulation.ipynb` (summary statistics and diagnostics), `Szenario_plot.ipynb` (visualize scenario outcomes).

- **`SSD_simualtion_core/`** ⚙️
	- Core application scripts and utilities powering simulations and integrations.
	- Typical files: `application.py` (application entrypoint or REST app), `connectquery_db.py` (database helpers), `maininteract.py` (interactive runner), `scenarioclass.py` (scenario abstractions), plus a small `README.md` with implementation notes.
	- Note: folder name contains a typo (`simualtion`) — keep this in mind when navigating or scripting paths.

- **Root files** 📄
	- `LICENSE` — project license
	- This top-level `README.md` — overview and pointers

---

## Getting started — quick pointers 💡

- To run example analyses, open the notebooks in `Jupyter_notebooks/` or `SSD_run_simulation/` with JupyterLab or Jupyter Notebook.
- To deploy the REST service, follow the instructions in `REST-server_deployment/` (build the Docker image and run `docker-compose up`).
- For model editing or inspection, open the files in `SSD_model_library/` with a compatible system-dynamics tool (XMILE/Vensim-compatible editors).
- See `SSD_simualtion_core/README.md` for details on running the core application and database connections.

**Contact / issues:** If anything is missing or unclear, please open an issue or contact the repository owner for details.

