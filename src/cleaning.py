import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler, PowerTransformer

def clean_and_engineer(input_path):
    df = pd.read_csv(input_path)
    
    # Handle Negatives 
    pct_cols = ['renewable_electricity_pct', 'renewable_final_energy_pct', 'coal_electricity_pct']
    for col in pct_cols:
        df[col] = df[col].clip(lower=0)


    # Log-transform skewed data
    df['log_gdp_pc'] = np.log1p(df['gdp_per_capita_constant'])
    df['log_energy_pc'] = np.log1p(df['energy_use_per_capita'])

    # Feature Selection
    # Dropping raw economic values and the redundant NZ_DATE
    to_drop = ['gdp_constant_usd', 'gdp_per_capita_constant', 'energy_use_per_capita', 'LEV4_NZ_DATE']
    df_clean = df.drop(columns=to_drop)
    
    return df_clean

def preprocess_for_ml(df, method='standard', type = 'temporal'):
    if type == 'temporal': 
        
        
        # Separate identifiers from features
        identifiers = df[['country_code', 'Name', 'year']]
        features = df.drop(columns=['country_code', 'Name', 'year'])
        
        if method == 'power':
            transformer = PowerTransformer(method='yeo-johnson')
            X_scaled = transformer.fit_transform(features)
        else:
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(features)

        # Re-attach identifiers so we don't lose track of countries!
        processed_df = pd.DataFrame(X_scaled, columns=features.columns)
        final_df = pd.concat([identifiers.reset_index(drop=True), processed_df], axis=1)
        
        
    else:
        # Separate identifiers from features
        identifiers = df[['country_code', 'Name']]
        features = df.drop(columns=['country_code', 'Name'])
        
        if method == 'power':
            transformer = PowerTransformer(method='yeo-johnson')
            X_scaled = transformer.fit_transform(features)
        else:
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(features)

        # Re-attach identifiers so we don't lose track of countries!
        processed_df = pd.DataFrame(X_scaled, columns=features.columns)
        final_df = pd.concat([identifiers.reset_index(drop=True), processed_df], axis=1)

    return final_df

    

# --- EXECUTION ---
if __name__ == "__main__":
    raw_path_averaged = 'data/processed/climate_archetypes_avg.csv'
    raw_path_temporal = 'data/processed/climate_trajectories_long.csv'
    output_path_averaged = 'data/processed/avg_cleaned_feature_matrix.csv'
    output_path_temporal = 'data/processed/temporal_cleaned_feature_matrix.csv'
    
    print("Engineering features...")
    df_engineered_averaged = clean_and_engineer(raw_path_averaged)
    df_engineered_temporal = clean_and_engineer(raw_path_temporal)
    
    print("Scaling data...")
    df_final_averaged = preprocess_for_ml(df_engineered_averaged, method='power', type = 'averaged')
    df_final_temporal = preprocess_for_ml(df_engineered_temporal, method = 'power')
    
    df_final_averaged.to_csv(output_path_averaged, index=False)
    df_final_temporal.to_csv(output_path_temporal, index=False)
    print(f"Success! Prepared {df_final_averaged.shape[0]} rows and {df_final_averaged.shape[1]} features for averaged data and  {df_final_temporal.shape[0]} rows and {df_final_temporal.shape[1]} features for temporal data.")