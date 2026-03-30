import pandas as pd
import wbgapi as wb
import requests
import glob
from io import StringIO
import os

from constants import selected_oecd_policies

# Data loading functions 

#=========================================      World Bank Data    =========================================

# I don't use this at the moment because it's very simple to just do it in the notebook, but I might want to add more complex data processing here
def load_wdi(indicators, countries, start=2015, end=2025):
    """Fetches World Bank data."""
    df = wb.data.DataFrame(indicators.keys(), countries, time=range(start, end+1), labels=False)
    return df.rename(columns=indicators)

#=========================================      OECD data   =========================================



def load_oecd_data(url, policy_list=selected_oecd_policies):
    """Fetches OECD data and immediately filters for selected policies."""
    response = requests.get(url)
    df = pd.read_csv(StringIO(response.text))
    
    # Filter the DataFrame to only include selected policy IDs
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

def load_edgar_data(directory='../data/raw/', sheet_name=3, skiprows=9, countries=None, start_year=2015, end_year=2025):
    """
    Loads Excel files, skips metadata, and filters by specific country codes and year columns.
    """
    search_path = os.path.join(directory, "*.xlsx")
    files = glob.glob(search_path)
    
    if not files:
        print(f"DEBUG: No Excel files found in {os.path.abspath(directory)}")
        return None
    
    # Load raw data
    df = pd.read_excel(files[0], sheet_name=sheet_name, skiprows=skiprows)
    
    # Filter by country
    if countries is not None and 'Country_code_A3' in df.columns:
        df = df[df['Country_code_A3'].isin(countries)]
    
    # Subset to only keep the year columns we want
    desired_years = [f'Y_{y}' for y in range(start_year, end_year + 1)]
    
    # Keep non-year columns (ID columns) plus our target year columns
    id_cols = [c for c in df.columns if not str(c).startswith('Y_')]
    available_years = [c for c in df.columns if c in desired_years]
    
    return df[id_cols + available_years]



#=========================================      All data    =========================================

def load_all_climate_data(wb_indicators, wb_countries, oecd_url, edgar_dir):
    """Orchestrates loading all three data sources into a dictionary of DataFrames."""
    return {
        'wb': load_wdi(wb_indicators, wb_countries),
        'oecd': load_oecd_data(oecd_url, selected_oecd_policies),
        'edgar': load_edgar_data(directory=edgar_dir, countries=wb_countries)
    }