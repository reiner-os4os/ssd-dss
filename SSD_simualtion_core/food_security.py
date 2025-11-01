
#      _                   _ _
#  _____| |__ ___ _ __  _ __(_| |___ _ _
# (_-/ _` / _/ _ | '  \| '_ | | / -_| '_|
# /__\__,_\__\___|_|_|_| .__|_|_\___|_|
#                      |_|
# Copyright (c) 2013-2020 transentis management & consulting. All rights reserved.
#
    
import numpy as np
from scipy.interpolate import interp1d
from scipy.special import gammaln
from scipy.stats import norm
import math, statistics, random, logging
from datetime import datetime
import re
import itertools
from copy import copy, deepcopy

import BPTK_Py
from BPTK_Py import Model
from BPTK_Py import sd_functions as sd
from BPTK_Py import bptk

def bptk_factory():
    bptk = BPTK_Py.bptk()
    return bptk

def cartesian_product(listoflists):
    """
    Helper for Cartesian product
    :param listoflists:
    :return:
    """
    if len(listoflists) == 1:
        return listoflists[0]
    res = list(itertools.product(*listoflists))

    if len(res) == 1:
        return res[0]

    return res

def LERP(x,points):
    """
    Linear interpolation between a set of points
    :param x: x to obtain y for
    :param points: List of tuples containing the graphical function's points [(x,y),(x,y) ... ]
    :return: y value for x obtained using linear interpolation
    """
    x_vals = np.array([ x[0] for x in points])
    y_vals = np.array([x[1] for x in points])

    if x<= x_vals[0]:
        return y_vals[0]

    if x >= x_vals[len(x_vals)-1]:
        return y_vals[len(x_vals)-1]

    f = interp1d(x_vals, y_vals)
    return float(f(x))

