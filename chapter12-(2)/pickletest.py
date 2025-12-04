import pickle

myMovie={'Superman vs Betman':9.8,'Ironman':"9.6"}

pickle.dump(myMovie,open("save.p","wb"))


myMovie=pickle.load(open("save.p","rb"))
print(myMovie)