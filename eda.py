import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
import seaborn as sns
import data_loader as dl

sns.set_palette("husl")
plt.style.use('seaborn-v0_8')


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

print("\nTarget Value")
plt.figure(figsize=(10, 8))
sns.boxplot(x='Engine Condition', y='Lub oil pressure', data=df)
plt.title('Engine Condition: Lub oil pressure')
plt.tight_layout()
plt.show()