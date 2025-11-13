import os

base_dir=os.path.dirname(__file__)
file_path=os.path.join(base_dir,"phones.txt")

infile=open(file_path,"r",encoding="UTF-8")
line=infile.readline()

while line != "":
    print(line)
    line=infile.readline()

infile.close()
 