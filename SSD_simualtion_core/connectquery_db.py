from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists
from local_settings import postgressql as settings
import pandas as pd

# see following video https://www.youtube.com/watch?v=neW9Y9xh4jc
# https://www.youtube.com/watch?v=OLsVfmjEpSc

def get_engine(db_username, db_password, db_host, db_port, db_name):
    """
    Create engine, take the data base username, password, host,
    port and name as input.
    Return the engine information back.
    Please check the credetials in the local_settings.py 
    """
    url = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
    if not database_exists(url):
        raise Exception('No database exists, check if database is running.')
    engine = create_engine(url)
    return engine

def engine_connect(inengine, sql, num_value):
    """
    Using engine connection and executing the query with the parameter
    """
    with inengine.connect() as conn:
        result = conn.execute(text(sql), {"num_value": num_value})
        # Fetch all rows from the result
        result_list = result.fetchall()
        # Get the column names from the result
        columns = result.keys()
        # Convert the result list into a DataFrame
        df_result = pd.DataFrame(result_list, columns=columns)
        # Return the DataFrame
        return df_result

def get_engine_from_settings():
    """
    Check if all key are provided in the settings file, if all is ok 
    start the get_engine function with the credetials provided in the settings file, 
    else excetion Bad config file.
    !!!Exception does not work jet properly need to be checked in detail!!!
    """
    keys = ['db_username', 'db_password', 'db_host', 'db_port', 'db_name']
    if not all (key in keys for key in settings.keys()):
        raise Exception('Bad config file')
    
    return get_engine(settings['db_username'],
                    settings['db_password'],
                    settings['db_host'],
                    settings['db_port'],
                    settings['db_name']
                    )

def get_session():
    """
    Include comments, documentation here. get_session function
    """
    engine = get_engine_from_settings()
    session = sessionmaker(bind=engine)()
    # return engine, session
    return engine

def get_Area(inengine, num_value):
    """
    To avoid any conflicts later with the area calculation, the area in the data base should be the same as used in the SD model
    Task update the borough table with an extra entry area in km²
    """
    sql = '''
        WITH borough_geom AS (
        SELECT ST_Union(geometry) AS geom
        FROM public.boroughs
        WHERE "NUM" = :num_value
        )
        SELECT
        SUM(
            ct."LANDAREA" *
            (ST_Area(ST_Intersection(ct.geometry, b.geom)) / NULLIF(ST_Area(ct.geometry), 0))
        ) AS area_km2
        FROM public.census_tracks ct
        JOIN borough_geom b
        ON ST_Intersects(ct.geometry, b.geom);
    '''
    df_result = engine_connect(inengine, sql, num_value)
    return df_result


def get_ResidentialArea(inengine, num_value):
    """
    To avoid any conflicts later with the area calculation, the area in the data base should be the same as used in the SD model
    Task update the borough table with an extra entry area in km²
    """
    sql = '''
        WITH borough_geom AS (
            SELECT ST_Union(geometry) AS geom
            FROM public.boroughs
            WHERE "NUM" = :num_value
        )
        SELECT 
            SUM(
                ST_Area(
                    ST_Transform(
                        ST_Intersection(ct.geometry, b.geom),
                        32618
                    )
                ) / 1000000
            ) AS area_km2
        FROM public.osm_landuse ct
        JOIN borough_geom b
            ON ST_Intersects(ct.geometry, b.geom)
        WHERE ct.fclass = 'residential';
    '''
    df_result = engine_connect(inengine, sql, num_value)
    return df_result


def get_IniFastFoodOutlet(inengine, num_value):
    """
    Include comments, documentation here. get_IniFastFoodOutlet function
    """
    sql = '''
        SELECT COUNT(*) 
        FROM public.businesses bus
        JOIN public.boroughs bor 
        ON ST_Intersects(bus.geometry, bor.geometry)
        WHERE bor."NUM" = :num_value
        AND bus.kategorie = 'fast_food_outlet';
    '''
    df_result = engine_connect(inengine, sql, num_value)
    return df_result


