import string
txt = '''<div style='text-align:center;width:200px;height:250px;border:1px solid gray;padding:5px;'>
<h2 style='margin:10px;'>$TITLE</h2>
<img src='$IMAGE' width=200 />
<div><a href='$LINK'>Read more</a></div>
</div>'''

dct = {"TITLE":"Tiger 1","IMAGE":"https://upload.wikimedia.org/wikipedia/commons/b/ba/Bundesarchiv_Bild_101I-299-1805-16%2C_Nordfrankreich%2C_Panzer_VI_%28Tiger_I%29.2.jpg","LINK":"https://en.wikipedia.org/wiki/Tiger_I"}
tmp = string.Template(txt)
output = tmp.substitute(dct)
print(output)