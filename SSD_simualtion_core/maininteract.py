import json
import ast
from scenarioclass import ScenarioClass
# from connectquery_db import get_session, get_Area, get_IniHealthyFoodStore, get_IniSupermarkets, get_IniFastFoodOutlet, get_IniPublicTransportStation 

from connectquery_db import (
    get_session,
    get_Area,
    get_IniHealthyFoodStore,
    get_IniSupermarkets,
    get_IniFastFoodOutlet,
    get_IniPublicTransportStation,
    get_IniShelterCostsLessThan30Percent,
    get_IniShelterCostsMore30Percent,
    get_ResidentialArea,
    get_IniCoupleWithoutChildren,
    get_IniTwoParent,
    get_IniSingleParent,
    get_IniMultigenerational,
    get_IniSinglePersonLivingAlone,
    get_IniTotalHouseholdTypes,
    get_IniTotalPrivateRentalMarket,
    get_IniOwner,
    get_InipercentOfTenantHouseholdsInSubsidizedHousing,
    get_IniTotalImmigrationStatus,
    get_IniNonImmigrants,
    get_IniImmigrants,
    get_NonPermanentResidents # your new function
)


def custom_decoder(dct):
    """
    Include comments, documentation here. custom_decoder function
    """
    return ScenarioClass(**dct)

