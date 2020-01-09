#%% Accessing NEON Data

# Using steps from NEON Website: https://www.neonscience.org/neon-utilities-python

#%% Load NEON Utilities
import rpy2
import rpy2.robjects as robjects
import warnings

from rpy2.rinterface        import RRuntimeWarning
from rpy2.robjects.packages import importr

base     = importr('base')
utils    = importr('utils')
stats    = importr('stats')

# Ignore R warnings
warnings.filterwarnings("ignore", category=RRuntimeWarning)


#%% Devtools

# Devtools package from R
utils.install_packages('devtools')
# Import devtools
devtools    = importr('devtools')
# Install Devtools from GitHub
devtools.install_github("NEONScience/NEON-utilities/neonUtilities")
# Import neonUtilities
neonUtils   = importr("neonUtilities")

#%% Join Data Files

# Extract rdata object from neonUtils package
neonUdata   = neonUtils.__rdata__
# Extract table_types object from rdata object
table_types = neonUdata.fetch('table_types')['table_types']
# Pass table_types object through R
robjects.globalenv['table_types'] = table_types

# Stack downloaded tables into zip folder - enter path as input
neonUtils.stackByTable(filepath='NEON_2018_07__2019_11/filesToStack00200')