def get_IniSupermarkets(inengine, num_value):
    """
    Include comments, documentation here. get_IniSupermarkets function
    """
    sql = '''
        SELECT COUNT(*) 
        FROM public.businesses bus
        JOIN public.boroughs bor 
        ON ST_Intersects(bus.geometry, bor.geometry)
        WHERE bor."NUM" = :num_value
        AND bus.kategorie = 'supermarket';
    '''
    df_result = engine_connect(inengine, sql, num_value)
    return df_result

def get_IniHealthyFoodStore(inengine, num_value):
    """
    Include comments, documentation here. get_IniHealthyFoodStore function
    """
    sql = '''
        SELECT COUNT(*) 
        FROM public.businesses bus
        JOIN public.boroughs bor 
        ON ST_Intersects(bus.geometry, bor.geometry)
        WHERE bor."NUM" = :num_value
        AND bus.kategorie = 'healthy_food_store';
    '''
    df_result = engine_connect(inengine, sql, num_value)
    return df_result
    
def get_IniPublicTransportStation(inengine, num_value):
    """
    Include comments, documentation here. get_IniPublicTransportStation function
    """
    sql = '''
        SELECT COUNT(*)
        FROM public.transport_point po
        JOIN public.boroughs bor
        ON ST_Intersects(po.geometry, bor.geometry)
        WHERE bor."NUM" = :num_value
        AND po.fclass IN ('bus_stop', 'bus_station', 'railway_station');
    '''
    df_result = engine_connect(inengine, sql, num_value)
    return df_result

def get_IniShelterCostsLessThan30Percent(inengine, num_value):
    sql = '''
        WITH borough_geom AS (
          SELECT ST_Union(geometry) AS geom
          FROM public.boroughs
          WHERE "NUM" = :num_value
        )

        SELECT
          COALESCE(
            SUM(cs."C1_COUNT_TOTAL" *
              (ST_Area(ST_Intersection(cs.geometry, b.geom)) / NULLIF(ST_Area(cs.geometry), 0))
            ),
            0
          ) AS count
        FROM public.census_shelter_cost cs
        JOIN borough_geom b ON ST_Intersects(cs.geometry, b.geom)
        WHERE cs."CHARACTERISTIC_NAME" = '  Spending less than 30% of income on shelter costs';
    '''
    df_result = engine_connect(inengine, sql, num_value)
    return df_result

def get_IniShelterCostsMore30Percent(inengine, num_value):
    sql = '''
        WITH borough_geom AS (
          SELECT ST_Union(geometry) AS geom
          FROM public.boroughs
          WHERE "NUM" = :num_value
        )

        SELECT
          COALESCE(
            SUM(cs."C1_COUNT_TOTAL" *
              (ST_Area(ST_Intersection(cs.geometry, b.geom)) / NULLIF(ST_Area(cs.geometry), 0))
            ),
            0
          ) AS count
        FROM public.census_shelter_cost cs
        JOIN borough_geom b ON ST_Intersects(cs.geometry, b.geom)
        WHERE cs."CHARACTERISTIC_NAME" = '  Spending 30% or more of income on shelter costs';
    '''
    df_result = engine_connect(inengine, sql, num_value)
    return df_result

def get_IniCoupleWithoutChildren(inengine, num_value):
    """
    Function in the connectquery_db.py
    Include comments, documentation here. get_IniFastFoodOutlet function
    """
    sql = '''
        WITH borough_geom AS (
        SELECT ST_Union(geometry) AS geom
        FROM public.boroughs
        WHERE "NUM" = :num_value
        )

        SELECT
        COALESCE(
            SUM(cs."C1_COUNT_TOTAL" *
            (ST_Area(ST_Intersection(cs.geometry, b.geom)) / NULLIF(ST_Area(cs.geometry), 0))
            ),
            0
        ) AS count
        FROM public.census_household_type cs
        JOIN borough_geom b ON ST_Intersects(cs.geometry, b.geom)
        WHERE cs."CHARACTERISTIC_NAME" = '      Without children';
    '''
    df_result = engine_connect(inengine, sql, num_value)
    return df_result

