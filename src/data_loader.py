import pandas as pd
import wbgapi as wb
import requests
import glob
from io import StringIO

# Data loading functions for World Bank, OECD, and EDGAR datasets.

# I don't use this at the moment because it's very simple to just do it in the notebook, but I might want to add more complex data processing here
def load_wdi(indicators, countries, start=2015, end=2025):
    """Fetches World Bank data."""
    df = wb.data.DataFrame(indicators.keys(), countries, time=range(start, end+1), labels=False)
    return df.rename(columns=indicators)

# This is a bit more complex because the OECD data is in SDMX format TODO: need to filter more based on which variables I actually want to use
def load_oecd_data(url):
    response = requests.get(url)
    return pd.read_csv(StringIO(response.text))

def get_edgar_citation():
    """Returns the mandatory citation for EDGAR 2025 data."""
    return (
        "Emissions Database for Global Atmospheric Research (EDGAR), "
        "release EDGAR_2025_GHG (1970 - 2024) of September 2025. "
        "European Commission, Joint Research Centre (JRC). "
        "DOI: 10.2760/9816914"
    )

EDGAR_SECTOR_MAP = {
    'ENE': 'Power industry',
    'IND': 'Combustion for manufacturing',
    'TRO': 'Road transportation',
    'RCO': 'Energy for buildings',
    # ... add others 
}

def clean_edgar_data(df):
    """Standardizes sectors using the mapping above."""
    if 'sector' in df.columns:
        df['sector_name'] = df['sector'].map(EDGAR_SECTOR_MAP)
    return df


import glob
import pandas as pd
import os

def load_edgar_data(directory='../data/raw/', sheet_name=3, skiprows=9):
    """
    Loads Excel files, skipping metadata rows.
    skiprows=9: Skips the first 9 rows, making the 10th row the header.
    """
    search_path = os.path.join(directory, "*.xlsx")
    files = glob.glob(search_path)
    
    if not files:
        print(f"DEBUG: No Excel files found in {os.path.abspath(directory)}")
        return None
    
    # Pass the skiprows parameter to read_excel
    return pd.read_excel(files[0], sheet_name=sheet_name, skiprows=skiprows)



def load_all_climate_data(wb_indicators, wb_countries, oecd_url, edgar_dir):
    """Orchestrates loading all three data sources into a dictionary of DataFrames."""
    return {
        'wb': load_wdi(wb_indicators, wb_countries),
        'oecd': load_oecd_data(oecd_url),
        'edgar': load_edgar_data(directory=edgar_dir)
    }