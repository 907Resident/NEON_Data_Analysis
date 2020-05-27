#%% Load NEON data from API, simply
## I have tried to use the utilies package for python users <https://www.neonscience.org/neonDataStackR>
## created by NEON, but it did not work very well for me.  Therefore, I am using a much simipler approach
## - the urlib and request packages that I normally use when accessing data from other APIs


#%% Import Necessary Libraries 

import pandas                               as pd 
import numpy                                as np 
import matplotlib.pyplot                    as plt 
import seaborn                              as sns

import requests
import json

#%% 

# tets url
test_url = r"http://data.neonscience.org/api/v0/data/DP4.00200.001/ORNL/2019-11"

response        = requests.get(test_url)
json_response   = response.json()



# %%
