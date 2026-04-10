# %%
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Get the dataset
df_averaged = pd.read_csv('../../data/processed/final_feature_matrix.csv')

# Drop non numerical values
X = df_averaged.drop(columns=['country_code', 'Name'])

# Scale using fit transform
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Print the first few rows of the scaled data
print(X_scaled[:5])

# Compare with unscaled data
print(X[:5])

# Which scaling method is best for K-Means? StandardScaler?
# Use standard scalar



# %% [markdown]
# # Visualising OG set

# %%
# Simple visualisation of distibution of og set


df_averaged.hist(figsize=(12, 10))
plt.tight_layout()
plt.show()


# %%


from sklearn.preprocessing import StandardScaler, PowerTransformer
# Apply PowerTransformer (Yeo-Johnson) 
pt = PowerTransformer(method='yeo-johnson')
X_transformed = pt.fit_transform(X)

# Final Standardization
scaler = StandardScaler()
X_final = scaler.fit_transform(X_transformed)

# Convert to DataFrame to check results
X_df = pd.DataFrame(X_final, columns=X.columns)
print("New Mean (should be ~0):", X_df.mean().mean())
print("New Std (should be ~1):", X_df.std().mean())

# Compare with the scaling used above
print("Standard Scaled Mean (should be ~0):", X_scaled.mean())
print("Standard Scaled Std (should be ~1):", X_scaled.std())



# %%
plt.figure(figsize=(12, 10))
sns.heatmap(X_scaled_df.corr(), cmap='coolwarm', center=0)
plt.title("Feature Redundancy Audit")

# %%
# Save the scaled data
scaled_df = pd.DataFrame(X_final, columns=X.columns)
scaled_df.to_csv('../../data/processed/merged_dataset_scaled.csv', index=False)



