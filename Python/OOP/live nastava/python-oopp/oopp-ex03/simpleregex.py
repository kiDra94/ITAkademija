import re 
txt = "bing bang bong bung"
p = re.compile("bong")
m = p.search(txt) 
print("String contains word: " + m.group())
print(re.sub(p,"HELLO",txt))