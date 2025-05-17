import pandas as pd
import matplotlib.pyplot as plt

data_df = pd.read_excel('rawdata\supermarket.xlsx')

column_names = data_df.columns
print(column_names)
print(data_df)