def get_IniTwoParent(inengine, num_value):
    """
    Function in the connectquery_db.py
    Include comments, documentation here. get_IniFastFoodOutlet function
    """
    sql = '''
        WITH borough_geom AS (
        SELECT ST_Union(geometry) AS geom
        FROM public.boroughs
        WHERE "NUM" = :num_value
        )

        SELECT
        COALESCE(
            SUM(cs."C1_COUNT_TOTAL" *
            (ST_Area(ST_Intersection(cs.geometry, b.geom)) / NULLIF(ST_Area(cs.geometry), 0))
            ),
            0
        ) AS count
        FROM public.census_household_type cs
        JOIN borough_geom b ON ST_Intersects(cs.geometry, b.geom)
        WHERE cs."CHARACTERISTIC_NAME" = '      With children';
    '''
    df_result = engine_connect(inengine, sql, num_value)
    return df_result

def get_IniSingleParent(inengine, num_value):
    """
    Function in the connectquery_db.py
    Include comments, documentation here. get_IniFastFoodOutlet function
    """
    sql = '''
        WITH borough_geom AS (
        SELECT ST_Union(geometry) AS geom
        FROM public.boroughs
        WHERE "NUM" = :num_value
        )

        SELECT
        COALESCE(
            SUM(cs."C1_COUNT_TOTAL" *
            (ST_Area(ST_Intersection(cs.geometry, b.geom)) / NULLIF(ST_Area(cs.geometry), 0))
            ),
            0
        ) AS count
        FROM public.census_household_type cs
        JOIN borough_geom b ON ST_Intersects(cs.geometry, b.geom)
        WHERE cs."CHARACTERISTIC_NAME" = '    One-parent-family households';
    '''
    df_result = engine_connect(inengine, sql, num_value)
    return df_result

def get_IniMultigenerational(inengine, num_value):
    """
    Function in the connectquery_db.py
    Include comments, documentation here. get_IniFastFoodOutlet function
    """
    sql = '''
        WITH borough_geom AS (
        SELECT ST_Union(geometry) AS geom
        FROM public.boroughs
        WHERE "NUM" = :num_value
        )

        SELECT
        COALESCE(
            SUM(cs."C1_COUNT_TOTAL" *
            (ST_Area(ST_Intersection(cs.geometry, b.geom)) / NULLIF(ST_Area(cs.geometry), 0))
            ),
            0
        ) AS count
        FROM public.census_household_type cs
        JOIN borough_geom b ON ST_Intersects(cs.geometry, b.geom)
        WHERE cs."CHARACTERISTIC_NAME" = '  Multigenerational households';
    '''
    df_result = engine_connect(inengine, sql, num_value)
    return df_result

def get_IniSinglePersonLivingAlone(inengine, num_value):
    """
    Function in the connectquery_db.py
    Include comments, documentation here. get_IniFastFoodOutlet function
    """
    sql = '''    
        WITH borough_geom AS (
        SELECT ST_Union(geometry) AS geom
        FROM public.boroughs
        WHERE "NUM" = :num_value
        )

        SELECT
        COALESCE(
            SUM(cs."C1_COUNT_TOTAL" *
            (ST_Area(ST_Intersection(cs.geometry, b.geom)) / NULLIF(ST_Area(cs.geometry), 0))
            ),
            0
        ) AS count
        FROM public.census_household_type cs
        JOIN borough_geom b ON ST_Intersects(cs.geometry, b.geom)
        WHERE cs."CHARACTERISTIC_NAME" = '  One-person households';
    '''
    df_result = engine_connect(inengine, sql, num_value)
    return df_result

