class Playlist:
    def __init__(self,l=[]):
        self.l=l
    def valid_songs(self,song):
        if len(song)>4:
            n=len(song)
            return song[n-4:].lower()==".mp3"
        return False
    def __add__(self,other):
        if self.valid_songs():
            if isinstance(other,Playlist):
                l=self.l+other.l
                return Playlist(l)
            else:
                self.l.append(other)
                return self
    def __contains__(self,other):
        return other in self.l
p1=Playlist()

