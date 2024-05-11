import sys,os
if len(sys.argv) < 2:
    print("No valid input file")
    exit(0) 
input_file = sys.argv[1] 
output_file = input_file.split(".")[0] + ".py"
cmds = {"echo":"print(CONTENT,end='')"}
inp = open(input_file,"r")
out = open(output_file,"w")
lines = []
line = ""
char = inp.read(1)
while char:
    if char == ';': 
        lines.append(line)
        line = ""
    else:
        line+=char
    char = inp.read(1)
for line in lines:
    line = line.strip()
    print(line)
    parts = line.split(" ",1)
    cmd = parts[0]
    exp = parts[1] 
    if not "'" in exp:
        exp = eval(exp)
    line = cmds[cmd].replace("CONTENT",str(exp)) 
    out.write(line+"\n")
out.close()
inp.close()


