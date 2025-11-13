import os

base_dir=os.path.dirname(__file__)
file_path=os.path.join(base_dir,"proverbs.txt")
count = 0
with open(file_path,"r") as infile:
    for line in infile:
        line=line.rstrip()
        word_list=line.split()
        for word in word_list:
            print(word)
        count += len(word_list)
    print(f'총 단어의 개수:{count}')

line = "Bad: news: travels: fast."
wordl_ist=line.split(":")
print(wordl_ist)