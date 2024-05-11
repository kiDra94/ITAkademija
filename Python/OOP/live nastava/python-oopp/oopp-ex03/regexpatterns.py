import re
print("Match if string contains characters b, i or f");
p = re.compile("[bif]");  
print(p.search("bing bang bong bung"));

print("Match if string contains characters from d to h");
p = re.compile("[d-h]");  
print(p.search("hello world"));

print("Match if string contains characters from a to c and from e to g");
p = re.compile("[a-ce-g]");  
print(p.search("I will be matched true"));

print("Match if string contains numbers from 0 to 9");
p = re.compile("\\d");  
print(p.search("I don't have any numbers"));