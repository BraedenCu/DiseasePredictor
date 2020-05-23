import pandas as pd
import numpy as np

download_path = '~/Downloads/OHASDataset.csv'

def load_csv(path):
    return pd.read_csv(path)

data = load_csv(download_path)

data.describe()

data.dtypes

#I don't see Weight or Height being useful because BMI is simply a combonation of those factors
#so I am going to simply remove them
data.drop(['Height'], axis=1)
data.drop(['Weight'], axis=1)
