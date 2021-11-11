import pandas as pd

import os
import glob

#obtener el working directory
path = os.getcwd()
#buscar todos los archivos de extension csv y nombre con registro-nacional-sociedades
all_files = glob.glob(path + "/registro-nacional-sociedades*.csv")
print(all_files)
df = pd.DataFrame()

#Leer el csv sin encabezados
df1 = pd.read_csv(all_files[-1], index_col=None, header=0)
#Filtro domicilio fiscal en general pico
df1_sliced = df1.loc[df1['dom_fiscal_localidad'] == 'GENERAL PICO']
#Eliminar duplicados
df1_sliced = df1_sliced.drop_duplicates()
#Exportar csv
df1_sliced.to_csv('registro-nacional-sociedades-general-pico.csv', index = False)