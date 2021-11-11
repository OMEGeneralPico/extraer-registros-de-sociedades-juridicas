import pandas as pd

import os
import glob

#obtener el working directory
path = os.getcwd()
all_files = glob.glob(path + "/registro-nacional-sociedades*.csv")
print(all_files)
df = pd.DataFrame()

for i in range(len(all_files)):
df1 = pd.read_csv(all_files[i], index_col=None, header=0)
print(all_files[i])
df1_sliced = df1.loc[df1['dom_fiscal_localidad'] == 'GENERAL PICO']
df = df.append(df1_sliced)
df = df.drop_duplicates()
df1 = pd.read_csv(all_files[-1], index_col=None, header=0)

df1_sliced = df1.loc[df1['dom_fiscal_localidad'] == 'GENERAL PICO']

df1_sliced = df1_sliced.drop_duplicates()

df1_sliced.to_csv('registro-nacional-sociedades-general-pico.csv', index = False)