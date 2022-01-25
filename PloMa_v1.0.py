# -*- coding: utf-8 -*-
# =============================================================================
# =============================================================================
#
# F4E_D_2R9B67 PloMa -- Plotting of scattered 2D data into maps
# Application to FRS seismic data
#
# =============================================================================
# =============================================================================

# Jordi Ayneto
# jordi.ayneto@f4e.europa.eu
# v1.0
# Licensed under the EUPL, Version 1.2

'''
This script demonstrates the postprocessing of scattered 2D data into "maps", 
providing:
    - data points with associated numerical values
    - interpolated contour color fields
    - overlayed "plan" drawing

This script is provided as a demonstration of the recommended postprocessing 
to be performed when seismic FRS data is massively produced from analysis.

The user is supposed to incorporate this example in recursive and more complex
scripts.

Input data
This scripts considers, for demonstration purposes, an already preprocessed set
of data, that provides node numbers, node coordinates (2D) and associated FRS
data (pseudoaccelerations).

Output produced
A plot file is written presenting the elements described above.
'''


# Imports
import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib.cbook as cbook
import scipy.interpolate
from imageio import imread

# Definitions

FRS_Data       = np.loadtxt('B2_Data.txt', skiprows = 1)
Level_Drawing  = '\\Drawings\\B2.png'

path = os.getcwd()

# Source data
'''
The source data is a list of nodes, with 2D locations and pseudoacceleration
values (Saz, ZPAz in this example)

Node     x-coord    y-coord    Saz    ZPAz
5        090.425    049.225    010.230    002.880
47       060.375    045.400    006.150    002.030
55       060.375    049.225    007.150    002.060
[...]
'''



# Produce level-by-level FRS maps
# =============================================================================
# 

# Identify data
Nodes = FRS_Data[:,0]
x     = FRS_Data[:,1]
y     = FRS_Data[:,2]
Saz   = FRS_Data[:,3]
ZPAz  = FRS_Data[:,4]

# Plot instance
plt.figure(figsize = (10,8))

# Use plan drawing
plan = cbook.get_sample_data(path + Level_Drawing)
img = imread(plan)
plt.imshow(img, zorder=0, extent=[min(x), max(x), min(y), max(y)])

# Generate and overlay interpolated field
rbf = scipy.interpolate.Rbf(x, y, Saz, function = 'linear')
xi, yi = np.linspace(min(x), max(x), 200), np.linspace(min(y), max(y), 200)
xi, yi = np.meshgrid(xi, yi)
zi = rbf(xi, yi)

colormap = plt.get_cmap('jet')
plt.imshow(zi,
           vmin = np.amin(zi), vmax = np.amax(zi),
           origin = 'lower',
           extent=[min(x), max(x), min(y), max(y)], cmap=colormap,
           alpha=0.4)

# Add scatter data with associated values
plt.scatter(x, y, s = 16, c = Saz, cmap = colormap)
plt.colorbar(shrink = 0.8, label = '$[m/s^2]$')

for i, txt in enumerate(Saz):
    plt.annotate('{0:3.2f}'.format(txt), (x[i], y[i]), fontsize = '7')
del i, txt

# Complete plot with labels
plt.title('Saz at level B2 @ 4% damping', fontsize=20, y=1.03)
plt.xlabel('X $[m]$')
plt.ylabel('Y $[m]$')

# Save
plt.savefig('Saz.png', dpi = 300, bbox_inches='tight')
plt.close()

# End
