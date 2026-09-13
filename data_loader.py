import numpy as np
import pandas as pd

def load_data():
    data = pd.read_csv('D:\Prog\Python\EnginePredict\data\engine_data.csv')
    return data

def data_info(data):
    print('\nDataset shape:', data.shape)
    print(data.info())
    print('----DATA QUALITY CHECK----')
    print('\nData types:', data.dtypes)
    print('\nMissing values:', data.isnull().sum())
    print('\nDuplicate values:', data.duplicated().sum())
    print('\nCheck infinite values...')
    for col in data.columns:
        inf_count = np.isinf(data[col]).sum()
        if inf_count > 0:
            print(col, inf_count)
    print('\nSuccessfully')