def get_IniTotalHouseholdTypes(inengine, num_value):
    """
    Function in the connectquery_db.py
    Include comments, documentation here. get_IniFastFoodOutlet function
    """
    sql = '''
        WITH borough_geom AS (
        SELECT ST_Union(geometry) AS geom
        FROM public.boroughs
        WHERE "NUM" = :num_value
        )

        SELECT
        COALESCE(
            SUM(cs."C1_COUNT_TOTAL" *
            (ST_Area(ST_Intersection(cs.geometry, b.geom)) / NULLIF(ST_Area(cs.geometry), 0))
            ),
            0
        ) AS count
        FROM public.census_household_type cs
        JOIN borough_geom b ON ST_Intersects(cs.geometry, b.geom)
        WHERE cs."CHARACTERISTIC_NAME" = 'Total - Household type - 100% data';
    '''
    df_result = engine_connect(inengine, sql, num_value)
    return df_result

def get_IniTotalPrivateRentalMarket(inengine, num_value):
    """
    Function in the connectquery_db.py
    Include comments, documentation here. get_IniFastFoodOutlet function
    initialTotalPrivateRentalMarket
    """
    sql = '''
        WITH borough_geom AS (
        SELECT ST_Union(geometry) AS geom
        FROM public.boroughs
        WHERE "NUM" = :num_value
        )

        SELECT
        COALESCE(
            SUM(cs."C1_COUNT_TOTAL" *
            (ST_Area(ST_Intersection(cs.geometry, b.geom)) / NULLIF(ST_Area(cs.geometry), 0))
            ),
            0
        ) AS count
        FROM public.census_housing_situation cs
        JOIN borough_geom b ON ST_Intersects(cs.geometry, b.geom)
        WHERE cs."CHARACTERISTIC_NAME" = 'Total - Tenant households in non-farm, non-reserve private dwellings - 25% sample data';
    '''
    df_result = engine_connect(inengine, sql, num_value)
    return df_result

def get_IniOwner(inengine, num_value):
    """
    Function in the connectquery_db.py
    Include comments, documentation here. get_IniFastFoodOutlet function
    initialOwner
    """
    sql = '''
        WITH borough_geom AS (
        SELECT ST_Union(geometry) AS geom
        FROM public.boroughs
        WHERE "NUM" = :num_value
        )

        SELECT
        COALESCE(
            SUM(cs."C1_COUNT_TOTAL" *
            (ST_Area(ST_Intersection(cs.geometry, b.geom)) / NULLIF(ST_Area(cs.geometry), 0))
            ),
            0
        ) AS count
        FROM public.census_housing_situation cs
        JOIN borough_geom b ON ST_Intersects(cs.geometry, b.geom)
        WHERE cs."CHARACTERISTIC_NAME" = 'Total - Owner households in non-farm, non-reserve private dwellings - 25% sample data';
    '''
    df_result = engine_connect(inengine, sql, num_value)
    return df_result

def get_InipercentOfTenantHouseholdsInSubsidizedHousing(inengine, num_value):
    """
    Function in the connectquery_db.py
    Include comments, documentation here. get_IniFastFoodOutlet function
    percentOfTenantHouseholdsInSubsidizedHousing
    """
    sql = '''
        WITH borough_geom AS (
        SELECT ST_Union(geometry) AS geom
        FROM public.boroughs
        WHERE "NUM" = :num_value
        )

        SELECT
        COALESCE(
            AVG(cs."C1_COUNT_TOTAL" *
            ((ST_Area(ST_Intersection(cs.geometry, b.geom))/100) / NULLIF(ST_Area(cs.geometry), 0))
            ),
            0
        ) AS mean_percent
        FROM public.census_housing_situation cs
        JOIN borough_geom b ON ST_Intersects(cs.geometry, b.geom)
        WHERE cs."CHARACTERISTIC_NAME" = '  % of tenant households in subsidized housing';
    '''
    df_result = engine_connect(inengine, sql, num_value)
    return df_result