class simulation_model():
    def __init__(self):
        # Simulation Settings
        self.dt = 1
        self.starttime = 0.0
        self.stoptime = 120.0
        self.units = 'Month'
        self.method = 'RK4'
        self.equations = {

        # Stocks
        
    
        'numberOfAutomaticVendingMachines'          : lambda t: ( (self.memoize('initialNumberOfAutomaticVendingMachines', t)) if ( t  <=  self.starttime ) else (self.memoize('numberOfAutomaticVendingMachines',t-self.dt) + self.dt * 0) ),
        'numberOfFastFoodOutletAndRestaurants'          : lambda t: ( (self.memoize('initialNumberOfFastFoodOutlet', t)) if ( t  <=  self.starttime ) else (self.memoize('numberOfFastFoodOutletAndRestaurants',t-self.dt) + self.dt * 0) ),
        'numberOfPublicTransportStations'          : lambda t: ( (self.memoize('initialNumberOfPublicTransportStation', t) + 0.001) if ( t  <=  self.starttime ) else (self.memoize('numberOfPublicTransportStations',t-self.dt) + self.dt * ( self.memoize('publicTransportStationDevelopment',t-self.dt) )) ),
        'numberOfSupermaketsAndHealthyFoodStore'          : lambda t: ( (self.memoize('initialNumberOfHealthyFoodStore', t) + self.memoize('initialNumberOfSupermarkets', t) + 0.1) if ( t  <=  self.starttime ) else (self.memoize('numberOfSupermaketsAndHealthyFoodStore',t-self.dt) + self.dt * 0) ),
        'numberOfUrbanFarms'          : lambda t: ( (self.memoize('initialNumberOfUrbanFarms', t)) if ( t  <=  self.starttime ) else (self.memoize('numberOfUrbanFarms',t-self.dt) + self.dt * ( self.memoize('urbanFoodProductionDevelopment',t-self.dt) )) ),
        
    
        # Flows
        
    
        # converters
        'accessibilityAndAffordabilityOfPublicTransport'      : lambda t: ( 1.0 / ( 1.0 + np.exp( -10.0 * ( ( self.memoize('publicTransportStationDensity', t) / self.memoize('optimalPublicTransportStationDensity', t) - 0.5 ) ) ) ) + ( math.cos(self.memoize('affordabilityOfPublicTransport', t) * 3.14159 + 3.14159) / 2.0 + 0.5 ) ) / 2.0,
        'accessibilityOfHealthyFoodInLocalArea'      : lambda t: ( ( math.cos(self.memoize('situationalOrTimeConstraints', t) * 3.14159) / 2.0 + 0.5 ) + ( 1.0 / ( 1.0 + np.exp( -10.0 * ( ( self.memoize('supermarketAndHealthyFoodStoreDensity', t) / self.memoize('fastFoodOutletDensity', t) - 0.5 ) ) ) ) ) ) / 2.0,
        'affordabilityOfPublicTransport'      : lambda t: 1.0 / ( 1.0 + np.exp( -10.0 * ( self.memoize('costsIndividualVehicleUse', t) / self.memoize('costsPublicTransportUse', t) - 1.0 ) ) ),
        'automaticVendingMachinesDevelopment'      : lambda t: self.memoize('newBuildRateAutomaticVendingMachines', t),
        'availabilityOfHealthyFoodInHousehold'      : lambda t: ( ( math.cos(self.memoize('availabilityOfHealthyFoodInLocalArea', t) * 3.14159 + 3.14159) / 2.0 + 0.5 ) + ( math.cos(self.memoize('strategicUnhealthyEatingHabits', t) * 3.14159) / 2.0 + 0.5 ) + ( math.cos(self.memoize('healthDeterminedPurchases', t) * 3.14159 + 3.14159) / 2.0 + 0.5 ) ) / 3.0,
        'availabilityOfHealthyFoodInLocalArea'      : lambda t: ( ( math.cos(self.memoize('accessibilityOfHealthyFoodInLocalArea', t) * 3.14159 + 3.14159) / 2.0 + 0.5 ) + ( ( 1.0 / ( 1.0 + np.exp( -10.0 * ( ( self.memoize('productionDenisty', t) / self.memoize('optimalProductionDensity', t) ) - 0.5 ) ) ) ) ) ) / 3.0,
        'cCoupleWithoutChildren'      : lambda t: 0.006736,
        'cImmigrants'      : lambda t: 0.035312,
        'cMultigenerational'      : lambda t: 0.004491,
        'cNonImmigrants'      : lambda t: 0.031434,
        'cNonPermanentResidents'      : lambda t: 0.033475,
        'cOwner'      : lambda t: 0.002041,
        'cPrivateRentalMarket'      : lambda t: 0.073278,
        'cSingleParent'      : lambda t: 0.012655,
        'cSinglePersonLivingAlone'      : lambda t: 0.006736,
        'cSubsidizedHousing'      : lambda t: 0.015717,
        'cTwoParent'      : lambda t: 0.034904,
        'coeffHousehold'      : lambda t: 3.20924,
        'coeffHousing'      : lambda t: 0.502839,
        'coeffImmi'      : lambda t: -0.146239,
        'costsIndividualVehicleUse'      : lambda t: 0.5,
        'costsPublicTransportUse'      : lambda t: 0.5,
        'customerDemandForHealthyFood'      : lambda t: math.cos(self.memoize('healthDeterminedPurchases', t) * 3.14159 + 3.14159) / 2.0 + 0.5,
        'fastFoodOutletDensity'      : lambda t: ( self.memoize('numberOfFastFoodOutletAndRestaurants', t) + self.memoize('numberOfAutomaticVendingMachines', t) ) / self.memoize('residentialArea', t) + 0.1,
        'fastFoodOutletDevelopment'      : lambda t: self.memoize('newBuildRateFastFoodOutlet', t),
        'financialManagement'      : lambda t: math.cos(self.memoize('pressureOnCostOfLiving', t) * 3.14159) / 2.0 + 0.5,
        'healthDeterminedPurchases'      : lambda t: math.cos(self.memoize('willingnessToPayForHealthyFoods', t) * 3.14159 + 3.14159) / 2.0 + 0.5,
        'householdCircumstancesFoodInsecurity'      : lambda t: self.memoize('householdTypeRisk', t) + self.memoize('housingSituationRisk', t) + self.memoize('immigrationStatusRisk', t) + self.memoize('interceptSimple', t),
        'householdFoodInsecurity'      : lambda t: ( ( math.cos(self.memoize('insufficientFoodBudget', t) * 3.14159 + 3.14159) / 2.0 + 0.5 ) + ( math.cos(self.memoize('availabilityOfHealthyFoodInHousehold', t) * 3.14159) / 2.0 + 0.5 ) + ( math.cos(self.memoize('householdCircumstancesFoodInsecurity', t) * 3.14159 + 3.14159) / 2.0 + 0.5 ) ) / 3.0,
        'householdTypeRisk'      : lambda t: ( self.memoize('cCoupleWithoutChildren', t) * self.memoize('initialCoupleWithoutChildren', t) + self.memoize('cMultigenerational', t) * self.memoize('initialMultigenerational', t) + self.memoize('cSingleParent', t) * self.memoize('initialSingleParent', t) + self.memoize('cSinglePersonLivingAlone', t) * self.memoize('initialSinglePersonLivingAlone', t) + self.memoize('cTwoParent', t) * self.memoize('initialTwoParent', t) ) / self.memoize('initialTotalHouseholdTypes', t),
        'housingSituationRisk'      : lambda t: ( self.memoize('cOwner', t) * self.memoize('initialOwner', t) + self.memoize('cPrivateRentalMarket', t) * self.memoize('initialPrivateRentalMarket', t) + self.memoize('cSubsidizedHousing', t) * self.memoize('initialSubsidizedHousing', t) ) / self.memoize('initialTotalHouseholdTypes', t),
        'immigrationStatusRisk'      : lambda t: ( self.memoize('cImmigrants', t) * self.memoize('initialImmigrants', t) + self.memoize('cNonImmigrants', t) * self.memoize('initialNonImmigrants', t) + self.memoize('cNonPermanentResidents', t) * self.memoize('initialNonPermanentResidents', t) ) / self.memoize('initialTotalHouseholdTypes', t),
        'initialCoupleWithoutChildren'      : lambda t: 13040.0,
        'initialImmigrants'      : lambda t: 32940.0,
        'initialMultigenerational'      : lambda t: 238.0,
        'initialNonImmigrants'      : lambda t: 55054.0,
        'initialNonPermanentResidents'      : lambda t: 20117.0,
        'initialNumberOfAutomaticVendingMachines'      : lambda t: 0.0,
        'initialNumberOfFastFoodOutlet'      : lambda t: 1527.0,
        'initialNumberOfHealthyFoodStore'      : lambda t: 35.0,
        'initialNumberOfPublicTransportStation'      : lambda t: 538.0,
        'initialNumberOfSupermarkets'      : lambda t: 313.0,
        'initialNumberOfUrbanFarms'      : lambda t: 0.0,
        'initialOwner'      : lambda t: 18507.0,
        'initialPrivateRentalMarket'      : lambda t: self.memoize('initialTotalPrivateRentalMarket', t) * ( 1.0 - self.memoize('percentOfTenantHouseholdsInSubsidizedHousing', t) ),
        'initialSingleParent'      : lambda t: 3186.0,
        'initialSinglePersonLivingAlone'      : lambda t: 35456.0,
        'initialSubsidizedHousing'      : lambda t: self.memoize('percentOfTenantHouseholdsInSubsidizedHousing', t) * self.memoize('initialTotalPrivateRentalMarket', t),
        'initialTotalHouseholdTypes'      : lambda t: 64619.0,
        'initialTotalImmigrationStatus'      : lambda t: 108112.0,
        'initialTotalPrivateRentalMarket'      : lambda t: 46075.0,
        'initialTwoParent'      : lambda t: 5603.0,
        'insufficientFoodBudget'      : lambda t: ( ( math.cos(self.memoize('pressureOnCostOfLiving', t) * 3.14159 + 3.14159) / 2.0 + 0.5 ) + ( math.cos(self.memoize('financialManagement', t) * 3.14159) / 2.0 + 0.5 ) ) / 2.0,
        'interceptSimple'      : lambda t: 0.00470216,
        'livingCostBurden'      : lambda t: ( ( math.cos(self.memoize('pressureOnCostOfLiving', t) * 3.14159 + 3.14159) / 2.0 + 0.5 ) + ( math.cos(self.memoize('insufficientFoodBudget', t) * 3.14159 + 3.14159) / 2.0 + 0.5 ) + ( math.cos(self.memoize('affordabilityOfPublicTransport', t) * 3.14159) / 2.0 + 0.5 ) ) / 3.0,
        'localMarketPressure'      : lambda t: ( ( math.cos(self.memoize('needToShopOutsideLocality', t) * 3.14159 + 3.14159) / 2.0 + 0.5 ) + ( math.cos(self.memoize('customerDemandForHealthyFood', t) * 3.14159 + 3.14159) / 2.0 + 0.5 ) ) / 2.0,
        'needToShopOutsideLocality'      : lambda t: math.cos(self.memoize('availabilityOfHealthyFoodInLocalArea', t) * 3.14159) / 2.0 + 0.5,
        'negativePerceptionsOfLocalArea'      : lambda t: 0.5,
        'newBuildRateAutomaticVendingMachines'      : lambda t: 0.0,
        'newBuildRateFastFoodOutlet'      : lambda t: 2.0,
        'newBuildRateOfPublicTransportStations'      : lambda t: 0.01,
        'newBuildRateSupermarketAndHealthyFoodStore'      : lambda t: 2.0,
        'newBuildRateUrbanFarmsCg'      : lambda t: 0.0,
        'objectiveRelativeCostOfHealthyFood'      : lambda t: math.cos(self.memoize('availabilityOfHealthyFoodInLocalArea', t) * 3.14159) / 2.0 + 0.5,
        'openingHoursOfSupermarketsDailyStores'      : lambda t: 0.5,
        'optimalProductionDensity'      : lambda t: 0.2,
        'optimalPublicTransportStationDensity'      : lambda t: 8.0,
        'perceivedAffordabilityOfHealthyFood'      : lambda t: ( ( math.cos(self.memoize('availabilityOfHealthyFoodInLocalArea', t) * 3.14159 + 3.14159) / 2.0 + 0.5 ) + ( math.cos(self.memoize('objectiveRelativeCostOfHealthyFood', t) * 3.14159) / 2.0 + 0.5 ) + ( 1.0 / ( 1.0 + np.exp( -10.0 * ( ( self.memoize('fastFoodOutletDensity', t) ) - 0.5 ) ) ) ) + ( math.cos(self.memoize('insufficientFoodBudget', t) * 3.14159) / 2.0 + 0.5 ) ) / 4.0,
        'percentOfTenantHouseholdsInSubsidizedHousing'      : lambda t: 0.2,
        'pressureOnCostOfLiving'      : lambda t: self.memoize('shelterCostsMoreThan30Percent', t) / ( self.memoize('shelterCostsMoreThan30Percent', t) + self.memoize('shelterCostsLessThan30Percent', t) ),
        'pressureOnPolicyForPublicTransportDevelopment'      : lambda t: ( 1.0 * ( math.cos(self.memoize('needToShopOutsideLocality', t) * 3.14159 + 3.14159) / 2.0 + 0.5 ) + ( math.cos(self.memoize('accessibilityAndAffordabilityOfPublicTransport', t) * 3.14159) / 2.0 + 0.5 ) ) / 2.0,
        'productionDenisty'      : lambda t: self.memoize('numberOfUrbanFarms', t) / self.memoize('residentialArea', t),
        'publicTransportStationDensity'      : lambda t: self.memoize('numberOfPublicTransportStations', t) / self.memoize('residentialArea', t),
        'publicTransportStationDevelopment'      : lambda t: self.memoize('newBuildRateOfPublicTransportStations', t) * math.cos(self.memoize('pressureOnPolicyForPublicTransportDevelopment', t) * 3.14159 + 3.14159),
        'residentialArea'      : lambda t: 3.86889,
        'residentialOrGeographicalSegregation'      : lambda t: 0.5,
        'residentialSegregation'      : lambda t: 0.5,
        'shelterCostsLessThan30Percent'      : lambda t: 39242.0 + 23426.0 - self.memoize('shelterCostsMoreThan30Percent', t),
        'shelterCostsMoreThan30Percent'      : lambda t: 23426.0,
        'situationalOrTimeConstraints'      : lambda t: ( math.cos(self.memoize('openingHoursOfSupermarketsDailyStores', t) * 3.14159) / 2.0 + 0.5 + math.cos(self.memoize('accessibilityAndAffordabilityOfPublicTransport', t) * 3.14159) / 2.0 + 0.5 ) / 2.0,
        'strategicUnhealthyEatingHabits'      : lambda t: ( ( math.cos(self.memoize('financialManagement', t) * 3.14159 + 3.14159) / 2.0 + 0.5 ) + ( math.cos(self.memoize('insufficientFoodBudget', t) * 3.14159 + 3.14159) / 2.0 + 0.5 ) ) / 2.0,
        'supermarketAndHealthyFoodStoreDensity'      : lambda t: self.memoize('numberOfSupermaketsAndHealthyFoodStore', t) / self.memoize('residentialArea', t),
        'supermarketAndHealthyFoodStoreDevelopment'      : lambda t: self.memoize('newBuildRateSupermarketAndHealthyFoodStore', t) * ( math.cos(self.memoize('localMarketPressure', t) * 3.14159 + 3.14159) + math.cos(self.memoize('negativePerceptionsOfLocalArea', t) * 3.14159) + math.cos(self.memoize('residentialOrGeographicalSegregation', t) * 3.14159) ) / 3.0,
        'urbanFoodProductionDevelopment'      : lambda t: self.memoize('newBuildRateUrbanFarmsCg', t) * math.cos(self.memoize('customerDemandForHealthyFood', t) * 3.14159 + 3.14159),
        'vulnerabilityToFluctuationInLivingCosts'      : lambda t: ( math.cos(self.memoize('livingCostBurden', t) * 3.14159 + 3.14159) / 2.0 + 0.5 ),
        'willingnessToPayForHealthyFoods'      : lambda t: ( ( math.cos(self.memoize('perceivedAffordabilityOfHealthyFood', t) * 3.14159 + 3.14159) / 2.0 + 0.5 ) + ( math.cos(self.memoize('vulnerabilityToFluctuationInLivingCosts', t) * 3.14159) / 2.0 + 0.5 ) + ( math.cos(self.memoize('insufficientFoodBudget', t) * 3.14159) / 2.0 + 0.5 ) ) / 3.0,
        
    
        # gf
        
    
        #constants
        
    
    
        }
    
        self.points = {
            
        }
    
    
        self.dimensions = {
        	'': {
                'labels': [  ],
                'variables': [  ],
            },
        }
                
        self.dimensions_order = {}     
    
        self.stocks = ['numberOfAutomaticVendingMachines',   'numberOfFastFoodOutletAndRestaurants',   'numberOfPublicTransportStations',   'numberOfSupermaketsAndHealthyFoodStore',   'numberOfUrbanFarms'  ]
        self.flows = []
        self.converters = ['accessibilityAndAffordabilityOfPublicTransport',   'accessibilityOfHealthyFoodInLocalArea',   'affordabilityOfPublicTransport',   'automaticVendingMachinesDevelopment',   'availabilityOfHealthyFoodInHousehold',   'availabilityOfHealthyFoodInLocalArea',   'cCoupleWithoutChildren',   'cImmigrants',   'cMultigenerational',   'cNonImmigrants',   'cNonPermanentResidents',   'cOwner',   'cPrivateRentalMarket',   'cSingleParent',   'cSinglePersonLivingAlone',   'cSubsidizedHousing',   'cTwoParent',   'coeffHousehold',   'coeffHousing',   'coeffImmi',   'costsIndividualVehicleUse',   'costsPublicTransportUse',   'customerDemandForHealthyFood',   'fastFoodOutletDensity',   'fastFoodOutletDevelopment',   'financialManagement',   'healthDeterminedPurchases',   'householdCircumstancesFoodInsecurity',   'householdFoodInsecurity',   'householdTypeRisk',   'housingSituationRisk',   'immigrationStatusRisk',   'initialCoupleWithoutChildren',   'initialImmigrants',   'initialMultigenerational',   'initialNonImmigrants',   'initialNonPermanentResidents',   'initialNumberOfAutomaticVendingMachines',   'initialNumberOfFastFoodOutlet',   'initialNumberOfHealthyFoodStore',   'initialNumberOfPublicTransportStation',   'initialNumberOfSupermarkets',   'initialNumberOfUrbanFarms',   'initialOwner',   'initialPrivateRentalMarket',   'initialSingleParent',   'initialSinglePersonLivingAlone',   'initialSubsidizedHousing',   'initialTotalHouseholdTypes',   'initialTotalImmigrationStatus',   'initialTotalPrivateRentalMarket',   'initialTwoParent',   'insufficientFoodBudget',   'interceptSimple',   'livingCostBurden',   'localMarketPressure',   'needToShopOutsideLocality',   'negativePerceptionsOfLocalArea',   'newBuildRateAutomaticVendingMachines',   'newBuildRateFastFoodOutlet',   'newBuildRateOfPublicTransportStations',   'newBuildRateSupermarketAndHealthyFoodStore',   'newBuildRateUrbanFarmsCg',   'objectiveRelativeCostOfHealthyFood',   'openingHoursOfSupermarketsDailyStores',   'optimalProductionDensity',   'optimalPublicTransportStationDensity',   'perceivedAffordabilityOfHealthyFood',   'percentOfTenantHouseholdsInSubsidizedHousing',   'pressureOnCostOfLiving',   'pressureOnPolicyForPublicTransportDevelopment',   'productionDenisty',   'publicTransportStationDensity',   'publicTransportStationDevelopment',   'residentialArea',   'residentialOrGeographicalSegregation',   'residentialSegregation',   'shelterCostsLessThan30Percent',   'shelterCostsMoreThan30Percent',   'situationalOrTimeConstraints',   'strategicUnhealthyEatingHabits',   'supermarketAndHealthyFoodStoreDensity',   'supermarketAndHealthyFoodStoreDevelopment',   'urbanFoodProductionDevelopment',   'vulnerabilityToFluctuationInLivingCosts',   'willingnessToPayForHealthyFoods'  ]
        self.gf = []
        self.constants= []
        self.events = [
            ]
    
        self.memo = {}
        for key in list(self.equations.keys()):
          self.memo[key] = {}  # DICT OF DICTS!
          
    
    """
    Builtin helpers
    """
    def ramp(self,slope,start,t):
        if not start:
            start = self.starttime
        if t <= start: return 0
        return (t-start)*slope
        
    def rootn(self,expression,order):
        order = round(order,0)
        if expression < 0 and order % 2 == 0: # Stella does not allow even roots for negative numbers as no complex numbers are supported
            return np.nan
        return -abs(expression)**(1/round(order,0)) if expression < 0 else abs(expression)**(1/round(order,0)) # Stella Logic! No Complex numbers for negative numbers. Hence take the nth root of the absolute value and then add the negativity (if any)
    
    """
    Statistical builtins with Seed
    """
    def pareto_with_seed(self, shape, scale, seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.pareto(shape) * scale  
    
    def weibull_with_seed(self, shape, scale, seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.weibull(shape) * scale      
    
    def poisson_with_seed(self, mu, seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.poisson(mu)   
    
    def negbinomial_with_seed(self, successes, p, seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.negative_binomial(successes, p)  
    
    def lognormal_with_seed(self, mean, stdev, seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.lognormal(mean, stdev)   
    
    def logistic_with_seed(self, mean, scale, seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.logistic(mean, scale)
    
    def random_with_seed(self, seed, t ):
        if t == self.starttime:
            random.seed(int(seed))
        return random.random()

    def beta_with_seed(self, a,b,seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.beta(a,b)
        
    def binomial_with_seed(self, n,p,seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.binomial(n,p)
        
    def gamma_with_seed(self, shape,scale,seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.gamma(shape,scale)
        
    def exprnd_with_seed(self, plambda,seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.exponential(plambda)
        
    def geometric_with_seed(self, p, seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.geometric(p)
    
    def triangular_with_seed(self, left, mode, right, seed, t):
        if t == self.starttime:
            np.random.seed(int(seed))
        return np.random.triangular(left, mode, right)
    
    def rank(self, lis, rank):
        rank = int(rank)
        sorted_list = np.sort(lis)
        try:
            rankth_elem = sorted_list[rank-1]
        except IndexError as e:
            logging.error("RANK: Rank {} too high for array of size {}".format(rank,len(lis)))
        return (lis==rankth_elem).nonzero()[0][0]+1
        

    def interpolate(self, variable, t, *args):
        """
        Helper for builtin "interpolate". Uses the arrayed variable and args to compute the interpolation
        :param variable:
        :param t:
        :param args: Interpolation weight for each dimension, between one or zero
        :return:
        """
        def compute_x(values): #
            """
            Compute x values for interpolation. Always from 0 to 1. E.g. values = [1,2,3], then x = [0, 0.5, 1.0]
            :param values:
            :return:
            """
            #
            x = [0]
            for i in range(1, len(values)): x += [x[i - 1] + 1 / (len(values) - 1)]
            return x

        def interpolate_values(index, y_val):  # Internal interpolate of a dimension's results
            x_val = compute_x(y_val)
            points = [(x_val[i], y_val[i]) for i in range(0, len(x_val))]
            return LERP(index, points)

        # Fix each weight to a value between 0 and 1
        args = [max(0,min(x,1)) for x in args]

        # Get dimensions of variable (2,3,4 ...)
        dimensions = self.dimensions_order[variable]

        # Get Labels
        labels = {key: dim["labels"] for key, dim in
                  dict(filter(lambda elem: elem[0] in dimensions, self.dimensions.items())).items()}

        # Compute
        results = {}
        if len(labels.keys()) == 1:
            return interpolate_values(args[0], self.equation(variable + "[*]", t))
        for index, dimension in enumerate(dimensions):
            results[dimension] = []
            for label in labels[dimension]:
                indices = ["*" if i != index else label for i in
                           range(0, len(dimensions))]  # Build indices, such as "*,element1" or "1,*"

                results[dimension] += [
                    interpolate_values(args[index], self.equation(variable + "[{}]".format(",".join(indices)), t))]

        return [interpolate_values(args[i], v) for i, v in enumerate(results.values())][0]

    def lookupinv(self,gf, value):
        """
        Helper for lookupinv builtin. Looks for the corresponding x of a given y
        :param gf: Name of graphical function
        :param value: Value we are looking for (y)
        :return:
        """
        def lerpfun(x, points):  # Special lerp function for the reversed points
            from scipy.interpolate import interp1d
            x_vals = np.array([x[0] for x in points])
            y_vals = np.array([x[1] for x in points])
            f = interp1d(x_vals, y_vals)
            return f(x)

        results = []
        for t in np.arange(self.starttime, self.stoptime + self.dt,
                           self.dt):  # Compute all y values for graphical functions using standard interpolate (LERP)
            results += [(LERP(t, self.points[gf]), t)] # y,x

        return np.round(lerpfun(value, results),
                     3)  # Use LERP function for the reversed set of points (y,x) and find the correct value. Cannot use standard LERP here because that would require continuous X (1,2,3..)

    def delay(self, tdelayed, offset, initial, t):
        '''
        Delay builtin
        :param tdelayed: Delayed T
        :param offset: Offset
        :param initial: Initial value
        :param t:
        :return:
        '''
        if (t - self.starttime) < offset: return initial
        else: return tdelayed

    def counter(self,start, interval, t):
        '''
        Counter bultin
        :param start:
        :param interval:
        :param t:
        :return:
        '''
        num_elems = (interval / start / self.dt)
        value = interval / num_elems
        t_copy = copy(t)

        while t >= interval: t = t - interval
        if (t_copy > interval): return (start + (t / self.dt) * value)

        return (t / self.dt * value)

    def npv(self, initial, p, t):
        """
        NPV (Net Present Value) builtin
        :param initial:
        :param p:
        :param t:
        :return:
        """
        rate = 1.0 / (1.0 + p) ** (t - self.dt - self.starttime + self.dt)
        return initial if (t <= self.starttime) else ( self.npv(initial, p, t - self.dt) + (self.dt * rate * initial) )# Recurse

    def irr(self, stock_name, missing, t,myname):
        """
        Approximate IRR (Internal Rate of Return)
        :param stock_name: Identifier of Stock to approximate for
        :param missing: Replace missing values with this value
        :param t:
        :return:
        """

        def compute_npv(stock_name, t, i, missing):
            I = missing if missing else self.equation(stock_name, self.starttime)
            return I + sum( [self.memoize(stock_name, t) / (1 + i) ** t for t in np.arange(self.starttime+self.dt , t, self.dt)])

        i = 0
        try:
            i = 0 if t <= self.starttime + self.dt else self.memo[myname][t-self.dt]
        except:
            pass

        if t == self.starttime: return None

        best_kw = {i : compute_npv(stock_name, t, i, missing)}
        for _ in range(0, 300):
            # Here we approximate the IRR
            kw = compute_npv(stock_name, t, i, missing)

            change = 0.001

            best_kw[i] = kw

            if abs(kw) < self.memoize(stock_name, t)*0.1: change = 0.0001

            if abs(kw) < self.memoize(stock_name, t)*0.05: change = 0.00001

            if abs(kw) < self.memoize(stock_name, t)*0.02: change = 0.000001

            if kw < 0: i -= change
            elif kw > 0:  i += change

            if kw == 0: return i
        best_kw = {k: v for k, v in sorted(best_kw.items(), key=lambda item: item[1])}
        x = {v: k for k, v in sorted(best_kw.items(), key=lambda item: item[1])} # Sort by best npv
        return x[min(x.keys())]

    def normalcdf(self,left, right, mean, sigma):
        import scipy.stats
        right = scipy.stats.norm(float(mean), float(sigma)).cdf(float(right))
        left = scipy.stats.norm(float(mean), float(sigma)).cdf(float(left))
        return round(right - left, 3)

    def cgrowth(self, p):
        from sympy.core.numbers import Float
        import sympy as sy
        z = sy.symbols('z', real=True) # We want to find z
        dt = self.dt

        x = (1 + dt * (1 * z))

        for i in range(1, int(1 / dt)): x = (x + dt * (x * z))

        # Definition of the equation to be solved
        eq = sy.Eq(1 + p, x)

        # Solve the equation
        results = [x for x in (sy.solve(eq)) if type(x) is Float and x > 0] # Quadratic problem, hence usually a positive, negative and 2 complex solutions. We only require the positive one
        return float(results[0])

    def montecarlo(self,probability,seed, t):
        """
        Montecarlo builtin
        :param probability:
        :param seed:
        :param t:
        :return:
        """
        if seed and t==self.starttime:
            random.seed(seed)
        rndnumber = random.uniform(0,100)
        return 1 if rndnumber < (probability*self.dt) else 0


    def derivn(self, equation, order, t):
        """
        nth derivative of an equation
        :param equation: Name of the equation
        :param order: n
        :param t: current t
        :return:
        """
        memo = {}
        dt = 0.25

        def mem(eq, t):
            """
            Memo for internal equations
            :param eq:
            :param t:
            :return:
            """
            if not eq in memo.keys(): memo[eq] = {}
            mymemo = memo[eq]
            if t in mymemo.keys(): return mymemo[t]
            else:
                mymemo[t] = s[eq](t)
                return mymemo[t]

        s = {}
        s[1] = lambda t: 0 if t <= self.starttime else (self.memoize(equation, t) - self.memoize(equation, t - dt)) / dt

        def addEquation(n):
            s[n] = lambda t: 0 if t <= self.starttime else (mem(n - 1, t) - mem(n - 1, t - dt)) / dt

        for n in list(range(2, order + 1)): addEquation(n)

        return s[order](t) if ( t >= self.starttime + (dt * order) ) else 0

    def smthn(self, inputstream, averaging_time, initial, n, t):
        """
        Pretty complex operator. Actually we are building a whole model here and have it run
        Find info in https://www.iseesystems.com/resources/help/v1-9/default.htm#08-Reference/07-Builtins/Delay_builtins.htm#kanchor364
        :param inputstream:
        :param averaging_time:
        :param initial:
        :param n:
        :param t:
        :return:
        """
        memo = {}
        dt = self.dt
        from copy import deepcopy

        def mem(eq, t):
            """
            Internal memo for equations
            :param eq:
            :param t:
            :return:
            """
            if not eq in memo.keys(): memo[eq] = {}
            mymemo = memo[eq]
            if t in mymemo.keys():return mymemo[t]
            else:
                mymemo[t] = s[eq](t)
                return mymemo[t]

        s = {}

        def addEquation(n, upper):
            y = deepcopy(n)
            if y == 1:
                s["stock1"] = lambda t: (
                    (max([0, (self.memoize(inputstream, t) if (initial is None) else initial)])) if (
                                t <= self.starttime) else (
                                mem('stock1', t - dt) + dt * (mem('changeInStock1', t - dt))))
                s['changeInStock1'] = lambda t: (self.memoize(inputstream, t) - mem('stock1', t)) / (
                            averaging_time / upper)
            if y > 1:
                s["stock{}".format(y)] = lambda t: (
                    (max([0, (self.memoize(inputstream, t) if (initial is None) else initial)])) if (t <= self.starttime) else (
                                mem("stock{}".format(y), t - dt) + dt * (mem('changeInStock{}'.format(y), t - dt))))
                s['changeInStock{}'.format(y)] = lambda t: (mem("stock{}".format(y - 1), t) - mem("stock{}".format(y),
                                                                                                  t)) / (averaging_time / upper)
        n = int(n)

        for i in list(range(0, n + 1)): addEquation(i, n)

        return s['stock{}'.format(n)](t)

    def forcst(self,inputstream, averaging_time, horizon, initial, t):
        memo = {"change_in_input": {}, "average_input": {}, "trend_in_input": {}, "forecast_input": {}}

        def mem(eq, t):
            """
            Internal memo for equations
            :param eq:
            :param t:
            :return:
            """
            mymemo = memo[eq]
            if t in mymemo.keys(): return mymemo[t]
            else:
                mymemo[t] = s[eq](t)
                return mymemo[t]

        s = {
            "change_in_input": lambda t: max([0, (self.memoize(inputstream,t) - mem('average_input', t)) / averaging_time]),
            "average_input": lambda t: ((self.memoize(inputstream,t)) if (t <= self.starttime) else (
                        mem("average_input", t - self.dt) + self.dt * (mem("change_in_input", t - self.dt)))),
            "trend_in_input": lambda t: (((self.memoize(inputstream,t) - self.memoize('averageInput', t)) / (
                        self.memoize('averageInput', t) * self.memoize('averagingTime', t))) if (
                        self.memoize('averageInput', t) > 0.0) else (np.nan)),
            "forecast_input": lambda t: self.memoize(inputstream,t) * (1.0 + mem("trend_in_input", t) * horizon)
        }

        return s["forecast_input"](t)

    #Helpers for Dimensions (Arrays)

    def find_dimensions(self, stock):
        stockdimensions = {}
        for dimension, values in self.dimensions.items():
            if stock in values["variables"]:
                stockdimensions[dimension] = values["labels"]

        if len(stockdimensions.keys()) == 1:
            return [stock + "[{}]".format(x) for x in stockdimensions[list(stockdimensions.keys())[0]]]

    def get_dimensions(self, equation, t):
        re_find_indices = r'\[([^)]+)\]'
        group = re.search(re_find_indices, equation).group(0).replace("[", "").replace("]", "")
        equation_basic = equation.replace(group, "").replace("[]", "")
        labels = []
        for index, elem in enumerate(group.split(",")):
            if len(elem.split(":")) > 1: # List operator
                try:
                    bounds = [int(x) for x in elem.split(":")]
                except ValueError as e:
                    logging.error(e)
                    continue
                bounds = sorted(bounds)
                if len(bounds) > 2:
                    logging.error("Too many arguments for list operator. Expecting 2, got {}".format(len(bounds)))

                labels += [list(range(bounds[0], bounds[1]+1))]

            elif elem == "*": # Star operator
                dim = self.dimensions_order[equation_basic][index]
                labels += [self.dimensions[dim]["labels"]]
            else:
                if not type(elem) is list:
                    labels += [[elem]]
                else:
                    labels += [elem]

        products = cartesian_product(labels)

        return_list = []

        for product in products:
            prod = str(product).replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("'", "").replace(" ", "")
            return_list += [self.memoize(equation_basic + "[{}]".format(prod), t)]
            
        return np.array(return_list)


    #Access equations API

    def equation(self, equation, arg):
        return self.memoize(equation,arg)


    #Memoizer for equations. Also does most of API work

    def memoize(self, equation, arg):
        if type(equation) is float or type(equation) is int: # Fallback for values
            return equation
        if "*" in equation or ":" in equation:
            return self.get_dimensions(equation,arg)
            
        if not equation in self.equations.keys():

            # match array pattern and find non-arrayed var
            import re
            match = re.findall(r'\[[a-zA-Z1-9,_]*\]', equation)

            if match:

                equation_replaced = equation.replace(match[0], "")

                if equation_replaced in self.equations:
                    return self.memoize(equation=equation_replaced,arg=arg)
            else:
                logging.error("Equation '{}' not found!".format(equation))

        mymemo = self.memo[equation]

        if arg in mymemo.keys():
            return mymemo[arg]
        else:
            result = self.equations[equation](arg)
            mymemo[arg] = result

        return result


    def setDT(self, v):
        self.dt = v

    def setStarttime(self, v):
        self.starttime = v

    def setStoptime(self, v):
        self.stoptime = v
    
    def specs(self):
        return self.starttime, self.stoptime, self.dt, 'Month', 'RK4'
    