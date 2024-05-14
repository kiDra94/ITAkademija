import xml.etree.ElementTree as ET
tree = ET.parse('movies7.xml')
root = tree.getroot()

print(ET.tostring(root, encoding='utf8').decode('utf8'))