# Identifying and Tracking Climate Policy Archetypes
**A Cluster-Based Assessment of select OECD countries' Climate Action (2000-2021)**

An unsupervised machine learning project that identifies and tracks global climate policy archetypes using K-Means, Hierarchical Clustering, DBSCAN, and a PyTorch Autoencoder.

## Interactive Outputs
- [Climate Policy Archetypes — World Map](https://irvsam.github.io/Identifying-and-Tracking-Climate-Policy-Archetypes/notebooks/outputs/map_autoencoder_full.html)
- [Policy vs Economy Comparison Map](https://irvsam.github.io/Identifying-and-Tracking-Climate-Policy-Archetypes/notebooks/outputs/map_autoencoder_policy.html)
- [AE Latent Space (3D)](https://irvsam.github.io/Identifying-and-Tracking-Climate-Policy-Archetypes/notebooks/outputs/ae_latent_3d.html)
- [Temporal Trajectories (3D)](https://irvsam.github.io/Identifying-and-Tracking-Climate-Policy-Archetypes/notebooks/outputs/trajectories_3d.html)

## Data Sources 

* **World Bank Development Indicators (WDI)**
  * **Citation**: World Bank (2026), World Development Indicators.
  * **License**: Creative Commons Attribution 4.0 International (CC BY 4.0).
  * **Access**: Data accessed via the World Bank API.

* **OECD Climate Actions and Policies Measurement Framework (CAPMF)**
  * **Citation**: OECD (2025), CAPMF Measurement Framework.
  * **License**: OECD Terms and Conditions for Use.
  * **Access**: Data accessed via OECD SDMX API.

* **ND-GAIN Country Index**
  * **Citation**: Notre Dame Global Adaptation Initiative (2025).
  * **License**: Creative Commons Attribution 4.0 International (CC BY 4.0).
  * **Access**: [gain.nd.edu](https://gain.nd.edu/our-work/country-index/)

  ## Daily logs
  Daily logs are kept in logbook.txt and are a good read to see how the project evolved over time. 

  ## Main Experiment
  The main final consolidated experiment lives in [text](notebooks/final_consolidated_archetype_testing.ipynb)
  The rest of the notebooks contain iterative experiments that evolved over time and accumulated into the consolidated file.