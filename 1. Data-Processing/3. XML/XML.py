'''
    -*- coding: utf-8 -*-
    Python Version: 3.6
    Course: GEOG5790M; Advanced Skills; @UniversityofLeeds
    Practical: 5; XML
    Author: kmbutterfield
    File name: XML.py
    Description: Validating XML scheme, editing, and converting to HTML.
'''

from lxml import etree

""" Validate the XML files schema """

# Open an XML file
xml2 = open("map2.xml").read()
xml2 = xml2.replace('<?xml version="1.0" encoding="UTF-8"?>',"")
root = etree.XML(xml2)

# Validate the file using XSD
xsd_file = open("map2.xsd")
xsd = etree.XMLSchema(etree.parse(xsd_file))

print(xsd.validate(root))

""" Editing an XML file and transforming to HTML type. """

# Open an XML file
xml1 = open("map1.xml").read()
xml1 = xml1.replace('<?xml version="1.0" encoding="UTF-8"?>',"")
root = etree.XML(xml1)

# Validate the file using DTD
dtd_file = open("map1.dtd")
dtd = etree.DTD(dtd_file)
print(dtd.validate(root))

# Parsing the XML file
print (root.tag)          # "MAP"
print (root[0].tag)       # "POLYGON"
print (root[0].get("id")) # "P1"
print (root[0][0].tag)    # "POINTS"
print (root[0][0].text)   # TEXT "100,100 200,100, 200, 200 100,100 100,100

# Edit the XML file
p2 = etree.Element("polygon")                  # Create the polygon
p2.set("id", "p2")                             # Set attribute
p2.append(etree.Element("points"))             # Append points
p2[0].text = "100,100 100,200 200,200 200,100" # Set points text
root.append(p2)                                # Append the polygon
print(root[1].tag)                             # Print to check

# Transform XML into HTML file
xsl3 = open("map3.xsl").read()      # Read the stylesheet
xsl3 = xsl3.replace('<?xml version="1.0" encoding="UTF-8"?>',"")
xslt_root = etree.XML(xsl3)         # Parse the stylesheet
transform = etree.XSLT(xslt_root)   # Make the transformation
result_tree = transform(root)       # Transform some XML root
transformed_text = str(result_tree)

print(transformed_text)

with open('map3.html', 'w') as f1:
    f1.write(transformed_text)
