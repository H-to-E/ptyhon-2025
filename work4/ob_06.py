class Playlist:
    def __init__(self,name,tracks=[]):
        self.name=name
        self.tracks=tracks
    def add(self,track):
        self.tracks.append(track)
    def count(self):
        return len(self.tracks)
    def show(self):
        self.number= Playlist.count(self)
        return "플리명:"+str(self.name)+",곡 수:"+str(self.number)+",곡들:"+str(self.tracks)

pl=Playlist('Mylist')
pl.add('Twomiusone')
pl.add('Readytolove')
pl.show()

