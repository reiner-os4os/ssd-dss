def select_data(Name, census_droped):
    # Population characteristics, number and age 
    if Name == 'census_population':
        census_droped_short = census_droped[(census_droped["CHARACTERISTIC_ID"] == 1) #'Population, 2021'
                            | (census_droped["CHARACTERISTIC_ID"] == 2) #'Population, 2016' 
                            | (census_droped["CHARACTERISTIC_ID"] == 3) #'Population percentage change, 2016 to 2021'
                            | (census_droped["CHARACTERISTIC_ID"] == 8) #"Total - Age groups of the population - 100% data"
                            | (census_droped["CHARACTERISTIC_ID"] == 39) #"Average age of the population"
                            | (census_droped["CHARACTERISTIC_ID"] == 40)] #"Median age of the population"      
        return census_droped_short
    
    # Private dwelling information
    elif Name == 'census_private_dwellings':
        census_droped_short = census_droped[(census_droped["CHARACTERISTIC_ID"] == 4) #'Total private dwellings'
                            | (census_droped["CHARACTERISTIC_ID"] == 5) #"Private dwellings occupied by usual residents"
                            | (census_droped["CHARACTERISTIC_ID"] == 41) #"Total - Occupied private dwellings by structural type of dwelling - 100% data"
                            | (census_droped["CHARACTERISTIC_ID"] == 50) #"Total - Private households by household size - 100% data"
                            | (census_droped["CHARACTERISTIC_ID"] == 56) #"Number of persons in private households"
                            | (census_droped["CHARACTERISTIC_ID"] == 57) #"Average household size"
                            | (census_droped["CHARACTERISTIC_ID"] == 71) #"Total - Census families in private households by family size - 100% data"
                            | (census_droped["CHARACTERISTIC_ID"] == 76) #"Average size of census families"
                            | (census_droped["CHARACTERISTIC_ID"] == 77)] #"Average number of children in census families with children"
        return census_droped_short 

    elif Name == 'census_household_type':
        census_droped_short = census_droped[(census_droped["CHARACTERISTIC_ID"] == 100) # Total - Household type - 100% data
                            | (census_droped["CHARACTERISTIC_ID"] == 101) # One-census-family households without additional persons
                            | (census_droped["CHARACTERISTIC_ID"] == 102) # Couple-family households
                            | (census_droped["CHARACTERISTIC_ID"] == 103) # With children
                            | (census_droped["CHARACTERISTIC_ID"] == 104) # Without children
                            | (census_droped["CHARACTERISTIC_ID"] == 105) # One-parent-family households
                            | (census_droped["CHARACTERISTIC_ID"] == 106) # Multigenerational households
                            | (census_droped["CHARACTERISTIC_ID"] == 107) # Multiple-census-family households
                            | (census_droped["CHARACTERISTIC_ID"] == 108) # One-census-family households with additional persons
                            | (census_droped["CHARACTERISTIC_ID"] == 109) # Two-or-more-person non-census-family households 
                            | (census_droped["CHARACTERISTIC_ID"] == 110)] # One-person households
        return census_droped_short 
           
    # Total income information for the year 2020
    elif Name == 'census_total_income_2020':
        census_droped_short = census_droped[(census_droped["CHARACTERISTIC_ID"] == 111) # Total - Income statistics in 2020 for the population aged 15 years and over in private households - 100% data
                                           | (census_droped["CHARACTERISTIC_ID"] == 112) # Number of total income recipients aged 15 years and over in private households in 2020 - 100% data
                                           | (census_droped["CHARACTERISTIC_ID"] == 113) # Median total income in 2020 among recipients ($)
                                           | (census_droped["CHARACTERISTIC_ID"] == 114) # Number of after-tax income recipients aged 15 years and over in private households in 2020 - 100% data
                                           | (census_droped["CHARACTERISTIC_ID"] == 115) # Median after-tax income in 2020 among recipients ($)
                                           | (census_droped["CHARACTERISTIC_ID"] == 116) # Number of market income recipients aged 15 years and over in private households in 2020 - 100% data
                                           | (census_droped["CHARACTERISTIC_ID"] == 117) # Median market income in 2020 among recipients ($)
                                           | (census_droped["CHARACTERISTIC_ID"] == 118) # Number of employment income recipients aged 15 years and over in private households in 2020 - 100% data
                                           | (census_droped["CHARACTERISTIC_ID"] == 119) # Median employment income in 2020 among recipients ($)
                                           | (census_droped["CHARACTERISTIC_ID"] == 120) # Number of government transfers recipients aged 15 years and over in private households in 2020 - 100% data
                                           | (census_droped["CHARACTERISTIC_ID"] == 121) # Median government transfers in 2020 among recipients ($)
                                           | (census_droped["CHARACTERISTIC_ID"] == 122) # Number of employment insurance benefits recipients aged 15 years and over in private households in 2020 - 100% data
                                           | (census_droped["CHARACTERISTIC_ID"] == 123) # Median employment insurance benefits in 2020 among recipients ($)
                                           | (census_droped["CHARACTERISTIC_ID"] == 124) # Number of COVID-19 emergency and recovery benefits recipients aged 15 years and over in private households in 2020 - 100% data
                                           | (census_droped["CHARACTERISTIC_ID"] == 125)] # Median COVID-19 emergency and recovery benefits in 2020 among recipients ($)
        return census_droped_short

   
    elif Name == 'census_total_income_2019':
        census_droped_short = census_droped[(census_droped["CHARACTERISTIC_ID"] == 204) # Total - Income statistics in 2019 for the population aged 15 years and over in private households - 100% data
                                           | (census_droped["CHARACTERISTIC_ID"] == 205) # Number of total income recipients aged 15 years and over in private households in 2019 - 100% data
                                           | (census_droped["CHARACTERISTIC_ID"] == 206) # Median total income in 2019 among recipients ($)
                                           | (census_droped["CHARACTERISTIC_ID"] == 207) # Number of after-tax income recipients aged 15 years and over in private households in 2019 - 100% data
                                           | (census_droped["CHARACTERISTIC_ID"] == 208) # Median after-tax income in 2019 among recipients ($)
                                           | (census_droped["CHARACTERISTIC_ID"] == 209) # Number of market income recipients aged 15 years and over in private households in 2019 - 100% data
                                           | (census_droped["CHARACTERISTIC_ID"] == 210) # Median market income in 2019 among recipients ($)
                                           | (census_droped["CHARACTERISTIC_ID"] == 211) # Number of employment income recipients aged 15 years and over in private households in 2019 - 100% data
                                           | (census_droped["CHARACTERISTIC_ID"] == 212) # Median employment income in 2019 among recipients ($)
                                           | (census_droped["CHARACTERISTIC_ID"] == 213) # Number of government transfers recipients aged 15 years and over in private households in 2019 - 100% data
                                           | (census_droped["CHARACTERISTIC_ID"] == 214) # Median government transfers in 2014 among recipients ($)
                                           | (census_droped["CHARACTERISTIC_ID"] == 215) # Number of employment insurance benefits recipients aged 15 years and over in private households in 2019 - 100% data
                                           | (census_droped["CHARACTERISTIC_ID"] == 216)] # Median employment insurance benefits in 2019 among recipients ($)
        return census_droped_short

    # Total household income information for the year 2020     
    elif Name == 'census_household_income_2020':
        census_droped_short = census_droped[(census_droped["CHARACTERISTIC_ID"] == 260) # Total - Household total income groups in 2020 for private households - 100% data
                            | (census_droped["CHARACTERISTIC_ID"] == 261) # Under $5,000
                            | (census_droped["CHARACTERISTIC_ID"] == 262) # $5,000 to $9,999
                            | (census_droped["CHARACTERISTIC_ID"] == 263) # $10,000 to $14,999
                            | (census_droped["CHARACTERISTIC_ID"] == 264) # $15,000 to $19,999
                            | (census_droped["CHARACTERISTIC_ID"] == 265) # $20,000 to $24,999
                            | (census_droped["CHARACTERISTIC_ID"] == 266) # $25,000 to $29,999
                            | (census_droped["CHARACTERISTIC_ID"] == 267) # $30,000 to $34,999
                            | (census_droped["CHARACTERISTIC_ID"] == 268) # $35,000 to $39,999                         
                            | (census_droped["CHARACTERISTIC_ID"] == 269) # $40,000 to $44,999
                            | (census_droped["CHARACTERISTIC_ID"] == 270) # $45,000 to $49,999
                            | (census_droped["CHARACTERISTIC_ID"] == 271) # $50,000 to $59,999
                            | (census_droped["CHARACTERISTIC_ID"] == 272) # $60,000 to $69,999
                            | (census_droped["CHARACTERISTIC_ID"] == 273) # $70,000 to $79,999
                            | (census_droped["CHARACTERISTIC_ID"] == 274) # $80,000 to $89,999
                            | (census_droped["CHARACTERISTIC_ID"] == 275) # $90,000 to $99,999
                            | (census_droped["CHARACTERISTIC_ID"] == 276) # $100,000 and over              
                            | (census_droped["CHARACTERISTIC_ID"] == 277) # $100,000 to $124,999
                            | (census_droped["CHARACTERISTIC_ID"] == 278) # $125,000 to $149,999
                            | (census_droped["CHARACTERISTIC_ID"] == 279) # $150,000 to $199,999
                            | (census_droped["CHARACTERISTIC_ID"] == 280)] # $200,000 and over
        return census_droped_short

    # Total household income after tax information for the year 2020  
    elif Name == 'census_household_income_after_tax_2020':
        census_droped_short = census_droped[(census_droped["CHARACTERISTIC_ID"] == 281) # Total - Household after-tax income groups in 2020 for private households - 100% data
                            | (census_droped["CHARACTERISTIC_ID"] == 282) # Under $5,000
                            | (census_droped["CHARACTERISTIC_ID"] == 283) # $5,000 to $9,999
                            | (census_droped["CHARACTERISTIC_ID"] == 284) # $10,000 to $14,999
                            | (census_droped["CHARACTERISTIC_ID"] == 285) # $15,000 to $19,999
                            | (census_droped["CHARACTERISTIC_ID"] == 286) # $20,000 to $24,999
                            | (census_droped["CHARACTERISTIC_ID"] == 287) # $25,000 to $29,999
                            | (census_droped["CHARACTERISTIC_ID"] == 288) # $30,000 to $34,999
                            | (census_droped["CHARACTERISTIC_ID"] == 289) # $35,000 to $39,999                         
                            | (census_droped["CHARACTERISTIC_ID"] == 290) # $40,000 to $44,999
                            | (census_droped["CHARACTERISTIC_ID"] == 291) # $45,000 to $49,999
                            | (census_droped["CHARACTERISTIC_ID"] == 292) # $50,000 to $59,999
                            | (census_droped["CHARACTERISTIC_ID"] == 293) # $60,000 to $69,999
                            | (census_droped["CHARACTERISTIC_ID"] == 294) # $70,000 to $79,999
                            | (census_droped["CHARACTERISTIC_ID"] == 295) # $80,000 to $89,999
                            | (census_droped["CHARACTERISTIC_ID"] == 296) # $90,000 to $99,999
                            | (census_droped["CHARACTERISTIC_ID"] == 297) # $100,000 and over              
                            | (census_droped["CHARACTERISTIC_ID"] == 298) # $100,000 to $124,999
                            | (census_droped["CHARACTERISTIC_ID"] == 299) # $125,000 to $149,999
                            | (census_droped["CHARACTERISTIC_ID"] == 300)] # $150,000 and over
        return census_droped_short   

    # Information on low income of the population
    elif Name == 'census_LIM_2020':
        census_droped_short = census_droped[(census_droped["CHARACTERISTIC_ID"] == 335) # Total - LIM low-income status in 2020 for the population in private households - 100% data
                            | (census_droped["CHARACTERISTIC_ID"] == 336) # 0 to 17 years
                            | (census_droped["CHARACTERISTIC_ID"] == 337) # 0 to 5 years
                            | (census_droped["CHARACTERISTIC_ID"] == 338) # 18 to 64 years
                            | (census_droped["CHARACTERISTIC_ID"] == 339) # 65 years and over
                            | (census_droped["CHARACTERISTIC_ID"] == 340) # In low income based on the Low-income measure, after tax (LIM-AT)
                            | (census_droped["CHARACTERISTIC_ID"] == 341) # 0 to 17 years
                            | (census_droped["CHARACTERISTIC_ID"] == 342) # 0 to 5 years
                            | (census_droped["CHARACTERISTIC_ID"] == 343) # 18 to 64 years                         
                            | (census_droped["CHARACTERISTIC_ID"] == 344) # 65 years and over
                            | (census_droped["CHARACTERISTIC_ID"] == 345) # Prevalence of low income based on the Low-income measure, after tax (LIM-AT) (%)
                            | (census_droped["CHARACTERISTIC_ID"] == 346) # 0 to 17 years (%)
                            | (census_droped["CHARACTERISTIC_ID"] == 347) # 0 to 5 years (%)
                            | (census_droped["CHARACTERISTIC_ID"] == 348) # 18 to 64 years (%)
                            | (census_droped["CHARACTERISTIC_ID"] == 349) # 65 years and over (%)
                            | (census_droped["CHARACTERISTIC_ID"] == 350) # Total - LICO low-income status in 2020 for the population in private households to whom the low-income concept is applicable - 100% data
                            | (census_droped["CHARACTERISTIC_ID"] == 351) # 0 to 17 years           
                            | (census_droped["CHARACTERISTIC_ID"] == 352) # 0 to 5 years
                            | (census_droped["CHARACTERISTIC_ID"] == 353) # 18 to 64 years
                            | (census_droped["CHARACTERISTIC_ID"] == 355) # In low income based on the Low-income cut-offs, after tax (LICO-AT)
                            | (census_droped["CHARACTERISTIC_ID"] == 356) # 0 to 17 years            
                            | (census_droped["CHARACTERISTIC_ID"] == 357) # 0 to 5 years
                            | (census_droped["CHARACTERISTIC_ID"] == 358) # 18 to 64 years
                            | (census_droped["CHARACTERISTIC_ID"] == 359) # 65 years and over (%)
                            | (census_droped["CHARACTERISTIC_ID"] == 360) # Prevalence of low income based on the Low-income cut-offs, after tax (LICO-AT) (%)   
                            | (census_droped["CHARACTERISTIC_ID"] == 361) # 0 to 17 years (%)
                            | (census_droped["CHARACTERISTIC_ID"] == 362) # 0 to 5 years
                            | (census_droped["CHARACTERISTIC_ID"] == 363) # 18 to 64 years
                            | (census_droped["CHARACTERISTIC_ID"] == 364)] # 65 years and over (%)
        return census_droped_short

    # Information on education level of people above 15 years
    elif Name == 'census_highest_certificate_15years':
        census_droped_short = census_droped[(census_droped["CHARACTERISTIC_ID"] == 1998) # Total - Highest certificate, diploma or degree for the population aged 15 years and over in private households - 25% sample data
                            | (census_droped["CHARACTERISTIC_ID"] == 1999) # No certificate, diploma or degree
                            | (census_droped["CHARACTERISTIC_ID"] == 2000) # High (secondary) school diploma or equivalency certificate
                            | (census_droped["CHARACTERISTIC_ID"] == 2001) # Postsecondary certificate, diploma or degree
                            | (census_droped["CHARACTERISTIC_ID"] == 2002) # Postsecondary certificate or diploma below bachelor level
                            | (census_droped["CHARACTERISTIC_ID"] == 2003) # Apprenticeship or trades certificate or diploma
                            | (census_droped["CHARACTERISTIC_ID"] == 2004) # Non-apprenticeship trades certificate or diploma
                            | (census_droped["CHARACTERISTIC_ID"] == 2005) # Apprenticeship certificate
                            | (census_droped["CHARACTERISTIC_ID"] == 2006) # College, CEGEP or other non-university certificate or diploma             
                            | (census_droped["CHARACTERISTIC_ID"] == 2007) # University certificate or diploma below bachelor level
                            | (census_droped["CHARACTERISTIC_ID"] == 2008) # Bachelor's degree or higher
                            | (census_droped["CHARACTERISTIC_ID"] == 2009) # Bachelor's degree
                            | (census_droped["CHARACTERISTIC_ID"] == 2010) # University certificate or diploma above bachelor level
                            | (census_droped["CHARACTERISTIC_ID"] == 2011) # Degree in medicine, dentistry, veterinary medicine or optometry
                            | (census_droped["CHARACTERISTIC_ID"] == 2012) # Master's degree
                            | (census_droped["CHARACTERISTIC_ID"] == 2013)] # Earned doctorate
        return census_droped_short

    # Information on education level of people between 25 and 64 years
    elif Name == 'census_highest_certificate_25_64years':
        census_droped_short = census_droped[(census_droped["CHARACTERISTIC_ID"] == 2014) # Total - Highest certificate, diploma or degree for the population aged 25 to 64 years in private households - 25% sample data
                            | (census_droped["CHARACTERISTIC_ID"] == 2015) # No certificate, diploma or degree
                            | (census_droped["CHARACTERISTIC_ID"] == 2016) # High (secondary) school diploma or equivalency certificate
                            | (census_droped["CHARACTERISTIC_ID"] == 2017) # Postsecondary certificate, diploma or degree
                            | (census_droped["CHARACTERISTIC_ID"] == 2018) # Postsecondary certificate or diploma below bachelor level
                            | (census_droped["CHARACTERISTIC_ID"] == 2019) # Apprenticeship or trades certificate or diploma
                            | (census_droped["CHARACTERISTIC_ID"] == 2020) # Non-apprenticeship trades certificate or diploma
                            | (census_droped["CHARACTERISTIC_ID"] == 2021) # Apprenticeship certificate
                            | (census_droped["CHARACTERISTIC_ID"] == 2022) # College, CEGEP or other non-university certificate or diploma             
                            | (census_droped["CHARACTERISTIC_ID"] == 2023) # University certificate or diploma below bachelor level
                            | (census_droped["CHARACTERISTIC_ID"] == 2024) # Bachelor's degree or higher
                            | (census_droped["CHARACTERISTIC_ID"] == 2025) # Bachelor's degree
                            | (census_droped["CHARACTERISTIC_ID"] == 2026) # University certificate or diploma above bachelor level
                            | (census_droped["CHARACTERISTIC_ID"] == 2027) # Degree in medicine, dentistry, veterinary medicine or optometry
                            | (census_droped["CHARACTERISTIC_ID"] == 2028) # Master's degree
                            | (census_droped["CHARACTERISTIC_ID"] == 2029)] # Earned doctorate
        return census_droped_short

    # Information on participation, employment and unemployment
    elif Name == 'census_employ':
        census_droped_short = census_droped[(census_droped["CHARACTERISTIC_ID"] == 2228) # Participation rate
                            | (census_droped["CHARACTERISTIC_ID"] == 2229) # Employment rate
                            | (census_droped["CHARACTERISTIC_ID"] == 2230)] # Unemployment rate
        return census_droped_short

        # Information on shelter-cost-to-income
    elif Name == 'census_shelter_cost':
        census_droped_short = census_droped[(census_droped["CHARACTERISTIC_ID"] == 1465) # Total - Owner and tenant households with household total income greater than zero, in non-farm, non-reserve private dwellings by shelter-cost-to-income ratio - 25% sample data
                            | (census_droped["CHARACTERISTIC_ID"] == 1466) #  Spending less than 30% of income on shelter costs
                            | (census_droped["CHARACTERISTIC_ID"] == 1467) #  Spending 30% or more of income on shelter costs
                            | (census_droped["CHARACTERISTIC_ID"] == 1468) #    30% to less than 100%
                            | (census_droped["CHARACTERISTIC_ID"] == 1469) # Total - Occupied private dwellings by housing indicators - 25% sample data
                            | (census_droped["CHARACTERISTIC_ID"] == 1470) #  Total - Households 'spending 30% or more of income on shelter costs' or 'not suitable' or 'major repairs needed'
                            | (census_droped["CHARACTERISTIC_ID"] == 1471) #    Spending 30% or more of income on shelter costs only 
                            | (census_droped["CHARACTERISTIC_ID"] == 1472) #    Not suitable only 
                            | (census_droped["CHARACTERISTIC_ID"] == 1473) #    Major repairs needed only 
                            | (census_droped["CHARACTERISTIC_ID"] == 1474) #    'Spending 30% or more of income on shelter costs' and 'not suitable' 
                            | (census_droped["CHARACTERISTIC_ID"] == 1475) #    'Spending 30% or more of income on shelter costs' and 'major repairs needed' 
                            | (census_droped["CHARACTERISTIC_ID"] == 1476) #    'Not suitable' and 'major repairs needed' 
                            | (census_droped["CHARACTERISTIC_ID"] == 1477) #    'Spending 30% or more of income on shelter costs' and 'not suitable' and 'major repairs needed' 
                            | (census_droped["CHARACTERISTIC_ID"] == 1478) #  Acceptable housing 
                            | (census_droped["CHARACTERISTIC_ID"] == 1479) #Total - Owner and tenant households with household total income greater than zero and shelter-cost-to-income ratio less than 100%, in non-farm, non-reserve private dwellings - 25% sample data
                            | (census_droped["CHARACTERISTIC_ID"] == 1480) #  In core need
                            | (census_droped["CHARACTERISTIC_ID"] == 1481)] #  Not in core need 
        return census_droped_short

        # Information on housing situation
    elif Name == 'census_housing_situation':
        census_droped_short = census_droped[(census_droped["CHARACTERISTIC_ID"] == 1482) # Total - Owner households in non-farm, non-reserve private dwellings - 25% sample data
                            | (census_droped["CHARACTERISTIC_ID"] == 1483) #  % of owner households with a mortgage  
                            | (census_droped["CHARACTERISTIC_ID"] == 1484) #  % of owner households spending 30% or more of its income on shelter costs  
                            | (census_droped["CHARACTERISTIC_ID"] == 1485) #  % in core housing need
                            | (census_droped["CHARACTERISTIC_ID"] == 1486) #  Median monthly shelter costs for owned dwellings ($)  
                            | (census_droped["CHARACTERISTIC_ID"] == 1487) #  Average monthly shelter costs for owned dwellings ($)  
                            | (census_droped["CHARACTERISTIC_ID"] == 1488) #  Median value of dwellings ($)
                            | (census_droped["CHARACTERISTIC_ID"] == 1489) #  Average value of dwellings ($)
                            | (census_droped["CHARACTERISTIC_ID"] == 1490) # Total - Tenant households in non-farm, non-reserve private dwellings - 25% sample data
                            | (census_droped["CHARACTERISTIC_ID"] == 1491) #  % of tenant households in subsidized housing
                            | (census_droped["CHARACTERISTIC_ID"] == 1492) #  % of tenant households spending 30% or more of its income on shelter costs 
                            | (census_droped["CHARACTERISTIC_ID"] == 1493) #  % in core housing need 
                            | (census_droped["CHARACTERISTIC_ID"] == 1494) #  Median monthly shelter costs for rented dwellings ($)
                            | (census_droped["CHARACTERISTIC_ID"] == 1495)] #  Average monthly shelter costs for rented dwellings ($) 
        return census_droped_short
    
        # Information on citizenship and immigration
    elif Name == 'census_citizenship':        
        census_droped_short = census_droped[(census_droped["CHARACTERISTIC_ID"] == 1522) # Total - Citizenship for the population in private households - 25% sample data
                            | (census_droped["CHARACTERISTIC_ID"] == 1523) # Canadian citizens   
                            | (census_droped["CHARACTERISTIC_ID"] == 1524) # Canadian citizens aged under 18
                            | (census_droped["CHARACTERISTIC_ID"] == 1525) # Canadian citizens aged 18 and over
                            | (census_droped["CHARACTERISTIC_ID"] == 1526)] # Not Canadian citizens
        return census_droped_short

        # Information on citizenship and immigration
    elif Name == 'cencus_immigtant_status':
        census_droped_short = census_droped[(census_droped["CHARACTERISTIC_ID"] == 1527) # Total - Immigrant status and period of immigration for the population in private households - 25% sample data
                            | (census_droped["CHARACTERISTIC_ID"] == 1528) # Non-immigrants
                            | (census_droped["CHARACTERISTIC_ID"] == 1529) # Immigrants  
                            | (census_droped["CHARACTERISTIC_ID"] == 1530) # Before 1980
                            | (census_droped["CHARACTERISTIC_ID"] == 1531) # 1980 to 1990
                            | (census_droped["CHARACTERISTIC_ID"] == 1532) # 1991 to 2000
                            | (census_droped["CHARACTERISTIC_ID"] == 1533) # 2001 to 2010
                            | (census_droped["CHARACTERISTIC_ID"] == 1534) # 2011 to 2021
                            | (census_droped["CHARACTERISTIC_ID"] == 1535) # 2011 to 2015
                            | (census_droped["CHARACTERISTIC_ID"] == 1536) # 2016 to 2021
                            | (census_droped["CHARACTERISTIC_ID"] == 1537)] # Non-permanent residents                                            
        return census_droped_short     

    
        # Information on religion
    elif Name == 'census_religion':
        census_droped_short = census_droped[(census_droped["CHARACTERISTIC_ID"] == 1949) # Total - Religion for the population in private households - 25% sample data
                            | (census_droped["CHARACTERISTIC_ID"] == 1950) # Buddhist  
                            | (census_droped["CHARACTERISTIC_ID"] == 1951) # Christian
                            | (census_droped["CHARACTERISTIC_ID"] == 1967) # Hindu
                            | (census_droped["CHARACTERISTIC_ID"] == 1968) # Jewish 
                            | (census_droped["CHARACTERISTIC_ID"] == 1969) # Muslim
                            | (census_droped["CHARACTERISTIC_ID"] == 1970) # Sikh
                            | (census_droped["CHARACTERISTIC_ID"] == 1971) # Traditional (North American Indigenous) spirituality
                            | (census_droped["CHARACTERISTIC_ID"] == 1972) # Other religions and spiritual traditions
                            | (census_droped["CHARACTERISTIC_ID"] == 1973)] # No religion and secular perspectives                                       
        return census_droped_short    

    elif Name == 'census_minority':        
        census_droped_short = census_droped[(census_droped["CHARACTERISTIC_ID"] == 1683) # Total - Visible minority for the population in private households - 25% sample data
                            | (census_droped["CHARACTERISTIC_ID"] == 1684) # Total visible minority population   
                            | (census_droped["CHARACTERISTIC_ID"] == 1685) # South Asian
                            | (census_droped["CHARACTERISTIC_ID"] == 1686) # Chinese
                            | (census_droped["CHARACTERISTIC_ID"] == 1687) # Black
                            | (census_droped["CHARACTERISTIC_ID"] == 1688) # Filipino
                            | (census_droped["CHARACTERISTIC_ID"] == 1689) # Arab
                            | (census_droped["CHARACTERISTIC_ID"] == 1690) # Latin American
                            | (census_droped["CHARACTERISTIC_ID"] == 1691) # Southeast Asian
                            | (census_droped["CHARACTERISTIC_ID"] == 1692) # West Asian
                            | (census_droped["CHARACTERISTIC_ID"] == 1693) # Korean
                            | (census_droped["CHARACTERISTIC_ID"] == 1694) # Japanese
                            | (census_droped["CHARACTERISTIC_ID"] == 1695) # Visible minority, n.i.e.
                            | (census_droped["CHARACTERISTIC_ID"] == 1696) # Multiple visible minorities
                            | (census_droped["CHARACTERISTIC_ID"] == 1697)] # Not a visible minority                                           
        return census_droped_short    

    else:
        return census_droped  # Or handle other cases here
    

    #     # Information on religion
    # elif Name == 'census_religion':        
    #     census_droped_short = census_droped[(census_droped["CHARACTERISTIC_ID"] == 1949) # Total - Religion for the population in private households - 25% sample data
    #                         | (census_droped["CHARACTERISTIC_ID"] == ) #    
    #                         | (census_droped["CHARACTERISTIC_ID"] == ) # 
    #                         | (census_droped["CHARACTERISTIC_ID"] == ) # 
    #                         | (census_droped["CHARACTERISTIC_ID"] == ) #    
    #                         | (census_droped["CHARACTERISTIC_ID"] == ) # 
    #                         | (census_droped["CHARACTERISTIC_ID"] == ) # 
    #                         | (census_droped["CHARACTERISTIC_ID"] == ) #   
    #                         | (census_droped["CHARACTERISTIC_ID"] == ) # 
    #                         | (census_droped["CHARACTERISTIC_ID"] == ) # 
    #                         | (census_droped["CHARACTERISTIC_ID"] == ) # 
    #                         | (census_droped["CHARACTERISTIC_ID"] == ) # 
    #                         | (census_droped["CHARACTERISTIC_ID"] == ) # 
    #                         | (census_droped["CHARACTERISTIC_ID"] == ) # 
    #                         | (census_droped["CHARACTERISTIC_ID"] == ) # 
    #                         | (census_droped["CHARACTERISTIC_ID"] == )] #                                             
    #     return census_droped_short 