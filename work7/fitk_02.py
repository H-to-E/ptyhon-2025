import os
 
base_dir=os.path.dirname(__file__)


infile=input('텍스트 파일 이름을 입력하세요:')
file_path=os.path.join(base_dir,infile)
check=input('검색 문자열을 입력하세요:')
try :
    openfile=open(file_path,"r")

    count=0

    line= openfile.readline()
    while line !="":
        if check in line:
            count +=1
        line = openfile.readline()

    openfile.close()
except FileNotFoundError as f:
    print(f)
print(f'{check}는 파일 내에서 {count}번 나타납니다')
