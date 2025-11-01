# Documentation
### High-level structure
- application.py is the Flask/BPTK entrypoint. It imports ScenarioClass, take_request (from maininteract), and bptk_factory (from food_security) and exposes /write_scenario, which forwards requests to take_request.
- maininteract.py orchestrates the flow: it imports ScenarioClass and many data-access functions from connectquery_db, builds a scenario JSON, and calls ScenarioClass.write_scenario(...).
- connectquery_db.py wraps SQLAlchemy/PostGIS queries (engine/session and many get_… helpers). It depends on local_settings.postgressql for DB credentials.
- food_security.py provides bptk_factory and the system-dynamics simulation_model used by BPTK_Py.
- scenarioclass.py defines ScenarioClass and write_scenario, which edits scenarios/scenarios.json.

### Internal dependencies (imports & calls)
- application → imports & calls: maininteract.take_request, imports: scenarioclass.ScenarioClass, food_security.bptk_factory.
- maininteract → imports: scenarioclass.ScenarioClass; imports & calls many functions from connectquery_db; calls ScenarioClass.write_scenario(...).
- connectquery_db → no project-internal imports; exports DB helpers.
- food_security → no project-internal imports; exports bptk_factory.
- scenarioclass → no project-internal imports.

### External libraries per module (non-exhaustive)
- application: BPTK_Py, Flask, flask_cors, markupsafe, json.
- maininteract: json, ast.
- connectquery_db: sqlalchemy, sqlalchemy_utils, pandas, local_settings.postgressql.
- food_security: numpy, scipy, BPTK_Py, math, logging, datetime, etc.
- scenarioclass: json.