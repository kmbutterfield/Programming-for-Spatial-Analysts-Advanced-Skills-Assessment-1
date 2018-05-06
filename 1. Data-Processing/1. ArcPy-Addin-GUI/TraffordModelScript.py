'''
    -*- coding: utf-8 -*-
    Python Version: 3.6
    Course: GEOG5790M; Advanced Skills; @UniversityofLeeds
    Practical: 1,2,3; ArcPy, Addin, GUI/Display
    Author: kmbutterfield
    File name: TraffordModelScript.py
    Description: Buffers a burglary point and lists buildings at risk of crime.
                 Requires ArcGIS and shapefiles from "albertsquare".
'''

import arcpy
import pythonaddins

arcpy.env.workspace = "D:/Kim/Documents/University/GEOG5790M/Programming-for-Spatial-Analysts-Advanced-Skills-Assessment-1/1. Data-Processing/1. ArcPy-Addin-GUI"

# Delte shapefile if it already exists
if arcpy.Exists("crime.shp"):
    arcpy.Delete_management ("crime.shp")

Burglaries = arcpy.GetParameterAsText(0)
Distance = arcpy.GetParameterAsText(1)
Buildings = arcpy.GetParameterAsText(2)
Out = "crime.shp"

# Import the toolbox "Models" with four variables.
arcpy.ImportToolbox("D:/Kim/Documents/University/GEOG5790M/Programming-for-Spatial-Analysts-Advanced-Skills-Assessment-1/1. Data-Processing/1. ArcPy-Addin-GUI/Models.tbx", "models")
arcpy.TraffordModel_models(Buildings, Out, Burglaries, Distance)

if arcpy.Exists("crime_sorted.shp"):
    arcpy.Delete_management ("crime_sorted.shp")
arcpy.Sort_management(Out, "crime_sorted", [["Join_Count", "DESCENDING"]])

''' Import the crime data '''

# Select the current map document.
mxd = arcpy.mapping.MapDocument("CURRENT")
df = mxd.activeDataFrame
newlayer = arcpy.mapping.Layer("crime_sorted.shp")
# Create a new layer containing the crime data.
layerFile = arcpy.mapping.Layer("D:/Kim/Documents/University/GEOG5790M/Programming-for-Spatial-Analysts-Advanced-Skills-Assessment-1/1. Data-Processing/1. ArcPy-Addin-GUI/0. albertsquarebuildings.lyr")
# Update the crime data layer with colour.
arcpy.mapping.UpdateLayer(df, newlayer, layerFile, True)
#  Request symbology to be based on "Joint_Count".
newlayer.symbology.valueField = "Join_Count"
# Sum the Join_Count values to enable different colours.
newlayer.symbology.addAllValues()
# Add the data layer to the map at the TOP.
arcpy.mapping.AddLayer(df, newlayer,"TOP")
