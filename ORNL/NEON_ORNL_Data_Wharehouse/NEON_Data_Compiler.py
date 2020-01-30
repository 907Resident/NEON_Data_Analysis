#%% NEON Compile Oct 2019 Clean Data Frames
# This short script compiles clean data frames (which were
# exported to csv files at the end of NEON_Data_Wrangler)

# Import Neccessary Libaries
import glob
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%% Import and concatenate csv files into dataframe

# Establish the path for folder containing the clean csv files
folderpath = "C:/Users/moyoa/Documents/GitHub/NEON_Data_Analysis/ORNL/NEON_ORNL_Data_Wharehouse/clean_dataframes/"

# Compile Clean Data Frames
df_ORNL = pd.concat(map(pd.read_csv, glob.glob(os.path.join(
                    folderpath, "df_ORNL_*.csv"))))

#%% Clean and Preprocess

# Rename 'Unnamed: 0' to 'faux_index'
df_ORNL.rename(columns={'Unnamed: 0':'faux_index'}, inplace=True)
# Get rid of former index column
df_ORNL = df_ORNL.drop('faux_index', axis=1)

#%% Exploratory Data Analysis

# Multiple Levels with IRGA on NEON Tower -- CO2
plt.style.use('seaborn-darkgrid')
df_ORNL.plot(x='timeBgn', y=['IRGA_lvl01_Co2_mu', 'IRGA_lvl02_Co2_mu', 
            'IRGA_lvl03_Co2_mu', 'IRGA_lvl04_Co2_mu', 'IRGA_lvl05_Co2_mu',
            'IRGA_lvl06_Co2_mu'], 
             kind='line', title='IRGA CO2 Measurements',grid=True)
plt.ylabel("[CO2] (ppm)")
plt.xlabel('')
plt.xticks(rotation=45)
plt.show()

# Multiple Levels with CRDS on NEON Tower -- CO2 
plt.style.use('seaborn-darkgrid')
df_ORNL.plot(x='timeBgn', y=['isoCO2_lvl01_dryCo2_mu', 'isoCO2_lvl02_dryCo2_mu', 
            'isoCO2_lvl03_dryCo2_mu', 'isoCO2_lvl04_dryCo2_mu', 'isoCO2_lvl05_dryCo2_mu',
            'isoCO2_lvl06_dryCo2_mu'], 
             kind='line', title='CRDS CO2 Measurements',grid=True)
plt.ylabel("[CO2] (ppm)")
plt.xlabel('')
plt.xticks(rotation=45)
plt.show()

# Multiple Levels with CRDS on NEON Tower -- d13C-CO2 
plt.style.use('seaborn-darkgrid')
df_ORNL.plot(x='timeBgn', y=['isoCO2_lvl01_iCo2_mu', 'isoCO2_lvl02_iCo2_mu', 
            'isoCO2_lvl03_iCo2_mu', 'isoCO2_lvl04_iCo2_mu', 'isoCO2_lvl05_iCo2_mu',
            'isoCO2_lvl06_iCo2_mu'], 
             kind='line', title='CRDS δ13C-CO2 Measurements',grid=True)
plt.ylabel("δ13C-CO2 (‰)")
plt.xlabel('')
plt.xticks(rotation=45)
plt.show()

# Subplots
## IRGA-lvl05 | CRDS-lvl05  | d13CO2-lvl-05 | Temp-lvl05 | EC-NetFlux
plt.style.use('seaborn-darkgrid')
ax = df_ORNL.plot(x='timeBgn', y=['IRGA_lvl05_Co2_mu', 'isoCO2_lvl05_dryCo2_mu',
            'isoCO2_lvl05_iCo2_mu', 'Lvl05_tempAir_mu', 'EC_co2FlxNSAE'], 
            subplots=True, figsize=(8,8), title='NEON ORNL CO2 Tower Data')
ax[0].set_ylabel('[CO2] (ppm)')
ax[1].set_ylabel('[CO2] (ppm)')
ax[2].set_ylabel('δ13C-CO2 (‰)')
ax[3].set_ylabel('°C')
ax[4].set_ylabel('mmol m-2 s-1')
plt.legend(loc='best')
plt.xlabel('')

#%%
