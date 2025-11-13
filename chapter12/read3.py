import os

base_dir = os.path.dirname(__file__)
file_path= os.path.join(base_dir,"phones.txt")

infile=open(file_path,"r")

for line in infile:
    line=line.rstrip()
    print(line)

line.close()