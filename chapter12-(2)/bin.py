outfile=open("image4.bin","wb")
data_to_write=bytes([255,128,0,1,10,50])

outfile.write(data_to_write)
outfile.close()

infile=open("image4.bin","wb")

bytesArray=infile.read()
infile.close()

print(bytesArray)
print(type(bytesArray))