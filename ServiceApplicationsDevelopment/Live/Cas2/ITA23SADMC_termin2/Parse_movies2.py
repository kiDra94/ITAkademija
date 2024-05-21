# https://www.datacamp.com/tutorial/python-xml-elementtree
import xml.etree.ElementTree as ET
tree = ET.parse('movies5.xml')
root = tree.getroot()

print(root.tag)
print(root.attrib)

for child in root:
    print(child.tag, child.attrib)

print([elem.tag for elem in root.iter()])

print(ET.tostring(root, encoding='utf8').decode('utf8'))

for movie in root.iter('movie'):
    print(movie.attrib)

for description in root.iter('description'):
    print(description.text)

print("-----------------------1992----------------------")
# atributi za tag year='1992'
for movie in root.findall("./genre/decade/movie/[year='1992']"):
    print(movie.attrib)

# atributi za atribut multiple='Yes'
for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
    print(movie.attrib)

#  atributi roditeljskog taga
for movie in root.findall("./genre/decade/movie/format[@multiple='Yes']..."):
    print(movie.attrib)

# atributi taga movie
for movie in root.iter('movie'):
    print(movie.attrib)

# promena
b2tf = root.find("./genre/decade/movie[@title='Back 2 the Future']")
print(b2tf)
b2tf.attrib["title"] = "Back to the Future"
print(b2tf.attrib)

tree.write("movies3.xml")

tree = ET.parse('movies3.xml')
root = tree.getroot()

for movie in root.iter('movie'):
    print(movie.attrib)

for form in root.findall("./genre/decade/movie/format"):
    print(form.attrib, form.text)

import re

for form in root.findall("./genre/decade/movie/format"):
    # Search for the commas in the format text
    match = re.search(',',form.text)
    if match:
        form.set('multiple','Yes')
    else:
        form.set('multiple','No')

# Write out the tree to the file again
tree.write("movies4.xml")

tree = ET.parse('movies4.xml')
root = tree.getroot()

for form in root.findall("./genre/decade/movie/format"):
    print(form.attrib, form.text)

for decade in root.findall("./genre/decade"):
    print(decade.attrib)
    for year in decade.findall("./movie/year"):
        print(year.text, '\n')

for movie in root.findall("./genre/decade/movie/[year='2000']"):
    print(movie.attrib)

print("-------NOVI ELEMENT-----------------")
action = root.find("./genre[@category='Action']")
new_dec = ET.SubElement(action, 'decade')
new_dec.attrib["years"] = '2000s'

print(ET.tostring(action, encoding='utf8').decode('utf8'))

print("------------------------")

xmen = root.find("./genre/decade/movie[@title='X-Men']")
dec2000s = root.find("./genre[@category='Action']/decade[@years='2000s']")
dec2000s.append(xmen)
dec1990s = root.find("./genre[@category='Action']/decade[@years='1990s']")
dec1990s.remove(xmen)

print(ET.tostring(action, encoding='utf8').decode('utf8'))

tree.write("movies6.xml")

tree = ET.parse('movies6.xml')
root = tree.getroot()

print(ET.tostring(root, encoding='utf8').decode('utf8'))





