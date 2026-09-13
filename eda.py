import numpy as np
from scipy import stats

import data_loader as dl

df = dl.load_data()
dl.data_info(df)

print('\n----DATA STATISTICS----')
print(df.describe())

numeric_cols = df.select_dtypes(include=[np.number]).columns
print(f"\nNumeric columns: {list(numeric_cols)}")

print("\nSkewness and Kurtosis:")
for col in numeric_cols:
    skewness = stats.skew(df[col].dropna())
    kurtosis = stats.kurtosis(df[col].dropna())
    print(f"{col}: Skewness = {skewness:.3f}, Kurtosis = {kurtosis:.3f}")