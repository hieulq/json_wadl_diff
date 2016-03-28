from lxml import etree

doc = etree.parse("test.xml")
print etree.tostring(doc)

a = doc.findall("staff")

print "fin"
