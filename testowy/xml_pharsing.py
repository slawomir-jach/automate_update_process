import urllib.request
import xml.dom.minidom
import sys

 

xml_str = sys.stdin.read()
xmldoc = xml.dom.minidom.parseString(xml_str) 

 

annotations = xmldoc.getElementsByTagName('annotations')[0]

version = annotations.getAttribute('versions').split(',')[0]

print(version)

