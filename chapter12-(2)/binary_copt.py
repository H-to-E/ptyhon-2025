sourcefile=input('원본파일이름을입력하세요')
destinationfile=input('복사파일이름을입력하세요')

with open(sourcefile,'rb')as source:
  with open(destinationfile,'wb') as destinationfile:
    while True:
      chunk=source.read(1024)
      if not chunk:
        break
      print(f'복사중 데이터:{chunk}')

      destinationfile.write(chunk)
print('저장완료')
  
