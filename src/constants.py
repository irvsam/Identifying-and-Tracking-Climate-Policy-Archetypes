countries = [
    'ARG', 'AUS', 'AUT', 'BEL', 'CAN', 'CHL', 'CHN', 'COL', 'CRC', 
    'CZE', 'DEU', 'DNK', 'ESP', 'EST', 'FIN', 'FRA', 'GBR', 'GRC', 'HUN', 
    'IDN', 'IND', 'IRL', 'ISL', 'ISR', 'ITA', 'JPN', 'KOR', 'LTU', 'LUX', 
    'LVA', 'MEX', 'NOR', 'NZL', 'PER', 'POL', 'PRT', 'RUS', 'SAU', 
    'SVK', 'SVN', 'SWE', 'TUR', 'ZAF', 'CHE', 'NLD', 'HRV', 'BGR', 'ROU',
]

years = list(range(2000, 2021))

selected_oecd_policies = {
    # Energy
    'LEV3_ETS_E':           'ets_electricity',
    'LEV3_CARBONTAX_E':     'carbon_tax_electricity',
    'LEV3_BAN_PHOUT_COAL':  'coal_phaseout',
    'LEV3_RENEWABLE_EXP':   'renewables_expansion',
    'LEV4_FIT_SOL_PR':      'feed_in_tariff_solar',
    # Industry
    'LEV3_CARBONTAX_I':     'carbon_tax_industry',
    'LEV3_ETS_I':           'ets_industry',
    'LEV4_EE_MANDATE':      'energy_efficiency_mandate',
    # Buildings
    'LEV3_BC':              'building_energy_codes',
    'LEV3_BAN_PHOUT_HEAT':  'fossil_heating_phaseout',
    # Transport
    'LEV3_CARBONTAX_T':     'carbon_tax_transport',
    'LEV3_BAN_PHOUT_ICE':   'ice_vehicle_phaseout',
    'LEV3_CONG_CHARG':      'congestion_charge',
    # Cross-cutting
    'LEV3_NZ':              'net_zero_target',
    'LEV3_NDC':             'ndc',
    'LEV2_CROSS_SEC_CG':    'climate_governance',
    'LEV3_RDD_RES':         'rdd_renewables',
    'LEV3_FFS_PRODUCER':    'fossil_fuel_subsidy_reform',
    'LEV4_BAN_EXTRAC_STAT': 'fossil_extraction_ban',
}


wb_indicators = {
    'EG.USE.PCAP.KG.OE': 'energy_use_per_capita',
    'NY.GDP.MKTP.KD': 'gdp_constant_usd',
    'EG.ELC.RNWX.ZS': 'renewable_electricity_pct',
    'NY.GDP.PCAP.KD': 'gdp_per_capita_constant',
    'EG.FEC.RNEW.ZS': 'renewable_final_energy_pct',
    'EG.ELC.COAL.ZS': 'coal_electricity_pct' ,
    'EN.GHG.CO2.PC.CE.AR5': 'co2_emissions_per_capita',
    'EN.GHG.ALL.PC.CE.AR5': 'ghg_emissions_per_capita'


}