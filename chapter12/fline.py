import os
base_dir = os.path.dirname(__file__)

infile = os.path.join(base_dir,"proverbs.txt")
outfile= os.path.join(base_dir,"numberpro.txt")

with open(infile,"r") as infile , open(outfile,"w")as outfile:
    i =1
    for line in infile:
        outfile.write(f"{str(i)}.{line}\n")
        i +=1
