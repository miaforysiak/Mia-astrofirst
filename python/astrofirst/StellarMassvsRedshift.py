#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np 
import matplotlib.pyplot as plt
from astropy.io import fits


# In[82]:


drpall = fits.open('drpall-v3_1_1.fits')
tbdata = drpall[1].data


# In[81]:


ancillary = (tbdata['mngtarg3'] != 0)
ancillary_cube = tbdata[ancillary]

sm_ancillary = ancillary_cube['nsa_elpetro_mass']
red_ancillary = ancillary_cube['nsa_z']

p_pp_s = (tbdata['mngtarg1'])

primary = (p_pp_s & (1 << 10) != 0)
primary_cube = tbdata[primary]

sm_primary = primary_cube['nsa_elpetro_mass']
red_primary = primary_cube['nsa_z']

primary_plus = (p_pp_s & (1 << 12) != 0)
primary_plus_cube = tbdata[primary_plus]

sm_primary_plus = primary_plus_cube['nsa_elpetro_mass']
red_primary_plus = primary_plus_cube['nsa_z']

secondary = (p_pp_s & (1 << 11) != 0)
secondary_cube = tbdata[secondary]

sm_secondary = secondary_cube['nsa_elpetro_mass']
red_secondary = secondary_cube['nsa_z']

plt.scatter(red_primary, np.log(sm_primary), s=1, color= 'crimson', label = 'Primary')
plt.scatter(red_primary_plus, np.log(sm_primary_plus), s=1, color= 'orange', label = 'Primary+')
plt.scatter(red_secondary, np.log(sm_secondary), s=1, color= 'yellowgreen', label = 'Secondary')
plt.scatter(red_ancillary, np.log(sm_ancillary), s=1, color= 'dodgerblue', label = 'Ancillary')

plt.ylim(7, 28)
plt.xlabel('Redshift', fontsize = 16)
plt.ylabel('Log Stellar Mass ($ M_{\odot} $)', fontsize = 16)
plt.title('Log Stellar Mass ($M_{\odot}$) vs. Redshift in MaNGA Sample', fontsize = 14)
plt.legend(title = 'Sample', loc = 'lower right', markerscale = 6)
plt.savefig('LogStellarMassvsRedshift.png')
plt.show()

