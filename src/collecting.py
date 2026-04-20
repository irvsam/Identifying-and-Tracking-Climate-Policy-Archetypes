import pandas as pd
import wbgapi as wb
import os
import sys



# Get the directory where the script is located (src)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the project root (one level up from src)
project_root = os.path.abspath(os.path.join(current_dir, '..'))

# Add the project root to sys.path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.constants import countries, years, wb_indicators, selected_oecd_policies
from src.data_loader import load_oecd_data

class ClimateDataFactory:
    def __init__(self):
        self.countries = countries
        self.years = years
        self.wb_indicators = wb_indicators
        self.oecd_url =oecd_url = "https://sdmx.oecd.org/public/rest/data/OECD.ENV.EPI,DSD_CAPMF@DF_CAPMF,1.0/ARG+AUS+BRA+CAN+CHN+FRA+DEU+IND+IDN+ITA+JPN+MEX+RUS+SAU+ZAF+KOR+TUR+USA+GBR.A.POL_STRINGENCY+POL_COUNT.LEV1_SEC+LEV1_CROSS_SEC+LEV1_INT+LEV2_SEC_E_MBI+LEV2_SEC_E_NMBI+LEV2_SEC_I_MBI+LEV2_SEC_I_NMBI+LEV2_SEC_B_MBI+LEV2_SEC_B_NMBI+LEV2_SEC_T_MBI+LEV2_SEC_T_NMBI+LEV2_CROSS_SEC_GHGTAR+LEV2_CROSS_SEC_RDD+LEV2_CROSS_SEC_FFPP+LEV2_CROSS_SEC_CG+LEV2_INT_C_COORD+LEV2_INT_C_FIN+LEV2_INT_GHGREP+LEV3_ETS_E+LEV3_CARBONTAX_E+LEV3_FFS_E+LEV3_EXCISETAX_E+LEV3_FIT+LEV3_AUCTION+LEV3_RECS+LEV3_BAN_PHOUT_COAL+LEV3_RENEWABLE_EXP+LEV3_EMIS_STD+LEV3_ETS_I+LEV3_CARBONTAX_I+LEV3_FFS_I+LEV3_EXCISETAX_I+LEV3_FIN_MECH_I+LEV3_MEPS_MOTOR+LEV3_EE_MANDATE+LEV3_ETS_B+LEV3_CARBONTAX_B+LEV3_FFS_B+LEV3_EXCISETAX_B+LEV3_FIN_MECH_B+LEV3_MEPS_APPL+LEV3_BC+LEV3_BAN_PHOUT_HEAT+LEV3_LABEL_APPL+LEV3_CONG_CHARG+LEV3_ETS_T+LEV3_CARBONTAX_T+LEV3_FFS_T+LEV3_EXCISETAX_T+LEV3_MEPS_T+LEV3_LABEL_CAR+LEV3_EXP_RAIL+LEV3_SPEED+LEV3_BAN_PHOUT_ICE+LEV3_NDC+LEV3_NZ+LEV3_RDD_EE+LEV3_RDD_CCS+LEV3_RDD_RES+LEV3_RDD_NUC+LEV3_RDD_HYDR+LEV3_RDD_OTHER+LEV3_BAN_PHOUT_EXTRAC+LEV3_FFS_PRODUCER+LEV3_METHAN+LEV3_AB+LEV3_TREATY+LEV3_INT_INIT+LEV3_PR_AV_MAR+LEV3_BAN_CREDIT+LEV3_BAN_FF_ABROAD+LEV3_EVAL_BR+LEV3_UNFCCC+LEV3_GHG_ACC+LEV4_FIT_SOL_PR+LEV4_FIT_SOL_DUR+LEV4_FIT_WIND_PR+LEV4_FIT_WIND_DUR+LEV4_AUCTION_SOL_PR+LEV4_AUCTION_SOL_DUR+LEV4_AUCTION_WIND_PR+LEV4_AUCTION_WIND_DUR+LEV4_RECS+LEV4_ETS_E_PR+LEV4_ETS_E_GHG+LEV4_CARBONTAX_E_PR+LEV4_FFS_E+LEV4_EXCISETAX_E_COAL+LEV4_EXCISETAX_E_NATGAS+LEV4_BAN_COAL_DATE+LEV4_BAN_COAL_STAT+LEV4_PHOUT_COAL_DATE+LEV4_PHOUT_COAL_STAT+LEV4_RENEWABLE_EXP+LEV4_EMIS_STD_NOX+LEV4_EMIS_STD_SOX+LEV4_EMIS_STD_PM+LEV4_ETS_I_PR+LEV4_ETS_I_GHG+LEV4_CARBONTAX_I+LEV4_FFS_I+LEV4_EXCISETAX_I_COAL+LEV4_EXCISETAX_I_NATGAS+LEV4_EXCISETAX_I_DIESEL+LEV4_FIN_MECH_I+LEV4_MEPS_MOTOR+LEV4_EE_MANDATE+LEV4_ETS_B_PR+LEV4_ETS_B_GHG+LEV4_CARBONTAX_B+LEV4_FFS_B+LEV4_EXCISETAX_B_C_COAL+LEV4_EXCISETAX_B_R_COAL+LEV4_EXCISETAX_B_C_DIESEL+LEV4_EXCISETAX_B_R_DIESEL+LEV4_EXCISETAX_B_C_LPG+LEV4_EXCISETAX_B_R_LPG+LEV4_EXCISETAX_B_C_NATGAS+LEV4_EXCISETAX_B_R_NATGAS+LEV4_FIN_MECH_B_R+LEV4_FIN_MECH_B_C+LEV4_MEPS_FRE+LEV4_MEPS_REF+LEV4_MEPS_LIGHT+LEV4_MEPS_AC+LEV4_BC_RES+LEV4_BC_NON_RES+LEV4_BAN_OIL_DATE+LEV4_BAN_OIL_STAT+LEV4_BAN_GAS_DATE+LEV4_BAN_GAS_STAT+LEV4_PHOUT_OIL_DATE+LEV4_PHOUT_OIL_STAT+LEV4_PHOUT_GAS_DATE+LEV4_PHOUT_GAS_STAT+LEV4_LABEL_FRE+LEV4_LABEL_REF+LEV4_LABEL_LIGHT+LEV4_LABEL_AC+LEV4_CONG_CHARG+LEV4_ETS_T_PR+LEV4_ETS_T_GHG+LEV4_CARBONTAX_T+LEV4_FFS_T+LEV4_EXCISETAX_T_DIESEL+LEV4_EXCISETAX_T_GASO+LEV4_MEPS_LDV+LEV4_MEPS_HDV+LEV4_LABEL_CAR+LEV4_EXP_RAIL+LEV4_SPEED+LEV4_BAN_ICE_DATE+LEV4_BAN_ICE_STAT+LEV4_PHOUT_ICE_DATE+LEV4_PHOUT_ICE_STAT+LEV4_NDC_LULUCF+LEV4_NDC_SCOPE_SEC+LEV4_NDC_SCOPE_EMIS+LEV4_NDC_SING_MULT+LEV4_NDC_TARG_TYPE+LEV4_NDC_DET+LEV4_NZ_GHG_SCOPE+LEV4_NZ_SEC_SCOPE+LEV4_NZ_DATE+LEV4_NZ_STAT+LEV4_RDD_EE+LEV4_RDD_CCS+LEV4_RDD_RES+LEV4_RDD_NUC+LEV4_RDD_HYDR+LEV4_RDD_OTHER+LEV4_BAN_EXTRAC_DATE+LEV4_BAN_EXTRAC_STAT+LEV4_PHOUT_EXTRAC_DATE+LEV4_PHOUT_EXTRAC_STAT+LEV4_FFS_PRODUCER+LEV4_METHAN+LEV4_AB_ESTABL+LEV4_AB_ESTABL_LAW+LEV4_AB_SECR_MEM+LEV4_AB_COUNC_MEM+LEV4_AB_BUDGET+LEV4_TREATY_UNFCCC+LEV4_TREATY_MONTREALPROT+LEV4_TREATY_MONTREALAMEND+LEV4_TREATY_KIGALI+LEV4_TREATY_KYOTO+LEV4_TREATY_PARIS+LEV4_INT_INIT+LEV4_PR_AV+LEV4_PR_MAR+LEV4_PR_CORSIA+LEV4_BAN_CREDIT_STAT+LEV4_BAN_CREDIT_DATE+LEV4_BAN_FF_ABROAD_STAT+LEV4_BAN_FF_ABROAD_DATE+LEV4_EVAL_BR+LEV4_UNFCCC_GHGINV+LEV4_UNFCCC_BR+LEV4_UNFCCC_NC+LEV4_UNFCCC_NDC+LEV4_UNFCCC_LTLEDS+LEV4_GHG_ACC_ANNEX+LEV4_GHG_ACC_SEEA.PL+0_TO_10?startPeriod=2015&endPeriod=2023&dimensionAtObservation=AllDimensions&format=csvfilewithlabels"
    def fetch_nd_gain(self, path='data/raw/gain.csv'):
        print("Processing ND-GAIN data...")
        df = pd.read_csv(path)
        df = df[df['ISO3'].isin(self.countries)]
        df_melted = df.melt(id_vars=['ISO3', 'Name'], var_name='year', value_name='nd_gain_score')
        df_melted['year'] = df_melted['year'].astype(int)
        df_melted = df_melted[df_melted['year'].isin(self.years)]
        return df_melted.rename(columns={'ISO3': 'country_code'})

    def fetch_world_bank(self):
        print("Fetching World Bank Indicators...")
        df = wb.data.DataFrame(self.wb_indicators.keys(), self.countries, time=self.years)
        df = df.rename(columns=self.wb_indicators).reset_index()
        
        # Transform from WB format to Long format
        df_melted = df.melt(id_vars=['economy', 'series'], var_name='year', value_name='value')
        df_melted['series'] = df_melted['series'].map(self.wb_indicators)
        df_final = df_melted.pivot_table(index=['economy', 'year'], columns='series', values='value').reset_index()
        df_final['year'] = df_final['year'].str.replace('YR', '').astype(int)
        return df_final.rename(columns={'economy': 'country_code'})

    def fetch_oecd_policy(self):
        print("Fetching OECD Policy Data...")

        # DYNAMICALLY build the country string for the URL
        country_str = "+".join(self.countries)
    
        # Construct the URL with the new country list
        dynamic_url = f"https://sdmx.oecd.org/public/rest/data/OECD.ENV.EPI,DSD_CAPMF@DF_CAPMF,1.0/{country_str}.A.POL_STRINGENCY+POL_COUNT.LEV1_SEC+LEV1_CROSS_SEC+LEV1_INT+LEV2_SEC_E_MBI+LEV2_SEC_E_NMBI+LEV2_SEC_I_MBI+LEV2_SEC_I_NMBI+LEV2_SEC_B_MBI+LEV2_SEC_B_NMBI+LEV2_SEC_T_MBI+LEV2_SEC_T_NMBI+LEV2_CROSS_SEC_GHGTAR+LEV2_CROSS_SEC_RDD+LEV2_CROSS_SEC_FFPP+LEV2_CROSS_SEC_CG+LEV2_INT_C_COORD+LEV2_INT_C_FIN+LEV2_INT_GHGREP+LEV3_ETS_E+LEV3_CARBONTAX_E+LEV3_FFS_E+LEV3_EXCISETAX_E+LEV3_FIT+LEV3_AUCTION+LEV3_RECS+LEV3_BAN_PHOUT_COAL+LEV3_RENEWABLE_EXP+LEV3_EMIS_STD+LEV3_ETS_I+LEV3_CARBONTAX_I+LEV3_FFS_I+LEV3_EXCISETAX_I+LEV3_FIN_MECH_I+LEV3_MEPS_MOTOR+LEV3_EE_MANDATE+LEV3_ETS_B+LEV3_CARBONTAX_B+LEV3_FFS_B+LEV3_EXCISETAX_B+LEV3_FIN_MECH_B+LEV3_MEPS_APPL+LEV3_BC+LEV3_BAN_PHOUT_HEAT+LEV3_LABEL_APPL+LEV3_CONG_CHARG+LEV3_ETS_T+LEV3_CARBONTAX_T+LEV3_FFS_T+LEV3_EXCISETAX_T+LEV3_MEPS_T+LEV3_LABEL_CAR+LEV3_EXP_RAIL+LEV3_SPEED+LEV3_BAN_PHOUT_ICE+LEV3_NDC+LEV3_NZ+LEV3_RDD_EE+LEV3_RDD_CCS+LEV3_RDD_RES+LEV3_RDD_NUC+LEV3_RDD_HYDR+LEV3_RDD_OTHER+LEV3_BAN_PHOUT_EXTRAC+LEV3_FFS_PRODUCER+LEV3_METHAN+LEV3_AB+LEV3_TREATY+LEV3_INT_INIT+LEV3_PR_AV_MAR+LEV3_BAN_CREDIT+LEV3_BAN_FF_ABROAD+LEV3_EVAL_BR+LEV3_UNFCCC+LEV3_GHG_ACC+LEV4_FIT_SOL_PR+LEV4_FIT_SOL_DUR+LEV4_FIT_WIND_PR+LEV4_FIT_WIND_DUR+LEV4_AUCTION_SOL_PR+LEV4_AUCTION_SOL_DUR+LEV4_AUCTION_WIND_PR+LEV4_AUCTION_WIND_DUR+LEV4_RECS+LEV4_ETS_E_PR+LEV4_ETS_E_GHG+LEV4_CARBONTAX_E_PR+LEV4_FFS_E+LEV4_EXCISETAX_E_COAL+LEV4_EXCISETAX_E_NATGAS+LEV4_BAN_COAL_DATE+LEV4_BAN_COAL_STAT+LEV4_PHOUT_COAL_DATE+LEV4_PHOUT_COAL_STAT+LEV4_RENEWABLE_EXP+LEV4_EMIS_STD_NOX+LEV4_EMIS_STD_SOX+LEV4_EMIS_STD_PM+LEV4_ETS_I_PR+LEV4_ETS_I_GHG+LEV4_CARBONTAX_I+LEV4_FFS_I+LEV4_EXCISETAX_I_COAL+LEV4_EXCISETAX_I_NATGAS+LEV4_EXCISETAX_I_DIESEL+LEV4_FIN_MECH_I+LEV4_MEPS_MOTOR+LEV4_EE_MANDATE+LEV4_ETS_B_PR+LEV4_ETS_B_GHG+LEV4_CARBONTAX_B+LEV4_FFS_B+LEV4_EXCISETAX_B_C_COAL+LEV4_EXCISETAX_B_R_COAL+LEV4_EXCISETAX_B_C_DIESEL+LEV4_EXCISETAX_B_R_DIESEL+LEV4_EXCISETAX_B_C_LPG+LEV4_EXCISETAX_B_R_LPG+LEV4_EXCISETAX_B_C_NATGAS+LEV4_EXCISETAX_B_R_NATGAS+LEV4_FIN_MECH_B_R+LEV4_FIN_MECH_B_C+LEV4_MEPS_FRE+LEV4_MEPS_REF+LEV4_MEPS_LIGHT+LEV4_MEPS_AC+LEV4_BC_RES+LEV4_BC_NON_RES+LEV4_BAN_OIL_DATE+LEV4_BAN_OIL_STAT+LEV4_BAN_GAS_DATE+LEV4_BAN_GAS_STAT+LEV4_PHOUT_OIL_DATE+LEV4_PHOUT_OIL_STAT+LEV4_PHOUT_GAS_DATE+LEV4_PHOUT_GAS_STAT+LEV4_LABEL_FRE+LEV4_LABEL_REF+LEV4_LABEL_LIGHT+LEV4_LABEL_AC+LEV4_CONG_CHARG+LEV4_ETS_T_PR+LEV4_ETS_T_GHG+LEV4_CARBONTAX_T+LEV4_FFS_T+LEV4_EXCISETAX_T_DIESEL+LEV4_EXCISETAX_T_GASO+LEV4_MEPS_LDV+LEV4_MEPS_HDV+LEV4_LABEL_CAR+LEV4_EXP_RAIL+LEV4_SPEED+LEV4_BAN_ICE_DATE+LEV4_BAN_ICE_STAT+LEV4_PHOUT_ICE_DATE+LEV4_PHOUT_ICE_STAT+LEV4_NDC_LULUCF+LEV4_NDC_SCOPE_SEC+LEV4_NDC_SCOPE_EMIS+LEV4_NDC_SING_MULT+LEV4_NDC_TARG_TYPE+LEV4_NDC_DET+LEV4_NZ_GHG_SCOPE+LEV4_NZ_SEC_SCOPE+LEV4_NZ_DATE+LEV4_NZ_STAT+LEV4_RDD_EE+LEV4_RDD_CCS+LEV4_RDD_RES+LEV4_RDD_NUC+LEV4_RDD_HYDR+LEV4_RDD_OTHER+LEV4_BAN_EXTRAC_DATE+LEV4_BAN_EXTRAC_STAT+LEV4_PHOUT_EXTRAC_DATE+LEV4_PHOUT_EXTRAC_STAT+LEV4_FFS_PRODUCER+LEV4_METHAN+LEV4_AB_ESTABL+LEV4_AB_ESTABL_LAW+LEV4_AB_SECR_MEM+LEV4_AB_COUNC_MEM+LEV4_AB_BUDGET+LEV4_TREATY_UNFCCC+LEV4_TREATY_MONTREALPROT+LEV4_TREATY_MONTREALAMEND+LEV4_TREATY_KIGALI+LEV4_TREATY_KYOTO+LEV4_TREATY_PARIS+LEV4_INT_INIT+LEV4_PR_AV+LEV4_PR_MAR+LEV4_PR_CORSIA+LEV4_BAN_CREDIT_STAT+LEV4_BAN_CREDIT_DATE+LEV4_BAN_FF_ABROAD_STAT+LEV4_BAN_FF_ABROAD_DATE+LEV4_EVAL_BR+LEV4_UNFCCC_GHGINV+LEV4_UNFCCC_BR+LEV4_UNFCCC_NC+LEV4_UNFCCC_NDC+LEV4_UNFCCC_LTLEDS+LEV4_GHG_ACC_ANNEX+LEV4_GHG_ACC_SEEA.PL+0_TO_10?startPeriod=2015&endPeriod=2023&dimensionAtObservation=AllDimensions&format=csvfilewithlabels"

        df = load_oecd_data(dynamic_url)
        df['TIME_PERIOD'] = df['TIME_PERIOD'].astype(int)
        
        # Filter for Stringency measures and Pivot
        df_stringency = df[df['Measure'].str.contains('Policy stringency')]
    
        df_wide = df_stringency.pivot_table(
            index=['REF_AREA', 'TIME_PERIOD'], 
            columns='CLIM_ACT_POL', 
            values='OBS_VALUE'
        ).reset_index()

        return df_wide.rename(columns={'REF_AREA': 'country_code', 'TIME_PERIOD': 'year'})

    def execute_pipeline(self):
        # 1. Collect
        df_gain = self.fetch_nd_gain()
        df_wb = self.fetch_world_bank()
        df_oecd = self.fetch_oecd_policy()

        # 2. Merge
        print("Merging datasets...")
        merged = pd.merge(df_gain, df_wb, on=['country_code', 'year'], how='outer')
        merged = pd.merge(merged, df_oecd, on=['country_code', 'year'], how='outer')
        
        # 3. Clean
        merged = merged[merged['year'] <= 2021] # Standardize cutoff
        merged = merged[~merged['country_code'].isin(['USA', 'BRA'])] # Filter outliers
        
        # 4. Collapse (Temporal Averaging)
        num_cols = merged.select_dtypes(include=['number']).columns.tolist()
        if 'year' in num_cols: num_cols.remove('year')
        final_avg = merged.groupby(['country_code', 'Name'])[num_cols].mean().reset_index()

        # Drop columns where every value is exactly the same (no information for clustering)
        final_avg = final_avg.loc[:, (final_avg != final_avg.iloc[0]).any()]

        # Remove any countries with missing data in the final set (since we can't cluster them)
        final_avg = final_avg.dropna()
        
        # Save output
        os.makedirs('data/processed', exist_ok=True)
        final_avg.to_csv('data/processed/final_feature_matrix.csv', index=False)
        print(f"Pipeline Complete! Generated matrix for {len(final_avg)} countries.")
        return final_avg

if __name__ == "__main__":
    factory = ClimateDataFactory()
    factory.execute_pipeline()