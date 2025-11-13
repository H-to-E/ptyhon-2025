import os

base_dir = os.path.dirname(__file__)
file_path= os.path.join(base_dir,"phones.txt")

outfile= open(file_path,"w",encoding="UTF-8")

outfile.write("홍길동01001001001")
outfile.write("김철수01781001001")
outfile.write("김영희01471001001")

outfile.close()