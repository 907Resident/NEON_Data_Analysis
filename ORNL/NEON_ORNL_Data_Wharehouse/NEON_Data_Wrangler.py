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
import os
import numpy                as np
import pandas               as pd
import matplotlib.pyplot    as plt
import glob

from datetime               import datetime, timedelta

#%% Gather the associated files 

# Gather file directory that points to data
data_dir_root   = r'E:/moyoa/Documents/OneDrive - Vanderbilt/PhD_Dissertation/Data_Analysis/Picarro/Cumberland/Vandy_NOAA_OakRidge/NEON'
data_fldr       = r'/ORNL_data/ORNL-unzipped-data/EC_data'
data_directory  = os.path.join(data_dir_root + data_fldr + "/*/*.h5")

# Concatenate filenamnes into list
h5_filenames    = glob.glob(data_directory)
## N-elements is the number of files .h5 files in the directory
N_h5_files      = len(h5_filenames)

# For loop to execute code for each .h5 file in the directory
for i in range(N_h5_files):
    # Path for HD5F file
    raw_file = h5_filenames[i]
    # Open up HD5F file
    h5_file = h5py.File(raw_file, 'r')
    
    # View the components of the DataFrame
    df_h5parts = pd.DataFrame(np.array(h5py.File(raw_file)))
    df_h5parts.head()

