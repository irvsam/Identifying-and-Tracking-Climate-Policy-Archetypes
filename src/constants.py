countries = ['ARG', 'AUS', 'CAN', 'CHN', 'FRA', 'DEU', 'IND', 
             'IDN', 'ITA', 'JPN', 'MEX', 'RUS', 'SAU', 'ZAF', 'KOR', 
             'TUR', 'GBR' ]

years = list(range(2015, 2021))

selected_oecd_policies = [
    'LEV4_CARBONTAX_T',  # Carbon Tax Transport
    'LEV3_BAN_PHOUT_COAL', # Coal phase-out
    'LEV4_EE_MANDATE',   # Energy Efficiency Mandates
    'LEV4_ETS_E_GHG',   # Emissions Trading System (Energy)
    'LEV4_NZ_DATE' , # Net Zero Target Year
    'LEV4_CONG_CHARGE', # Congestion Charge
    'LEV3_NZ', # Net Zero Target
    'LEV2_CROSS_SEC_CG', #Climate governance
    'LEV3_CARBONTAX_I', # Carbon Tax Industry
    'LEV4_BAN_EXTRAC_DATE', # Bans on Fossil Fuel Extraction (with date)
    'LEV4_FIT_SOL_PR', # Feed-in Tariffs for Solar PV
    'LEV4_RENEWABLE_EXP', # Planning Renewables Expansion
    'LEV4_BAN_EXTRAC_DATE', # Bans on Fossil Fuel Extraction (with date)
    'LEV4_BAN_COAL_STAT', # Ban on the construction of coal power plants - legal status
]


wb_indicators = {
    'EG.USE.PCAP.KG.OE': 'energy_use_per_capita',
    'NY.GDP.MKTP.KD': 'gdp_constant_usd',
    'EG.ELC.RNWX.ZS': 'renewable_electricity_pct',
    'NY.GDP.PCAP.KD': 'gdp_per_capita_constant',
    'EG.FEC.RNEW.ZS': 'renewable_final_energy_pct',
    'EG.ELC.COAL.ZS': 'coal_electricity_pct' ,
    'EN.ATM.CO2E.PP.GD': 'co2_emissions_per_gdp',

}