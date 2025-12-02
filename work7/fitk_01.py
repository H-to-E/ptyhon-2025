import os
 
base_dir=os.path.dirname(__file__)


infile=input('텍스트 파일 이름을 입력하세요:')
file_path=os.path.join(base_dir,infile)
try :
    openfile=open(file_path,"r")

    line= openfile.readline()
    while line !="":
        print(line)
        line = openfile.readline()

    openfile.close()
except FileNotFoundError as f:
    print(f)
