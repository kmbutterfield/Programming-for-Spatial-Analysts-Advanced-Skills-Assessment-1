# Creating a Python addin for ArcGIS using ArcPy and GUI; an example

To demonstrate the use of Addins, Arcpy, Arc Toolbar, and sorting data in ArcGIS, code and data was provided to map the risk of burglary. The model created for the demonstration is based on the work by Manchester Police; if a building has been burgled, other buildings within a 400m buffer are at an increased risk of being burgled. The shape files for this demonstration can be found in the "0. albertsquare". The case study area for this demonstration is an area of the East End of London, Albertsquare.

The model created is named the "Trafford Model" and can be found in the toolbox provided in this folder "Models.tbx". The addin creates a 80m buffer around a point of burglary (substantially smaller due to the case study area being smaller, and produces a table of the buildings that are at an increased risk of being burgled (within a 80m radius). Next, the addin creates a new layer file displaying a choropleth map of the buildings at the highest risk of burglary around the burlgary point.The buildings are coloured by at how much of a risk they are of being burgled, and a table is created, sorted by risk.

* To run the addin, your are required to have ArcGIS and Arcpy installed.
