countries = [
    'ARG', 'AUS', 'AUT', 'BEL', 'BRA', 'CAN', 'CHL', 'CHN', 'COL', 'CRC', 
    'CZE', 'DEU', 'DNK', 'ESP', 'EST', 'FIN', 'FRA', 'GBR', 'GRC', 'HUN', 
    'IDN', 'IND', 'IRL', 'ISL', 'ISR', 'ITA', 'JPN', 'KOR', 'LTU', 'LUX', 
    'LVA', 'MEX', 'NOR', 'NZL', 'PER', 'PHL', 'POL', 'PRT', 'RUS', 'SAU', 
    'SVK', 'SVN', 'SWE', 'TUR', 'USA', 'ZAF', 'CHE', 'NLD', 'SGP', 'VNM'
]

years = list(range(2000, 2021))

selected_oecd_policies = {
    'LEV4_CARBONTAX_T':     'carbon_tax_transport',
    'LEV3_BAN_PHOUT_COAL':  'coal_phaseout',
    'LEV4_EE_MANDATE':      'energy_efficiency_mandate',
    'LEV4_ETS_E_GHG':       'ets_electricity',
    'LEV4_CONG_CHARG':      'congestion_charge',
    'LEV3_NZ':              'net_zero_target',
    'LEV2_CROSS_SEC_CG':    'climate_governance',
    'LEV3_CARBONTAX_I':     'carbon_tax_industry',
    'LEV4_BAN_EXTRAC_STAT': 'fossil_extraction_ban',
    'LEV4_FIT_SOL_PR':      'feed_in_tariff_solar',
    'LEV4_RENEWABLE_EXP':   'renewables_expansion',
    'LEV4_BAN_COAL_STAT':   'coal_ban_status',
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