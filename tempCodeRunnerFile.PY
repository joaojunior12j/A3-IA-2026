import pandas as pd 
import matplotlib as plt
import numpy as np
import seaborn as sns

dados = "amazon.csv"
df = pd.read_csv (dados)
print(df.head())

print(df.dtypes)
print(df.columns)
