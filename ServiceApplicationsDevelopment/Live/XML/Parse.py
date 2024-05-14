import xml.etree.ElementTree as ET
tree = ET.parse('movies5.xml')
root = tree.getroot()

print(root.tag)
print(root.attrib)

for child in root:
    print(child.tag, child.attrib)

print([elem.tag for elem in root.iter()])

#print(ET.tostring(root, encoding='utf8').decode('utf8'))

for movie in root.iter('movie'):
    print(movie.attrib)

for description in root.iter('description'):
    print(description.text)

print("-----------------------1992----------------------")
# atributi za tag year='1992'
for movie in root.findall("./genre/decade/movie/[year='1992']"):
    print(movie.attrib)

print("-----------------------atribut multiple----------------------")
# atributi za atribut multiple='Yes'
for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
    print(movie.tag, movie.attrib)

# promena
b2tf = root.find("./genre/decade/movie[@title='Back 2 the Future']")
print(b2tf)
b2tf.attrib["title"] = "Back to the Future"
print(b2tf.attrib)

tree.write("movies7.xml")

tkk2 = root.find("./genre/decade/movie[@title='THE KARATE KID']")
print(tkk2)
tkk2.attrib["title"] = "THE KARATE KID 2"
print(tkk2.attrib)

tree.write("movies6.xml")