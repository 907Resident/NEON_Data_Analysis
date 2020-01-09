#%% NEON_Unzipper
# title: Unzip NEON Flux Data
# 
# author: Moyo Ajayi
# 
# description: [works with previously downloaded files; sec01-unzip files]
# 


#%% Unzip Downloaded files

# Path of zipped files
zipped_data_query    = r'NEON_eddy-flux.zip'
# Path to deposit unzipped files
unzipped_data_query  = r'ORNL_data'
# Import Necessary Packages
import zipfile
with zipfile.ZipFile(zipped_data_query, 'r') as zip_ref:
    zip_ref.extractall(unzipped_data_query)

#%% October 2019 Data

# Path of zipped files
zipped_Oct2019         = r'ORNL_data/NEON.D07.ORNL.DP4.00200.001.2019-10.expanded.20191202T191735Z.zip'
# Path to deposit unzipped files
unzipped_data_Oct2019  = r'ORNL_data/ORNL-unzipped-data'

with zipfile.ZipFile(zipped_Oct2019, 'r') as zip_ref:
    zip_ref.extractall(unzipped_data_Oct2019)


