# Extensible Markup Language (XML)
Using provided .dtd, .xml, .xsd, and .xsl files, the code within the "XML.py" script validates the schema of an XML file, performs an edit to the file, and finally transforms it into an HTML file.

The following files are required to run the script:
* XML Maps: "map1.xml" and "map2.xml"
* Schema definition document: "Map2.xsd"
* Document type definition document: "map1.dtd"
* The style sheet: "map3.xsl"

When ran, the model will print either True if the referred XML document does follow the input schema, or False if it doesn't. After, a HTML file is written using the input map XML. 
