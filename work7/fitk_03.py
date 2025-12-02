import os
 
base_dir=os.path.dirname(__file__)


infile1=os.path.join(base_dir,input('첫번째 텍스트 파일을 입력하세요:'))
infile2=os.path.join(base_dir,input('두번째 텍스트 파일을 입력하세요:'))
outfile=os.path.join(base_dir,input('저장할 텍스트 파일을 입력하세요:'))


with open(infile1,"r") as in1, open(infile2,"r") as in2, open(outfile,"w",encoding="UTF-8")as out:
    for line in in1:
        out.write(line+"\n")
    for line in in2:
        out.write(line+"\n")






