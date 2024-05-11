import re 

sentences = [];
sentences.append("A tank is a large type of armoured fighting vehicle with tracks, designed for front-line combat.");
sentences.append("Modern tanks are strong mobile land weapons platforms, mounting a large-calibre cannon in a rotating gun turret.");
sentences.append("They combine this with heavy vehicle armour providing protection for the crew of the weapon and operational mobility, which allows them to position on the battlefield in advantageous locations.");
sentences.append("These features enable the tank to have enormous capability to perform well in a tactical situation: the combination of strong weapons fire from their tank gun and their ability to resist enemy fire means the tank can take hold of and control an area of the battle and prevent other enemy vehicles from advancing, for example.");

word = input("Enter word: ");
pattern = re.compile(word);
for s in sentences:
    if pattern.search(s):
        print(s)