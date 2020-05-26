#%% NEON_Data_Wrangler_SoilCO2
# title: Wrangle NEON Flux Data
# 
# author: Moyo Ajayi
# 
# description: [works with previously unzipped files; SCO2C]
# 

#%% Import necessary packages

import os
import glob
import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime

# Gather file directory that points to data
data_dir  = r'C:/Users/moyoa/Google Drive/CompSci/PhD Dissertation/Data Analysis/Picarro/Cumberland/Vandy_NOAA_OakRidge/NEON'
data_fldr = r'/ORNL_data/ORNL-unzipped-data/'
# First part of file name -- includes the data product number
data_file = r'/NEON.D07.ORNL.DP1.00095.001.'
data_file_a = '*30_minute.2019-10.csv'

# Path for Soil CO2 file
soilCO2_csv_files = glob.glob(data_dir + data_fldr + data_file + data_file_a)

for i in range(len(soilCO2_csv_files)):
    soilCO2_csv_files[i] = soilCO2_csv_files[i].replace("\\","/")

#%% Compile csv files into dataframe

# Compile Clean Data Frames from CSV Files
## Set the folder path for the csv files
#folderpath = 
# Read and Concatenate csv Files into dataframe
df_SoilCO2 = []
for filename in soilCO2_csv_files:
    df = pd.read_csv(filename, header=0)
    df_SoilCO2.append(df)

df_SoilCO2 = pd.concat(df_SoilCO2)

#%% Clean and Preprocess dataframe

# Clean date and time
# Time Begin
df_SoilCO2['startDateTime'] = df_SoilCO2['startDateTime'].astype(str)
df_SoilCO2['startDateTime'] = df_SoilCO2['startDateTime'].astype(str)
# Time End
df_SoilCO2['endDateTime'] = df_SoilCO2['endDateTime'].astype(str)
df_SoilCO2['endDateTime'] = df_SoilCO2['endDateTime'].astype(str)
# Date Format
date_format = "%Y-%m-%dT%H:%M:%SZ"
# Convert to datetime
df_SoilCO2['startDateTime'] = pd.to_datetime(
                     df_SoilCO2['startDateTime'], format=date_format, 
                     errors='coerce')
df_SoilCO2['endDateTime'] = pd.to_datetime(
                     df_SoilCO2['endDateTime'], format=date_format, 
                     errors='coerce')
df_SoilCO2.head()


#%% Exploratory Data Analysis

# SoilCO2 - min | mean | max
df_SoilCO2.plot(x='startDateTime', 
                y=['soilCO2concentrationMean'], kind='line', 
                title='Soil CO2 Concentration at NEON', legend=False,
                grid=True, linestyle='',marker='.')
plt.style.use('seaborn-darkgrid') 
plt.ylabel('[CO2] (ppm)')

# Resample for the 3hr median
# set index to start time and then resample and plot
# %%
