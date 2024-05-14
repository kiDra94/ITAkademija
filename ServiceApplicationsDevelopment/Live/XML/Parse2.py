import xml.etree.ElementTree as ET
tree = ET.parse('movies7.xml')
root = tree.getroot()

print(ET.tostring(root, encoding='utf8').decode('utf8'))

import re

for form in root.findall("./genre/decade/movie/format"):
    # Search for the commas in the format text
    match = re.search(',',form.text)
    if match:
        form.set('multiple','Yes')
    else:
        form.set('multiple','No')

# Write out the tree to the file again
tree.write("movies8.xml")

for decade in root.findall("./genre/decade"):
    print(decade.attrib)
    for year in decade.findall("./movie/year"):
        print(year.text, '\n')