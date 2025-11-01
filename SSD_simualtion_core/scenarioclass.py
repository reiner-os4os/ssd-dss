import json

class ScenarioClass:

    def __init__(self, city, borough_name, newBuildRateSupermarketAndHealthyFoodStore, \
                 newBuildRateFastFoodOutlet, newBuildRatePublicTransport,\
                 newBuildRateUrbanFarms, timeToAdjustCostsOfPublicTransport,\
                 optimalTransportStationDensity, localArea, localIniHealthyFoodStore, \
                 localIniSupermarkets, localIniFastFoodOutlet, localIniPublicTransportStation, \
                 localIniShelterCostsLessThan30Percent, localIniShelterCostsMore30Percent, localResidentialArea, \
                 localIniCoupleWithoutChildren, localIniTwoParent, localIniSingleParent, localIniMultigenerational, \
                 localIniSinglePersonLivingAlone, localIniTotalHouseholdTypes, \
                 localIniTotalPrivateRentalMarket, localIniOwner, localInipercentOfTenantHouseholdsInSubsidizedHousing, \
                 localIniTotalImmigrationStatus, localIniNonImmigrants, localIniImmigrants, localIniNonPermanentResidents):
            
        self.city = city
        self.borough_name = borough_name
        self.newBuildRateSupermarketAndHealthyFoodStore = newBuildRateSupermarketAndHealthyFoodStore
        self.newBuildRateFastFoodOutlet = newBuildRateFastFoodOutlet
        self.newBuildRatePublicTransport = newBuildRatePublicTransport
        self.newBuildRateUrbanFarms = newBuildRateUrbanFarms
        self.timeToAdjustCostsOfPublicTransport= timeToAdjustCostsOfPublicTransport
        self.optimalTransportStationDensity = optimalTransportStationDensity
        self.localArea = localArea
        self.localIniHealthyFoodStore = localIniHealthyFoodStore
        self.localIniSupermarkets = localIniSupermarkets
        self.localIniFastFoodOutlet = localIniFastFoodOutlet
        self.localIniPublicTransportStation = localIniPublicTransportStation
        self.localIniShelterCostsLessThan30Percent = localIniShelterCostsLessThan30Percent
        self.localIniShelterCostsMore30Percent = localIniShelterCostsMore30Percent
        self.localResidentialArea = localResidentialArea
        self.localIniCoupleWithoutChildren = localIniCoupleWithoutChildren
        self.localIniTwoParent = localIniTwoParent
        self.localIniSingleParent = localIniSingleParent
        self.localIniMultigenerational = localIniMultigenerational
        self.localIniSinglePersonLivingAlone = localIniSinglePersonLivingAlone
        self.localIniTotalHouseholdTypes = localIniTotalHouseholdTypes
        self.localIniTotalPrivateRentalMarket = localIniTotalPrivateRentalMarket
        self.localIniOwner = localIniOwner
        self.localInipercentOfTenantHouseholdsInSubsidizedHousing = localInipercentOfTenantHouseholdsInSubsidizedHousing
        self.localIniTotalImmigrationStatus = localIniTotalImmigrationStatus
        self.localIniNonImmigrants = localIniNonImmigrants
        self.localIniImmigrants = localIniImmigrants
        self.localIniNonPermanentResidents = localIniNonPermanentResidents


    def write_scenario(self, newBuildRateSupermarketAndHealthyFoodStore, \
                       newBuildRateFastFoodOutlet, newBuildRatePublicTransport, \
                       newBuildRateUrbanFarms, timeToAdjustCostsOfPublicTransport,\
                       optimalTransportStationDensity, localArea, localIniHealthyFoodStore, \
                       localIniSupermarkets, localIniFastFoodOutlet, localIniPublicTransportStation, \
                       localIniShelterCostsLessThan30Percent, localIniShelterCostsMore30Percent, localResidentialArea, \
                       localIniCoupleWithoutChildren, localIniTwoParent, localIniSingleParent, localIniMultigenerational, \
                       localIniSinglePersonLivingAlone, localIniTotalHouseholdTypes, \
                       localIniTotalPrivateRentalMarket, localIniOwner, localInipercentOfTenantHouseholdsInSubsidizedHousing, \
                       localIniTotalImmigrationStatus, localIniNonImmigrants, localIniImmigrants, localIniNonPermanentResidents):
        
        scenario_file = 'scenarios/scenarios.json'
        # Step 1: Open the JSON file for reading
        with open(scenario_file, 'r') as file:
            # Parse the JSON file and convert it into a Python dictionary
            data = json.load(file)
            # Step 2: Modify the values within 'food_stores' scenario
        #data['food_security']['scenarios']['base']['constants']['city'] = city
        data['food_security']['scenarios']['base']['constants']['newBuildRateSupermarketAndHealthyFoodStore'] = newBuildRateSupermarketAndHealthyFoodStore
        data['food_security']['scenarios']['base']['constants']['newBuildRateFastFoodOutlet'] = newBuildRateFastFoodOutlet
        data['food_security']['scenarios']['base']['constants']['newBuildRatePublicTransport'] = newBuildRatePublicTransport
        data['food_security']['scenarios']['base']['constants']['newBuildRateUrbanFarms'] = newBuildRateUrbanFarms
        data['food_security']['scenarios']['base']['constants']['timeToAdjustCostsOfPublicTransport'] = timeToAdjustCostsOfPublicTransport
        data['food_security']['scenarios']['base']['constants']['optimalTransportStationDensity'] = optimalTransportStationDensity
        data['food_security']['scenarios']['base']['constants']['localArea'] = localArea
        data['food_security']['scenarios']['base']['constants']['initialNumberOfHealthyFoodStore'] = localIniHealthyFoodStore
        data['food_security']['scenarios']['base']['constants']['initialNumberOfSupermarkets'] = localIniSupermarkets
        data['food_security']['scenarios']['base']['constants']['initialNumberOfFastFoodOutlet'] = localIniFastFoodOutlet
        data['food_security']['scenarios']['base']['constants']['initialNumberOfPublicTransportStation'] = localIniPublicTransportStation
        data['food_security']['scenarios']['base']['constants']['shelterCostsLessThan30Percent'] = localIniShelterCostsLessThan30Percent
        data['food_security']['scenarios']['base']['constants']['shelterCostsMoreThan30Percent'] = localIniShelterCostsMore30Percent
        data['food_security']['scenarios']['base']['constants']['residentialArea'] = localResidentialArea
        data['food_security']['scenarios']['base']['constants']['initialCoupleWithoutChildren'] = localIniCoupleWithoutChildren
        data['food_security']['scenarios']['base']['constants']['initialTwoParent'] = localIniTwoParent
        data['food_security']['scenarios']['base']['constants']['initialSingleParent'] = localIniSingleParent
        data['food_security']['scenarios']['base']['constants']['initialMultigenerational'] = localIniMultigenerational
        data['food_security']['scenarios']['base']['constants']['initialSinglePersonLivingAlone'] = localIniSinglePersonLivingAlone
        data['food_security']['scenarios']['base']['constants']['initialTotalHouseholdTypes'] = localIniTotalHouseholdTypes
        data['food_security']['scenarios']['base']['constants']['initialTotalPrivateRentalMarket'] = localIniTotalPrivateRentalMarket
        data['food_security']['scenarios']['base']['constants']['initialOwner'] = localIniOwner
        data['food_security']['scenarios']['base']['constants']['percentOfTenantHouseholdsInSubsidizedHousing'] = localInipercentOfTenantHouseholdsInSubsidizedHousing
        data['food_security']['scenarios']['base']['constants']['initialTotalImmigrationStatus'] = localIniTotalImmigrationStatus
        data['food_security']['scenarios']['base']['constants']['initialTotalImmigrationStatus'] = localIniNonImmigrants
        data['food_security']['scenarios']['base']['constants']['initialNonImmigrants'] = localIniImmigrants
        data['food_security']['scenarios']['base']['constants']['initialNonPermanentResidents'] = localIniNonPermanentResidents
        # Step 3: Save the modified data back to a JSON file
        with open(scenario_file, 'w') as file:
            json.dump(data, file, indent=4)

        return data