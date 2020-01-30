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

# Multiple Levels of IRGA Tower at CO2
df_ORNL.plot(x='timeBgn', y=['IRGA_lvl01_Co2_mu', 'IRGA_lvl02_Co2_mu', 
            'IRGA_lvl03_Co2_mu', 'IRGA_lvl04_Co2_mu', 'IRGA_lvl05_Co2_mu',
            'IRGA_lvl06_Co2_mu'], 
             kind='line', title='IRGA CO2 Measurements',grid=True)
plt.ylabel("[CO2] (ppm)")
plt.xlabel('')
plt.xticks(rotation=45)
plt.style.use('seaborn-darkgrid')
plt.show()

# 
# %%
