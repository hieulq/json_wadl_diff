from xml.dom import minidom

doc = minidom.parse("wadls/object-api/src/os-object-api-1.0.wadl")

# doc.getElementsByTagName returns NodeList
methods = doc.getElementsByTagName("method")

imp = minidom.getDOMImplementation('')
dtype = doc.doctype

for method in methods:
    mid = method.getAttribute("id")
    if not mid:
        continue
    name = method.getAttribute("name")
    request = method.getElementsByTagName("request")
    response = method.getElementsByTagName("response")

    # if len(request) == 0 or len(response) == 0:
    #     continue

    print ("id: %s, method: %s" % (mid, name))

    # print("id: %s, method: %s, request: %s, response: %s" %
    #       (mid, name, request[0].firstChild.data, response[0].firstChild.data))