def take_request(request):
    """
    Include comments, documentation here. take_request function
    """
    session = get_session()  
    # Convert the request into a dict, the dict values are used to write directly into the scenario file  
    data_dict = ast.literal_eval(request)
    borough_name = data_dict['borough_name']
    newBuildRateSupermarketAndHealthyFoodStore = data_dict['newBuildRateSupermarketAndHealthyFoodStore']
    newBuildRateFastFoodOutlet = data_dict['newBuildRateFastFoodOutlet']
    newBuildRatePublicTransport = data_dict['newBuildRatePublicTransport']
    newBuildRateUrbanFarmsCg = data_dict['newBuildRateUrbanFarmsCg']
    optimalPublicTransportStationDensity = data_dict['optimalPublicTransportStationDensity']
    negativePerceptionsOfLocalArea = data_dict['negativePerceptionsOfLocalArea']
    residentialOrGeographicalSegregation = data_dict['residentialOrGeographicalSegregation']
    costsPublicTransportUse = data_dict['costsPublicTransportUse']
    costsIndividualVehicleUse = data_dict['costsIndividualVehicleUse']
    openingHoursOfSupermarketsDailyStores = data_dict['openingHoursOfSupermarketsDailyStores']
    optimalProductionDensity = data_dict['optimalProductionDensity']
    reductionInShelterCosts = data_dict['reductionInShelterCosts']
    
    

    # Parse the JSON string, used for the POSTGIS query with NUM the number of the borough 
    data = json.loads(request)
    
    # area in km2 is the field from the POSTGIS 
    Area = get_Area(session, data['NUM'])
    localArea = Area['area_km2'][0]
    
    # residential area in km2 is the field from the POSTGIS residentialArea
    ResidentialArea = get_ResidentialArea(session, data['NUM'])
    localResidentialArea = ResidentialArea['area_km2'][0]
    
    # count is the field from the POSTGIS
    IniHealthyFoodStore = get_IniHealthyFoodStore(session, data['NUM'])
    localIniHealthyFoodStore = IniHealthyFoodStore['count'][0]
    
    # count is the field from the POSTGIS
    IniSupermarkets = get_IniSupermarkets(session, data['NUM'])
    localIniSupermarkets = IniSupermarkets['count'][0]
    
    # count is the field from the POSTGIS
    IniFastFoodOutlet = get_IniFastFoodOutlet(session, data['NUM'])
    localIniFastFoodOutlet = IniFastFoodOutlet['count'][0]

    # Get the number of public transport staions, count is the field from the POSTGIS
    IniPublicTransportStation = get_IniPublicTransportStation(session, data['NUM'])
    localIniPublicTransportStation = IniPublicTransportStation['count'][0]
    
    # Get the sum of the people living in households spending less then 30% of income on shelter costs', count is the field from the POSTGIS
    IniShelterCostsLessThan30Percent = get_IniShelterCostsLessThan30Percent(session, data['NUM'])
    localIniShelterCostsLessThan30Percent = IniShelterCostsLessThan30Percent['count'][0]
    
    # Get the sum of the people living in households spending less then 30% of income on shelter costs', count is the field from the POSTGIS
    IniShelterCostsMore30Percent = get_IniShelterCostsMore30Percent(session, data['NUM'])
    localIniShelterCostsMore30Percent = IniShelterCostsMore30Percent['count'][0]

    # Get the sum of the households whith couples without children, count is the field from the POSTGIS
    IniCoupleWithoutChildren = get_IniCoupleWithoutChildren(session, data['NUM'])
    localIniCoupleWithoutChildren = IniCoupleWithoutChildren['count'][0]
    
    # Get the sum of the households whith couples with children, count is the field from the POSTGIS
    IniTwoParent = get_IniTwoParent(session, data['NUM'])
    localIniTwoParent = IniTwoParent['count'][0]
    
    # Get the sum of the households whith One-parent-family, count is the field from the POSTGIS
    IniSingleParent = get_IniSingleParent(session, data['NUM'])
    localIniSingleParent = IniSingleParent['count'][0]    
    
    # Get the sum of the households whith Multigenerational, count is the field from the POSTGIS
    IniMultigenerational = get_IniMultigenerational(session, data['NUM'])
    localIniMultigenerational = IniMultigenerational['count'][0]        

    # Get the sum of the households whith One-person, count is the field from the POSTGIS
    IniSinglePersonLivingAlone = get_IniSinglePersonLivingAlone(session, data['NUM'])
    localIniSinglePersonLivingAlone = IniSinglePersonLivingAlone['count'][0]
    
    # Get the sum of the households whith One-person, count is the field from the POSTGIS
    IniTotalHouseholdTypes = get_IniTotalHouseholdTypes(session, data['NUM'])
    localIniTotalHouseholdTypes = IniTotalHouseholdTypes['count'][0]
    
    # Get the sum of thetenant households in non-farm, non-reserve private dwellings, count is the field from the POSTGIS
    IniTotalPrivateRentalMarket = get_IniTotalPrivateRentalMarket(session, data['NUM'])
    localIniTotalPrivateRentalMarket = IniTotalPrivateRentalMarket['count'][0]
    
    # Get the sum of owner households in non-farm, non-reserve private dwellings, count is the field from the POSTGIS
    IniOwner = get_IniOwner(session, data['NUM'])
    localIniOwner = IniOwner['count'][0]

    # Get the sum of owner households in non-farm, non-reserve private dwellings, count is the field from the POSTGIS
    InipercentOfTenantHouseholdsInSubsidizedHousing = get_InipercentOfTenantHouseholdsInSubsidizedHousing(session, data['NUM'])
    localInipercentOfTenantHouseholdsInSubsidizedHousing = InipercentOfTenantHouseholdsInSubsidizedHousing['mean_percent'][0]
    
    # Get the sum of total number of people total immigration status, count is the field from the POSTGIS
    IniTotalImmigrationStatus = get_IniTotalImmigrationStatus(session, data['NUM'])
    localIniTotalImmigrationStatus = IniTotalImmigrationStatus['count'][0]    
    
    # Get the sum of total number of people non-immigration status, count is the field from the POSTGIS
    IniNonImmigrants = get_IniNonImmigrants(session, data['NUM'])
    localIniNonImmigrants = IniNonImmigrants['count'][0]   

    # Get the sum of total number of people with immigration status, count is the field from the POSTGIS
    IniImmigrants = get_IniImmigrants(session, data['NUM'])
    localIniImmigrants = IniImmigrants['count'][0] 

    # Get the sum of total number of people non permanent residents status, count is the field from the POSTGIS
    IniNonPermanentResidents = get_NonPermanentResidents(session, data['NUM'])
    localIniNonPermanentResidents = IniNonPermanentResidents['count'][0] 
     

    # inputjson = f'{{"city": "Montreal", "borough_name": "{borough_name}", "localArea": {localArea},"localIniHealthyFoodStore":{localIniHealthyFoodStore}, "localIniSupermarkets":{localIniSupermarkets}}}'
    inputjson = f'{{"city": "Montreal", "borough_name": "{borough_name}", '\
            f'"newBuildRateSupermarketAndHealthyFoodStore": {newBuildRateSupermarketAndHealthyFoodStore},' \
            f'"newBuildRateFastFoodOutlet": {newBuildRateFastFoodOutlet},' \
            f'"newBuildRatePublicTransport": {newBuildRatePublicTransport},' \
            f'"newBuildRateUrbanFarmsCg": {newBuildRateUrbanFarmsCg},'\
            f'"optimalPublicTransportStationDensity": {optimalPublicTransportStationDensity},' \
            f'"optimalProductionDensity": {optimalProductionDensity},' \
            f'"negativePerceptionsOfLocalArea": {negativePerceptionsOfLocalArea},' \
            f'"residentialOrGeographicalSegregation": {residentialOrGeographicalSegregation},' \
            f'"costsPublicTransportUse": {costsPublicTransportUse},' \
            f'"costsIndividualVehicleUse": {costsIndividualVehicleUse},' \
            f'"openingHoursOfSupermarketsDailyStores": {openingHoursOfSupermarketsDailyStores},' \
            f'"reductionInShelterCosts": {reductionInShelterCosts},' \
            f'"localArea": {localArea},' \
            f'"localIniHealthyFoodStore": {localIniHealthyFoodStore},' \
            f'"localIniSupermarkets": {localIniSupermarkets}, "localIniFastFoodOutlet": {localIniFastFoodOutlet},' \
            f'"localIniPublicTransportStation": {localIniPublicTransportStation},'\
            f'"localIniShelterCostsLessThan30Percent": {localIniShelterCostsLessThan30Percent},' \
            f'"localIniShelterCostsMore30Percent": {localIniShelterCostsMore30Percent},' \
            f'"localResidentialArea": {localResidentialArea},' \
            f'"localIniCoupleWithoutChildren": {localIniCoupleWithoutChildren},' \
            f'"localIniTwoParent": {localIniTwoParent},' \
            f'"localIniSingleParent": {localIniSingleParent},' \
            f'"localIniMultigenerational": {localIniMultigenerational},' \
            f'"localIniSinglePersonLivingAlone": {localIniSinglePersonLivingAlone},' \
            f'"localIniTotalHouseholdTypes": {localIniTotalHouseholdTypes},' \
            f'"localIniTotalPrivateRentalMarket": {localIniTotalPrivateRentalMarket},' \
            f'"localIniOwner": {localIniOwner},' \
            f'"localInipercentOfTenantHouseholdsInSubsidizedHousing": {localInipercentOfTenantHouseholdsInSubsidizedHousing},' \
            f'"localIniTotalImmigrationStatus": {localIniTotalImmigrationStatus},' \
            f'"localIniNonImmigrants": {localIniNonImmigrants},' \
            f'"localIniImmigrants": {localIniImmigrants},' \
            f'"localIniNonPermanentResidents": {localIniNonPermanentResidents}}}'
    # f'"": {},' \
    
    # Convert JSON string to MyClass instance
    obj = json.loads(inputjson, object_hook=custom_decoder)
    # Write the scenario file
    my_scenario = obj.write_scenario(obj.newBuildRateSupermarketAndHealthyFoodStore, \
                                     obj.newBuildRateFastFoodOutlet, \
                                     obj.newBuildRatePublicTransport,\
                                     obj.newBuildRateUrbanFarmsCg, \
                                     obj.optimalPublicTransportStationDensity, \
                                     obj.negativePerceptionsOfLocalArea, \
                                     obj.residentialOrGeographicalSegregation, \
                                     obj.costsPublicTransportUse, \
                                     obj.costsIndividualVehicleUse, \
                                     obj.openingHoursOfSupermarketsDailyStores, \
                                     obj.optimalProductionDensity, \
                                     obj.reductionInShelterCosts, \
                                     obj.localArea, \
                                     obj.localIniHealthyFoodStore, \
                                     obj.localIniSupermarkets, \
                                     obj.localIniFastFoodOutlet, \
                                     obj.localIniPublicTransportStation, \
                                     obj.localIniShelterCostsLessThan30Percent, \
                                     obj.localIniShelterCostsMore30Percent, \
                                     obj.localResidentialArea, \
                                     obj.localIniCoupleWithoutChildren, \
                                     obj.localIniTwoParent, \
                                     obj.localIniSingleParent, \
                                     obj.localIniMultigenerational, \
                                     obj.localIniSinglePersonLivingAlone, \
                                     obj.localIniTotalHouseholdTypes, \
                                     obj.localIniTotalPrivateRentalMarket, \
                                     obj.localIniOwner, \
                                     obj.localInipercentOfTenantHouseholdsInSubsidizedHousing, \
                                     obj.localIniTotalImmigrationStatus, \
                                     obj.localIniNonImmigrants, \
                                     obj.localIniImmigrants, \
                                     obj.localIniNonPermanentResidents)
    return my_scenario
