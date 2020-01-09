#%% NEON_Data_Wrangler
# title: Wrangle NEON Flux Data
# 
# author: Moyo Ajayi
# 
# description: [works with previously unzipped files; sec01-unzip files]
# 

#%% Open up HDF5 Files

# Import necessary packages
import h5py
import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt
# Path for HD5F file
raw_file = r'ORNL_data/ORNL-unzipped-data/NEON.D07.ORNL.DP4.00200.001.nsae.2019-10-24.expanded.h5'
# Open up HD5F file
h5_file = h5py.File(raw_file, 'r')

# View the components of the DataFrame
df_h5parts = pd.DataFrame(np.array(h5py.File(raw_file)))
df_h5parts.head()

# Get readMe information
txt = h5_file['readMe']
rdMe = txt[0,]

# Write out the readMe file to a text file
with open(r'ORNL_data/rdMe.txt', 'wb') as w:
    w.write(rdMe)

#%% Organize pertinent data into dataframes

# Gather all data collected at site from h5 file
### All collected data at ORNL
data            = h5_file['ORNL']
### List the components of the data in the h5 file
data.keys()
###### The command above shows what levels of data products in the h5 file are present

### Level 0 prime data products
dp0p            = data['dp0p']['data']
dp0p.keys()
###### Gather the CO2 CRDS data
dp0p['crdCO2']

### Level 1
dp01p           = data['dp01']['data']
###### Gather the CO2 profile data
######## Level 01 | 30-min resolution
dp01p_lvl01_co2Stor = dp01p['co2Stor']['000_010_30m']['rtioMoleDryCo2']
dp01p_lvl01_co2Stor = dp01p['co2Stor']['000_010_30m']['rtioMoleDryCo2'][:len(dp01p_lvl01_co2Stor)]


# EC Tower CO2 Fluxes