def get_IniTotalImmigrationStatus(inengine, num_value):
    """
    Function in the connectquery_db.py
    Include comments, documentation here. get_IniFastFoodOutlet function
    initialTotalImmigrationStatus
    """
    sql = '''
        WITH borough_geom AS (
        SELECT ST_Union(geometry) AS geom
        FROM public.boroughs
        WHERE "NUM" = :num_value
        )

        SELECT
        COALESCE(
            SUM(cs."C1_COUNT_TOTAL" *
            (ST_Area(ST_Intersection(cs.geometry, b.geom)) / NULLIF(ST_Area(cs.geometry), 0))
            ),
            0
        ) AS count
        FROM public.cencus_immigtant_status cs
        JOIN borough_geom b ON ST_Intersects(cs.geometry, b.geom)
        WHERE cs."CHARACTERISTIC_NAME" = 'Total - Immigrant status and period of immigration for the population in private households - 25% sample data';
    '''
    df_result = engine_connect(inengine, sql, num_value)
    return df_result

def get_IniNonImmigrants(inengine, num_value):
    """
    Function in the connectquery_db.py
    Include comments, documentation here. get_IniFastFoodOutlet function
    initialNonImmigrants
    """
    sql = '''
        WITH borough_geom AS (
        SELECT ST_Union(geometry) AS geom
        FROM public.boroughs
        WHERE "NUM" = :num_value
        )

        SELECT
        COALESCE(
            SUM(cs."C1_COUNT_TOTAL" *
            (ST_Area(ST_Intersection(cs.geometry, b.geom)) / NULLIF(ST_Area(cs.geometry), 0))
            ),
            0
        ) AS count
        FROM public.cencus_immigtant_status cs
        JOIN borough_geom b ON ST_Intersects(cs.geometry, b.geom)
        WHERE cs."CHARACTERISTIC_NAME" = '  Non-immigrants';
    '''
    df_result = engine_connect(inengine, sql, num_value)
    return df_result

def get_IniImmigrants(inengine, num_value):
    """
    Function in the connectquery_db.py
    Include comments, documentation here. get_IniFastFoodOutlet function
    initialImmigrants
    """
    sql = '''
        WITH borough_geom AS (
        SELECT ST_Union(geometry) AS geom
        FROM public.boroughs
        WHERE "NUM" = :num_value
        )

        SELECT
        COALESCE(
            SUM(cs."C1_COUNT_TOTAL" *
            (ST_Area(ST_Intersection(cs.geometry, b.geom)) / NULLIF(ST_Area(cs.geometry), 0))
            ),
            0
        ) AS count
        FROM public.cencus_immigtant_status cs
        JOIN borough_geom b ON ST_Intersects(cs.geometry, b.geom)
        WHERE cs."CHARACTERISTIC_NAME" = '  Immigrants';
    '''
    df_result = engine_connect(inengine, sql, num_value)
    return df_result

def get_NonPermanentResidents(inengine, num_value):
    """
    Function in the connectquery_db.py
    Include comments, documentation here. get_IniFastFoodOutlet function
    initialNonPermanentResidents
    """
    sql = '''
        WITH borough_geom AS (
        SELECT ST_Union(geometry) AS geom
        FROM public.boroughs
        WHERE "NUM" = :num_value
        )

        SELECT
        COALESCE(
            SUM(cs."C1_COUNT_TOTAL" *
            (ST_Area(ST_Intersection(cs.geometry, b.geom)) / NULLIF(ST_Area(cs.geometry), 0))
            ),
            0
        ) AS count
        FROM public.cencus_immigtant_status cs
        JOIN borough_geom b ON ST_Intersects(cs.geometry, b.geom)
        WHERE cs."CHARACTERISTIC_NAME" = '  Non-permanent residents';
    '''
    df_result = engine_connect(inengine, sql, num_value)
    return df_result