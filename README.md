# Identifying and Tracking Climate Policy Archetypes
**A Cluster-Based Assessment of Climate Action Across 49 Countries (2000–2020)**

An unsupervised machine learning project that identifies and tracks global climate policy archetypes using K-Means, Hierarchical Clustering, DBSCAN, and a PyTorch Autoencoder.

## Interactive Outputs
- [Climate Policy Archetypes — World Map](https://irvsam.github.io/Identifying-and-Tracking-Climate-Policy-Archetypes/notebooks/outputs/map_autoencoder_full.html)
- [Policy vs Economy Comparison Map](https://irvsam.github.io/Identifying-and-Tracking-Climate-Policy-Archetypes/notebooks/outputs/map_autoencoder_policy.html)
- [AE Latent Space (3D)](https://irvsam.github.io/Identifying-and-Tracking-Climate-Policy-Archetypes/notebooks/outputs/ae_latent_3d.html)
- [Temporal Trajectories (3D)](https://irvsam.github.io/Identifying-and-Tracking-Climate-Policy-Archetypes/notebooks/outputs/trajectories_3d.html)

## How This Repo Works

### `src/` — Data Pipeline Scripts
These are the setup scripts for creating the final feature matrix. No need to re run them as the final datasets are version controlled and available in [data/processed](data/processed)

- **`collecting.py`** — Fetches raw data from the World Bank API, OECD CAPMF API, and a local ND-GAIN CSV. Merges everything into country-year pairs, fills missing policy values with 0, and outputs two CSVs: a long-format temporal dataset and an averaged snapshot per country.
- **`cleaning.py`** — Clips negative values in percentage columns, log-transforms GDP per capita and energy use per capita, then drops the original raw versions of those columns. Applies PowerTransformer (Yeo-Johnson) scaling separately to the averaged and temporal datasets.
- **`preprocessing.py`** — Standalone helper that applies either PowerTransformer or StandardScaler to a dataset and saves the result. Used for earlier experiments.
- **`data_loader.py`** — Helper functions for fetching World Bank, OECD, and EDGAR data, used by `collecting.py`.
- **`constants.py`** — Country list (50 countries), year range (2000–2020), World Bank indicator codes, and selected OECD policy IDs with human-readable names.

The final datasets used in the experiment are:
- `data/processed/avg_cleaned_feature_matrix.csv`
- `data/processed/temporal_cleaned_feature_matrix.csv`

### `notebooks/` — Experiments
The main experiment is in [`final_consolidated_archetype_testing.ipynb](notebooks/final_consolidated_archetype_testing.ipynb)`. It runs the following in sequence:

1. **Snapshot Clustering** — K-Means (with elbow and silhouette plots to choose k), Hierarchical (Ward linkage with dendrogram), and DBSCAN (with k-distance plot to choose eps); includes a cluster fingerprint heatmap and a stability check (co-occurrence matrix over 50 runs)
2. **Autoencoder + K-Means** — PyTorch autoencoder (input → 16 → 8 → 3 → 8 → 16 → input) compressing the averaged data to a 3D latent space, then K-Means on that representation; includes a PCA scatter plot, cluster fingerprint heatmap, and a counterfactual test where a real country's features are tweaked to see if it moves cluster
3. **Temporal Trajectories** — A second autoencoder trained on the full country-year dataset; tracks how countries move through archetype space from 2000 to 2020, with a 3D line plot, per-country cluster sequences, and a bar chart of total movement
4. **Feature Set Comparison (Maps)** — Re-runs clustering on the full feature set vs. policy-only (economic indicators removed), uses the Hungarian algorithm to align labels before comparing, and renders both as interactive choropleths
5. **Feature Importance** — Zeroes out each feature one at a time and measures the increase in reconstruction error to see which features the autoencoder relies on most

The other notebooks in the folder contain earlier iterative experiments that accumulated into the consolidated file.

### Daily Logs
[`logbook.txt`](logbook.txt) traces how the project evolved - worth a read to see the full thought process.

## Data Sources

- **World Bank Development Indicators (WDI)** — accessed via World Bank API. License: CC BY 4.0.
- **OECD Climate Actions and Policies Measurement Framework (CAPMF)** — accessed via OECD SDMX API.
- **ND-GAIN Country Index** — [gain.nd.edu](https://gain.nd.edu/our-work/country-index/). License: CC BY 4.0.