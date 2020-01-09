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
raw_file = r'ORNL-unzipped-data/NEON.D07.ORNL.DP4.00200.001.nsae.2019-10-24.expanded.h5'
# Open up HD5F file
h5_file = h5py.File(raw_file, 'r')

# View the components of the DataFrame
df_h5parts = pd.DataFrame(np.array(h5py.File(raw_file)))
df_h5parts.head()

# Get readMe information
txt = h5_file['readMe']
rdMe = txt[0,]

# Write out the readMe file to a text file
with open(r'rdMe.txt', 'wb') as w:
    w.write(rdMe)

#%% Organize pertinent data into dataframes

# Gather all data collected at site from h5 file
### All collected data at ORNL
data            = h5_file['ORNL']
### List the components of the data in the h5 file
data.keys()
###### The command above shows what levels of data products in the h5 file are present

#%% LEVEL 0 -- dp0p

### Level 0 prime data products
dp0p            = data['dp0p']['data']
dp0p.keys()
###### Gather the CO2 CRDS data
dp0p_crdCo2 = dp0p['crdCo2']
####### ^^^ No data for this entry

#%% LEVEL 1 -- dp01

### Level 1
dp01p           = data['dp01']['data']

###### Gather the CO2 profile data -- IRGA [CO2]
######## Level 01 | 30-min resolution
dp01p_IRGA_lvl01_co2Stor = dp01p['co2Stor']['000_010_30m']['rtioMoleDryCo2']
dp01p_IRGA_lvl01_co2Stor = dp01p['co2Stor']['000_010_30m']['rtioMoleDryCo2'][:len(dp01p_IRGA_lvl01_co2Stor)]
######## Level 02 | 30-min resolution
dp01p_IRGA_lvl02_co2Stor = dp01p['co2Stor']['000_020_30m']['rtioMoleDryCo2']
dp01p_IRGA_lvl02_co2Stor = dp01p['co2Stor']['000_020_30m']['rtioMoleDryCo2'][:len(dp01p_IRGA_lvl02_co2Stor)]
######## Level 03 | 30-min resolution
dp01p_IRGA_lvl03_co2Stor = dp01p['co2Stor']['000_030_30m']['rtioMoleDryCo2']
dp01p_IRGA_lvl03_co2Stor = dp01p['co2Stor']['000_030_30m']['rtioMoleDryCo2'][:len(dp01p_IRGA_lvl03_co2Stor)]
######## Level 04 | 30-min resolution
dp01p_IRGA_lvl04_co2Stor = dp01p['co2Stor']['000_040_30m']['rtioMoleDryCo2']
dp01p_IRGA_lvl04_co2Stor = dp01p['co2Stor']['000_040_30m']['rtioMoleDryCo2'][:len(dp01p_IRGA_lvl04_co2Stor)]
######## Level 05 | 30-min resolution
dp01p_IRGA_lvl05_co2Stor = dp01p['co2Stor']['000_050_30m']['rtioMoleDryCo2']
dp01p_IRGA_lvl05_co2Stor = dp01p['co2Stor']['000_050_30m']['rtioMoleDryCo2'][:len(dp01p_IRGA_lvl05_co2Stor)]
######## Level 06 | 30-min resolution
dp01p_IRGA_lvl06_co2Stor = dp01p['co2Stor']['000_060_30m']['rtioMoleDryCo2']
dp01p_IRGA_lvl06_co2Stor = dp01p['co2Stor']['000_060_30m']['rtioMoleDryCo2'][:len(dp01p_IRGA_lvl06_co2Stor)]

