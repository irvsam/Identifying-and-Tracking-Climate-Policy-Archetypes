import pandas as pd
import wbgapi as wb
import requests
import glob
from io import StringIO
import os

# Data loading functions for World Bank, OECD, and EDGAR datasets.

#=========================================      World Bank Data    =========================================

# I don't use this at the moment because it's very simple to just do it in the notebook, but I might want to add more complex data processing here
def load_wdi(indicators, countries, start=2015, end=2025):
    """Fetches World Bank data."""
    df = wb.data.DataFrame(indicators.keys(), countries, time=range(start, end+1), labels=False)
    return df.rename(columns=indicators)

#=========================================      OECD data   =========================================

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

def load_oecd_data(url, policy_list):
    """Fetches OECD data and immediately filters for selected policies."""
    response = requests.get(url)
    df = pd.read_csv(StringIO(response.text))
    
    # Filter the DataFrame to only include your selected policy IDs
    filtered_df = df[df['CLIM_ACT_POL'].isin(policy_list)]
    return filtered_df


#=========================================      Edgar Data    =========================================

EDGAR_SECTOR_MAP = {
    'ENE': 'Power industry',
    'IND': 'Combustion for manufacturing',
    'TRO': 'Road transportation',
    'RCO': 'Energy for buildings',
    # ... add others 
}

def get_edgar_citation():
    """Returns the mandatory citation for EDGAR 2025 data."""
    return (
        "Emissions Database for Global Atmospheric Research (EDGAR), "
        "release EDGAR_2025_GHG (1970 - 2024) of September 2025. "
        "European Commission, Joint Research Centre (JRC). "
        "DOI: 10.2760/9816914"
    )


def clean_edgar_data(df):
    """Standardizes sectors using the mapping above."""
    if 'sector' in df.columns:
        df['sector_name'] = df['sector'].map(EDGAR_SECTOR_MAP)
    return df


def load_edgar_data(directory='../data/raw/', sheet_name=3, skiprows=9, countries=None):
    """
    Loads Excel files, skips metadata, and filters by specific country codes.
    """
    search_path = os.path.join(directory, "*.xlsx")
    files = glob.glob(search_path)
    
    if not files:
        print(f"DEBUG: No Excel files found in {os.path.abspath(directory)}")
        return None
    
    df = pd.read_excel(files[0], sheet_name=sheet_name, skiprows=skiprows)
    
    # Standardize column name if necessary (common EDGAR issue)
    # Check if a common country column exists, usually 'Country_code_A3'
    if 'Country_code_A3' in df.columns and countries is not None:
        df = df[df['Country_code_A3'].isin(countries)]
        
    return df



#=========================================      All data    =========================================

def load_all_climate_data(wb_indicators, wb_countries, oecd_url, edgar_dir):
    """Orchestrates loading all three data sources into a dictionary of DataFrames."""
    return {
        'wb': load_wdi(wb_indicators, wb_countries),
        'oecd': load_oecd_data(oecd_url, selected_oecd_policies),
        'edgar': load_edgar_data(directory=edgar_dir, countries=wb_countries)
    }