#%% Organize pertinent data into dataframes

    # Gather all data collected at site from h5 file
    ### All collected data at ORNL
    data            = h5_file['ORNL']
    ### List the components of the data in the h5 file
    data.keys()
    ###### The command above shows what levels of data products in the h5 file are present

    # LEVEL 0 -- dp0p

    ### Level 0 prime data products
    dp0p            = data['dp0p']['data']
    dp0p.keys()

    # The keys at the zeroth data product level illustrate where you may find the data. For instance, if you search
    # keys for 'irgaTurb' will show '000_060' indicating that the turbulence measurement from the IRGA is located
    # the sixth level of the EC tower (the top)

    #%% Data Product 01  -- dp01

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

    ###### Gather CRDS d13CO2 - iCO2 -  Measurements
    ######## Level 01 | 30-min resolution
    dp01p_isoCo2_lvl01_iCo2 = dp01p['isoCo2']['000_010_30m']['dlta13CCo2']
    dp01p_isoCo2_lvl01_iCo2 = dp01p['isoCo2']['000_010_30m']['dlta13CCo2'][:len(dp01p_isoCo2_lvl01_iCo2)]
    ######## Level 02 | 30-min resolution
    dp01p_isoCo2_lvl02_iCo2 = dp01p['isoCo2']['000_020_30m']['dlta13CCo2']
    dp01p_isoCo2_lvl02_iCo2 = dp01p['isoCo2']['000_020_30m']['dlta13CCo2'][:len(dp01p_isoCo2_lvl02_iCo2)]
    ######## Level 03 | 30-min resolution
    dp01p_isoCo2_lvl03_iCo2 = dp01p['isoCo2']['000_030_30m']['dlta13CCo2']
    dp01p_isoCo2_lvl03_iCo2 = dp01p['isoCo2']['000_030_30m']['dlta13CCo2'][:len(dp01p_isoCo2_lvl02_iCo2)]
    ######## Level 04 | 30-min resolution
    dp01p_isoCo2_lvl04_iCo2 = dp01p['isoCo2']['000_040_30m']['dlta13CCo2']
    dp01p_isoCo2_lvl04_iCo2 = dp01p['isoCo2']['000_040_30m']['dlta13CCo2'][:len(dp01p_isoCo2_lvl04_iCo2)]
    ######## Level 05 | 30-min resolution
    dp01p_isoCo2_lvl05_iCo2 = dp01p['isoCo2']['000_050_30m']['dlta13CCo2']
    dp01p_isoCo2_lvl05_iCo2 = dp01p['isoCo2']['000_050_30m']['dlta13CCo2'][:len(dp01p_isoCo2_lvl05_iCo2)]
    ######## Level 06 | 30-min resolution
    dp01p_isoCo2_lvl06_iCo2 = dp01p['isoCo2']['000_060_30m']['dlta13CCo2']
    dp01p_isoCo2_lvl06_iCo2 = dp01p['isoCo2']['000_060_30m']['dlta13CCo2'][:len(dp01p_isoCo2_lvl06_iCo2)]

    """
    This block will need to be edited but since it does not contain any data, I have commented it out
    (09-Jan-2020)
    ###### Gather the Soil Temperature by plot and depth
    ######## Level 01 | 30-min resolution
    dp01p_p01l01_tempSoil = dp01p['tempSoil']['001_501_30m']
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

    ###### Gather the Air Temperature  by level
    ######## Level 01 | 30-min resolution
    dp01p_Lvl01_tempAir = dp01p['tempAirLvl']['000_010_30m']['temp']
    dp01p_Lvl01_tempAir = dp01p['tempAirLvl']['000_010_30m']['temp'][:len(dp01p_Lvl01_tempAir)]
    ######## Level 02 | 30-min resolution
    dp01p_Lvl02_tempAir = dp01p['tempAirLvl']['000_020_30m']['temp']
    dp01p_Lvl02_tempAir = dp01p['tempAirLvl']['000_020_30m']['temp'][:len(dp01p_Lvl02_tempAir)]
    ######## Level 03 | 30-min resolution
    dp01p_Lvl03_tempAir = dp01p['tempAirLvl']['000_030_30m']['temp']
    dp01p_Lvl03_tempAir = dp01p['tempAirLvl']['000_030_30m']['temp'][:len(dp01p_Lvl03_tempAir)]
    ######## Level 04 | 30-min resolution
    dp01p_Lvl04_tempAir = dp01p['tempAirLvl']['000_040_30m']['temp']
    dp01p_Lvl04_tempAir = dp01p['tempAirLvl']['000_040_30m']['temp'][:len(dp01p_Lvl04_tempAir)]
    ######## Level 05 | 30-min resolution
    dp01p_Lvl05_tempAir = dp01p['tempAirLvl']['000_050_30m']['temp']
    dp01p_Lvl05_tempAir = dp01p['tempAirLvl']['000_050_30m']['temp'][:len(dp01p_Lvl05_tempAir)]

    #%% Data Product 04 -- dp04

    ### Level 4
    dp04p           = data['dp04']['data']

    ###### Gather the EC Tower CO2 Fluxes -- Co2Flx
    ######+++ Used the Net Surface-Atmosphere Exchange values (nsae)
    #########+++ If 'nsae' is empty, then add storage flux (stor) and turbulent flux (turb)
    ######+++ See NEON documentation (https://data.neonscience.org/data-product-view?dpCode=DP4.00200.001) and 
    ######+++ Nicolini et al. (2018) (http://dx.doi.org/10.1016/j.agrformet.2017.09.025)
    ######## Storage FLux | 30-min resolution
    dp04p_EC_co2FlxStor = dp04p['fluxCo2']['stor']
    dp04p_EC_co2FlxStor = dp04p['fluxCo2']['stor'][:len(dp04p_EC_co2FlxStor)]
    ######## Turbulent FLux | 30-min resolution
    dp04p_EC_co2FlxTurb = dp04p['fluxCo2']['turb']
    dp04p_EC_co2FlxTurb = dp04p['fluxCo2']['turb'][:len(dp04p_EC_co2FlxTurb)]
    ######## NSAE Flux | 30-min resolution
    dp04p_EC_co2FlxNSAE = np.add(dp04p_EC_co2FlxStor['flux'], dp04p_EC_co2FlxTurb['fluxRaw'])

    #%% Combine Pertinent Data into DataFrame

    pert_data_dict = {
                    'timeBgn': dp01p_IRGA_lvl01_co2Stor['timeBgn'],
                    'timeEnd': dp01p_IRGA_lvl01_co2Stor['timeEnd'],
                    'IRGA_lvl01_Co2_mu': dp01p_IRGA_lvl01_co2Stor['mean'],
                    'IRGA_lvl01_Co2_mx': dp01p_IRGA_lvl01_co2Stor['max'],
                    'IRGA_lvl01_Co2_mn': dp01p_IRGA_lvl01_co2Stor['min'],
                    'IRGA_lvl01_Co2_vr': dp01p_IRGA_lvl01_co2Stor['vari'],
                    'IRGA_lvl01_Co2_n' : dp01p_IRGA_lvl01_co2Stor['numSamp'],
                    'IRGA_lvl02_Co2_mu': dp01p_IRGA_lvl02_co2Stor['mean'],
                    'IRGA_lvl02_Co2_mx': dp01p_IRGA_lvl02_co2Stor['max'],
                    'IRGA_lvl02_Co2_mn': dp01p_IRGA_lvl02_co2Stor['min'],
                    'IRGA_lvl02_Co2_vr': dp01p_IRGA_lvl02_co2Stor['vari'],
                    'IRGA_lvl02_Co2_n' : dp01p_IRGA_lvl02_co2Stor['numSamp'],
                    'IRGA_lvl03_Co2_mu': dp01p_IRGA_lvl03_co2Stor['mean'],
                    'IRGA_lvl03_Co2_mx': dp01p_IRGA_lvl03_co2Stor['max'],
                    'IRGA_lvl03_Co2_mn': dp01p_IRGA_lvl03_co2Stor['min'],
                    'IRGA_lvl03_Co2_vr': dp01p_IRGA_lvl03_co2Stor['vari'],
                    'IRGA_lvl03_Co2_n' : dp01p_IRGA_lvl03_co2Stor['numSamp'],
                    'IRGA_lvl04_Co2_mu': dp01p_IRGA_lvl04_co2Stor['mean'],
                    'IRGA_lvl04_Co2_mx': dp01p_IRGA_lvl04_co2Stor['max'],
                    'IRGA_lvl04_Co2_mn': dp01p_IRGA_lvl04_co2Stor['min'],
                    'IRGA_lvl04_Co2_vr': dp01p_IRGA_lvl04_co2Stor['vari'],
                    'IRGA_lvl04_Co2_n' : dp01p_IRGA_lvl04_co2Stor['numSamp'],
                    'IRGA_lvl05_Co2_mu': dp01p_IRGA_lvl05_co2Stor['mean'],
                    'IRGA_lvl05_Co2_mx': dp01p_IRGA_lvl05_co2Stor['max'],
                    'IRGA_lvl05_Co2_mn': dp01p_IRGA_lvl05_co2Stor['min'],
                    'IRGA_lvl05_Co2_vr': dp01p_IRGA_lvl05_co2Stor['vari'],
                    'IRGA_lvl05_Co2_n' : dp01p_IRGA_lvl05_co2Stor['numSamp'],
                    'IRGA_lvl06_Co2_mu': dp01p_IRGA_lvl06_co2Stor['mean'],
                    'IRGA_lvl06_Co2_mx': dp01p_IRGA_lvl06_co2Stor['max'],
                    'IRGA_lvl06_Co2_mn': dp01p_IRGA_lvl06_co2Stor['min'],
                    'IRGA_lvl06_Co2_vr': dp01p_IRGA_lvl06_co2Stor['vari'],
                    'IRGA_lvl06_Co2_n' : dp01p_IRGA_lvl06_co2Stor['numSamp'],
                    'isoCO2_lvl01_dryCo2_mu': dp01p_isoCo2_lvl01_dryCo2['mean'],
                    'isoCO2_lvl01_dryCo2_mx': dp01p_isoCo2_lvl01_dryCo2['max'],
                    'isoCO2_lvl01_dryCo2_mn': dp01p_isoCo2_lvl01_dryCo2['min'],
                    'isoCO2_lvl01_dryCo2_vr': dp01p_isoCo2_lvl01_dryCo2['vari'],
                    'isoCO2_lvl01_dryCo2_n' : dp01p_isoCo2_lvl01_dryCo2['numSamp'],
                    'isoCO2_lvl02_dryCo2_mu': dp01p_isoCo2_lvl02_dryCo2['mean'],
                    'isoCO2_lvl02_dryCo2_mx': dp01p_isoCo2_lvl02_dryCo2['max'],
                    'isoCO2_lvl02_dryCo2_mn': dp01p_isoCo2_lvl02_dryCo2['min'],
                    'isoCO2_lvl02_dryCo2_vr': dp01p_isoCo2_lvl02_dryCo2['vari'],
                    'isoCO2_lvl02_dryCo2_n' : dp01p_isoCo2_lvl02_dryCo2['numSamp'],
                    'isoCO2_lvl03_dryCo2_mu': dp01p_isoCo2_lvl03_dryCo2['mean'],
                    'isoCO2_lvl03_dryCo2_mx': dp01p_isoCo2_lvl03_dryCo2['max'],
                    'isoCO2_lvl03_dryCo2_mn': dp01p_isoCo2_lvl03_dryCo2['min'],
                    'isoCO2_lvl03_dryCo2_vr': dp01p_isoCo2_lvl03_dryCo2['vari'],
                    'isoCO2_lvl03_dryCo2_n' : dp01p_isoCo2_lvl03_dryCo2['numSamp'],
                    'isoCO2_lvl04_dryCo2_mu': dp01p_isoCo2_lvl04_dryCo2['mean'],
                    'isoCO2_lvl04_dryCo2_mx': dp01p_isoCo2_lvl04_dryCo2['max'],
                    'isoCO2_lvl04_dryCo2_mn': dp01p_isoCo2_lvl04_dryCo2['min'],
                    'isoCO2_lvl04_dryCo2_vr': dp01p_isoCo2_lvl04_dryCo2['vari'],
                    'isoCO2_lvl04_dryCo2_n' : dp01p_isoCo2_lvl04_dryCo2['numSamp'],
                    'isoCO2_lvl05_dryCo2_mu': dp01p_isoCo2_lvl05_dryCo2['mean'],
                    'isoCO2_lvl05_dryCo2_mx': dp01p_isoCo2_lvl05_dryCo2['max'],
                    'isoCO2_lvl05_dryCo2_mn': dp01p_isoCo2_lvl05_dryCo2['min'],
                    'isoCO2_lvl05_dryCo2_vr': dp01p_isoCo2_lvl05_dryCo2['vari'],
                    'isoCO2_lvl05_dryCo2_n' : dp01p_isoCo2_lvl05_dryCo2['numSamp'],
                    'isoCO2_lvl06_dryCo2_mu': dp01p_isoCo2_lvl06_dryCo2['mean'],
                    'isoCO2_lvl06_dryCo2_mx': dp01p_isoCo2_lvl06_dryCo2['max'],
                    'isoCO2_lvl06_dryCo2_mn': dp01p_isoCo2_lvl06_dryCo2['min'],
                    'isoCO2_lvl06_dryCo2_vr': dp01p_isoCo2_lvl06_dryCo2['vari'],
                    'isoCO2_lvl06_dryCo2_n' : dp01p_isoCo2_lvl06_dryCo2['numSamp'],
                    'isoCO2_lvl01_iCo2_mu': dp01p_isoCo2_lvl01_iCo2['mean'],
                    'isoCO2_lvl01_iCo2_mx': dp01p_isoCo2_lvl01_iCo2['max'],
                    'isoCO2_lvl01_iCo2_mn': dp01p_isoCo2_lvl01_iCo2['min'],
                    'isoCO2_lvl01_iCo2_vr': dp01p_isoCo2_lvl01_iCo2['vari'],
                    'isoCO2_lvl01_iCo2_n' : dp01p_isoCo2_lvl01_iCo2['numSamp'],
                    'isoCO2_lvl02_iCo2_mu': dp01p_isoCo2_lvl02_iCo2['mean'],
                    'isoCO2_lvl02_iCo2_mx': dp01p_isoCo2_lvl02_iCo2['max'],
                    'isoCO2_lvl02_iCo2_mn': dp01p_isoCo2_lvl02_iCo2['min'],
                    'isoCO2_lvl02_iCo2_vr': dp01p_isoCo2_lvl02_iCo2['vari'],
                    'isoCO2_lvl02_iCo2_n' : dp01p_isoCo2_lvl02_iCo2['numSamp'],
                    'isoCO2_lvl03_iCo2_mu': dp01p_isoCo2_lvl03_iCo2['mean'],
                    'isoCO2_lvl03_iCo2_mx': dp01p_isoCo2_lvl03_iCo2['max'],
                    'isoCO2_lvl03_iCo2_mn': dp01p_isoCo2_lvl03_iCo2['min'],
                    'isoCO2_lvl03_iCo2_vr': dp01p_isoCo2_lvl03_iCo2['vari'],
                    'isoCO2_lvl03_iCo2_n' : dp01p_isoCo2_lvl03_iCo2['numSamp'],
                    'isoCO2_lvl04_iCo2_mu': dp01p_isoCo2_lvl04_iCo2['mean'],
                    'isoCO2_lvl04_iCo2_mx': dp01p_isoCo2_lvl04_iCo2['max'],
                    'isoCO2_lvl04_iCo2_mn': dp01p_isoCo2_lvl04_iCo2['min'],
                    'isoCO2_lvl04_iCo2_vr': dp01p_isoCo2_lvl04_iCo2['vari'],
                    'isoCO2_lvl04_iCo2_n' : dp01p_isoCo2_lvl04_iCo2['numSamp'],
                    'isoCO2_lvl05_iCo2_mu': dp01p_isoCo2_lvl05_iCo2['mean'],
                    'isoCO2_lvl05_iCo2_mx': dp01p_isoCo2_lvl05_iCo2['max'],
                    'isoCO2_lvl05_iCo2_mn': dp01p_isoCo2_lvl05_iCo2['min'],
                    'isoCO2_lvl05_iCo2_vr': dp01p_isoCo2_lvl05_iCo2['vari'],
                    'isoCO2_lvl05_iCo2_n' : dp01p_isoCo2_lvl05_iCo2['numSamp'],
                    'isoCO2_lvl06_iCo2_mu': dp01p_isoCo2_lvl06_iCo2['mean'],
                    'isoCO2_lvl06_iCo2_mx': dp01p_isoCo2_lvl06_iCo2['max'],
                    'isoCO2_lvl06_iCo2_mn': dp01p_isoCo2_lvl06_iCo2['min'],
                    'isoCO2_lvl06_iCo2_vr': dp01p_isoCo2_lvl06_iCo2['vari'],
                    'isoCO2_lvl06_iCo2_n' : dp01p_isoCo2_lvl06_iCo2['numSamp'],
                    'Lvl01_tempAir_mu' : dp01p_Lvl01_tempAir['mean'],
                    'Lvl01_tempAir_vr' : dp01p_Lvl01_tempAir['vari'],
                    'Lvl02_tempAir_mu' : dp01p_Lvl02_tempAir['mean'],
                    'Lvl02_tempAir_vr' : dp01p_Lvl02_tempAir['vari'],
                    'Lvl03_tempAir_mu' : dp01p_Lvl03_tempAir['mean'],
                    'Lvl03_tempAir_vr' : dp01p_Lvl03_tempAir['vari'],
                    'Lvl04_tempAir_mu' : dp01p_Lvl04_tempAir['mean'],
                    'Lvl04_tempAir_vr' : dp01p_Lvl04_tempAir['vari'],
                    'Lvl05_tempAir_mu' : dp01p_Lvl05_tempAir['mean'],
                    'Lvl05_tempAir_vr' : dp01p_Lvl05_tempAir['vari'],
                    'EC_co2FlxStor' : dp04p_EC_co2FlxStor['flux'],
                    'EC_co2FlxTurb' : dp04p_EC_co2FlxTurb['fluxRaw'],
                    'EC_co2FlxNSAE' : dp04p_EC_co2FlxNSAE
                    }

    df_ORNL = pd.DataFrame(pert_data_dict)

    # Clean date and time
    # Time Begin
    df_ORNL['timeBgn'] = df_ORNL['timeBgn'].astype(str).str.replace('b', '')
    df_ORNL['timeBgn'] = df_ORNL['timeBgn'].astype(str).str.replace("'", '')
    # Time End
    df_ORNL['timeEnd'] = df_ORNL['timeEnd'].astype(str).str.replace('b', '')
    df_ORNL['timeEnd'] = df_ORNL['timeEnd'].astype(str).str.replace("'", '')
    # Date Format
    date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    # Convert to datetime
    df_ORNL['timeBgn'] = pd.to_datetime(
                        df_ORNL['timeBgn'], format=date_format, 
                        errors='coerce')
    df_ORNL['timeEnd'] = pd.to_datetime(
                        df_ORNL['timeEnd'], format=date_format, 
                        errors='coerce')
    df_ORNL.head()

    # Export DataFrame to csv
    month = df_ORNL['timeBgn'].dt.month[0]
    day   = df_ORNL['timeBgn'].dt.day[0]
    export_file_root = r'C:/Users/moyoa/Documents/GitHub/NEON_Data_Analysis/ORNL/NEON_ORNL_Data_Wharehouse'
    export_df_title  = r'/clean_dataframes/df_ORNL_2019-{}-{}.csv'.format(month,day)
    df_ORNL.to_csv(os.path.join(export_file_root + export_df_title))

    print("Current progress:",np.round((i/N_h5_files)*100,2),"%")