"""
This block will need to be edited but since it does not contain any data, I have commented it out
(09-Jan-2020)
###### Gather the Soil Temperature 
######## Level 01 | 30-min resolution
#dp01p_p01l01_tempSoil = dp01p['tempSoil']['001_501_30m']
dp01p_p01l01_tempSoil = dp01p['tempSoil']['001_501_30m'][:len(dp01p_p01l01_tempSoil)]
######## Level 02 | 30-min resolution
dp01p_p01l02_tempSoil = dp01p['tempSoil']['001_502_30m']['rtioMoleDryCo2']
dp01p_p01l02_tempSoil = dp01p['tempSoil']['001_502_30m']['rtioMoleDryCo2'][:len(dp01p_lvl02_tempSoil)]
######## Level 03 | 30-min resolution
dp01p_p01l03_tempSoil = dp01p['tempSoil']['000_030_30m']['rtioMoleDryCo2']
dp01p_p01l03_tempSoil = dp01p['tempSoil']['000_030_30m']['rtioMoleDryCo2'][:len(dp01p_lvl03_tempSoil)]
######## Level 04 | 30-min resolution
dp01p_p01l04_tempSoil = dp01p['tempSoil']['000_040_30m']['rtioMoleDryCo2']
dp01p_p01l04_tempSoil = dp01p['tempSoil']['000_040_30m']['rtioMoleDryCo2'][:len(dp01p_lvl04_tempSoil)]
######## Level 05 | 30-min resolution
dp01p_p01l05_tempSoil = dp01p['tempSoil']['000_050_30m']['rtioMoleDryCo2']
dp01p_p01l05_tempSoil = dp01p['tempSoil']['000_050_30m']['rtioMoleDryCo2'][:len(dp01p_lvl05_tempSoil)]
######## Level 06 | 30-min resolution
dp01p_p01l06_tempSoil = dp01p['tempSoil']['000_060_30m']['rtioMoleDryCo2']
dp01p_p01l06_tempSoil = dp01p['tempSoil']['000_060_30m']['rtioMoleDryCo2'][:len(dp01p_lvl06_tempSoil)]

"""

###### Gather CRDS [CO2] Measurements
######## Level 01 | 30-min resolution
dp01p_isoCo2_lvl01_dryCo2 = dp01p['isoCo2']['000_010_30m']['rtioMoleDryCo2']
dp01p_isoCo2_lvl01_dryCo2 = dp01p['isoCo2']['000_010_30m']['rtioMoleDryCo2'][:len(dp01p_isoCo2_lvl01_dryCo2)]
######## Level 02 | 30-min resolution
dp01p_isoCo2_lvl02_dryCo2 = dp01p['isoCo2']['000_020_30m']['rtioMoleDryCo2']
dp01p_isoCo2_lvl02_dryCo2 = dp01p['isoCo2']['000_020_30m']['rtioMoleDryCo2'][:len(dp01p_isoCo2_lvl02_dryCo2)]
######## Level 03 | 30-min resolution
dp01p_isoCo2_lvl03_dryCo2 = dp01p['isoCo2']['000_030_30m']['rtioMoleDryCo2']
dp01p_isoCo2_lvl03_dryCo2 = dp01p['isoCo2']['000_030_30m']['rtioMoleDryCo2'][:len(dp01p_isoCo2_lvl03_dryCo2)]
######## Level 04 | 30-min resolution
dp01p_isoCo2_lvl04_dryCo2 = dp01p['isoCo2']['000_040_30m']['rtioMoleDryCo2']
dp01p_isoCo2_lvl04_dryCo2 = dp01p['isoCo2']['000_040_30m']['rtioMoleDryCo2'][:len(dp01p_isoCo2_lvl04_dryCo2)]
######## Level 05 | 30-min resolution
dp01p_isoCo2_lvl05_dryCo2 = dp01p['isoCo2']['000_050_30m']['rtioMoleDryCo2']
dp01p_isoCo2_lvl05_dryCo2 = dp01p['isoCo2']['000_050_30m']['rtioMoleDryCo2'][:len(dp01p_isoCo2_lvl05_dryCo2)]
######## Level 06 | 30-min resolution
dp01p_isoCo2_lvl06_dryCo2 = dp01p['isoCo2']['000_060_30m']['rtioMoleDryCo2']
dp01p_isoCo2_lvl06_dryCo2 = dp01p['isoCo2']['000_060_30m']['rtioMoleDryCo2'][:len(dp01p_isoCo2_lvl06_dryCo2)]


# EC Tower CO2 Fluxes


# %%
