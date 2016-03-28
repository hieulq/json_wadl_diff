from lxml import etree

parser = etree.XMLParser(load_dtd=True)
doc = etree.parse("wadls/object-api/src/os-object-api-1.0.wadl", parser=parser)

print doc.docinfo.doctype
print doc.findall("resources")

mt = doc.xpath("/method")

print 'fin'
