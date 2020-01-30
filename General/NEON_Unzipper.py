#%% NEON_Unzipper
# title: Unzip NEON Flux Data
# 
# author: Moyo Ajayi
# 
# description: [works with previously downloaded files; sec01-unzip files]
# will need to turn this into a function [30Jan2020]


#%% Unzip Downloaded files

# Path of zipped files
zipped_data_query    = r'C:/Users/moyoa/Google Drive/CompSci/PhD Dissertation/Data Analysis/Picarro/Cumberland/Vandy_NOAA_OakRidge/NEON/ORNL_data/NEON_conc-co2-soil.zip'
# Path to deposit unzipped files
unzipped_data_query  = r'C:/Users/moyoa/Google Drive/CompSci/PhD Dissertation/Data Analysis/Picarro/Cumberland/Vandy_NOAA_OakRidge/NEON/ORNL_data'
# Import Necessary Packages
import zipfile
with zipfile.ZipFile(zipped_data_query, 'r') as zip_ref:
    zip_ref.extractall(unzipped_data_query)

#%% October 2019 Data

# Path of zipped files
zipped_Oct2019         = r'C:/Users/moyoa/Google Drive/CompSci/PhD Dissertation/Data Analysis/Picarro/Cumberland/Vandy_NOAA_OakRidge/NEON/ORNL_data/NEON.D07.ORNL.DP1.00095.001.2019-10.expanded.20191105T194150Z.zip'
# Path to deposit unzipped files
unzipped_data_Oct2019  = r'C:/Users/moyoa/Google Drive/CompSci/PhD Dissertation/Data Analysis/Picarro/Cumberland/Vandy_NOAA_OakRidge/NEON/ORNL_data/ORNL-unzipped-data'

with zipfile.ZipFile(zipped_Oct2019, 'r') as zip_ref:
    zip_ref.extractall(unzipped_data_Oct2019)


