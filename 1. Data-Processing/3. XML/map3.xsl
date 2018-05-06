<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0" 
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method='html' version='1.0' encoding='UTF-8' indent='yes'/>

<xsl:template match="/">
<html>
<body>
<h2>Polygons</h2> 
<p>
<xsl:for-each select="/map/polygon">
<P>
<xsl:value-of select="@id"/> :
<xsl:value-of select="points"/>
</P>
</xsl:for-each>
</p>
</body>
</html>
</xsl:template>
</xsl:stylesheet>

