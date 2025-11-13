import os

base_dir = os.path.dirname(__file__)
infile= os.path.join(base_dir,input('파일명을 입력하세요:'))


with open(infile,"r") as infile:
    freqs={}
    for line in infile:
        for char in line.strip():
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char]+=1

print(freqs)