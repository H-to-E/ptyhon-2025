import os

def parse_file(path):
    infile = open(path,"r")

    space = 0
    tab = 0

    for line in infile:
        space += line.count(" ")
        tab += line.count("love")

    infile.close()
    return space, tab


base_dir = os.path.dirname(__file__)
filepath= os.path.join(base_dir,input('파일 이름을 입력하세요:'))

space,tab= parse_file(filepath)

print(f'스페이스의 개수:{space}, love의 개수:{tab}')