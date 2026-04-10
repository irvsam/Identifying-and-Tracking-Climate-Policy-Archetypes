import pandas as pd
from sklearn.preprocessing import StandardScaler, PowerTransformer

def preprocess_dataset(input_path, output_path, method='standard'):
    """Pre processing for the clustering algorithms."""

    # Load data
    df = pd.read_csv(input_path)
    
    # Drop non numerical
    # For most of the datasets im using it will just be these two: assume 'country_code' and 'Name' are the non-numeric labels
    X = df.drop(columns=['country_code', 'Name'])
    
    # Choose transformation method
    if method == 'power':
        # PowerTransformer (Yeo-Johnson) tries to make  data Gaussian (Bell Curve)
        # It also standardizes (mean=0, std=1) by default
        transformer = PowerTransformer(method='yeo-johnson')
        X_final = transformer.fit_transform(X)
        print("Used PowerTransformer (Yeo-Johnson)")
        
    else:
        # Standard Scaling: Only shifts and scales (Mean 0, Std 1)
        # Doesnt change the shape/distribution of the data
        scaler = StandardScaler()
        X_final = scaler.fit_transform(X)
        print("Used StandardScaler")

    # Save the results
    processed_df = pd.DataFrame(X_final, columns=X.columns)
    processed_df.to_csv(output_path, index=False)
    
    return processed_df

