F4E_D_2R9B67 v1.0 PloMa -- Plotting of scattered 2D data into maps

Fusion for Energy - Software Corner routine
Name: PloMa -- Plotting of scattered 2D data into maps v1.0
Description: 
This script demonstrates the postprocessing of scattered 2D data into "maps", providing:
1.	data points with associated numerical values
2.	interpolated contour color fields
3.	overlayed "plan" drawing
This script is provided as a demonstration of the recommended postprocessing to be performed when seismic FRS data is massively produced from analysis. The user is supposed to incorporate this example in recursive and more complex scripts.
Input data
This scripts considers, for demonstration purposes, an already preprocessed set of data, that provides node numbers, node coordinates (2D) and associated FRS data (pseudoaccelerations).
Node     x-coord    y-coord    Saz    ZPAz
5        090.425    049.225    010.230    002.880
47       060.375    045.400    006.150    002.030
55       060.375    049.225    007.150    002.060
[...]
Output
A plot file is written presenting the elements described above.
Contents:
 - PloMa_v1.0.py
 - Documentation
 - License
 - Example (ready to run)
Application
A working example is provided with the script, demonstrating the implementation.
