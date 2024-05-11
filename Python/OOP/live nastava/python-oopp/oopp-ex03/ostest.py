import sys  
if sys.platform == 'linux2': print("Computer runs Linux")
elif sys.platform == 'darwin': print("Computer runs MacOS")
else: print("Oh, crap...computer must be running Windows")