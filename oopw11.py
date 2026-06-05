from dataclasses import dataclass,field
from contextlib import contextmanager
class TrackError(Exception):
    pass
    # def __init__(self,code):
    #     self.code=code
@dataclass
class Track:
    code:str
    title:str
    genre:str
    duration:int
    _status:str=field(init=False,default="PENDING")
    def __post_init__(self):
        if self.duration<=0:
            raise TrackError(f"Invalid duration for {self.code}")
    @property
    def minutes(self):
        return round(self.duration/60,1)
    def __str__(self):
        return f"[{self.code}] {self.title} ({self.genre}, {self.duration}s) -> {self._status}"
    def __gt__(self,other):
        if isinstance(other,Track):
            return self.duration>other.duration
        return NotImplemented
class PlaylistFilter:
    def __init__(self,tracks,genres):
        self.tracks=tracks
        self.genres=genres
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>=len(self.tracks):
            raise StopIteration
        current_track=self.tracks[self.index]
        if current_track.genre in self.genres:
            current_track._status="QUEUED"
        else:
            current_track._status="SKIPPED"
        self.index+=1
        return current_track
def playlist_report(filt):
    queued_count=0
    skipped_count=0
    for track in filt:
        if track._status=="QUEUED":
            queued_count+=1
        else:
            skipped_count+=1
        yield str(track)
    yield f"Summary: {queued_count} queued, {skipped_count} skipped"

class PlaylistSession:
    def __init__(self,name):
        self.name=name
        self._tracks=[]
    def __enter__(self):
        print(f"== Playing: {self.name}==")
        return self
    def add(self,track):
        self._tracks.append(track)
    def filter(self,genres):
        p_filter=PlaylistFilter(self._tracks,genres)
        return playlist_report(p_filter)
    def __exit__(self,exc_type,exc_val,exc_tb):
        if exc_type is TrackError:
            print(f"!!! Error: {exc_val}")
        print(f"=== Stopped: {self.name} ({len(self._tracks)} tracks) ===")
        return exc_type is TrackError
with PlaylistSession("Road Trip") as pl:
    pl.add(Track("T01", "Bohemian Rhapsody", "Rock", 354))
    pl.add(Track("T02", "Blinding Lights", "Pop", 200))
    pl.add(Track("T03", "Clair de Lune", "Classical", 330))

    for line in pl.filter(("Rock", "Pop")):
        print(line)

    print(pl._tracks[0] > pl._tracks[1])

print()

with PlaylistSession("Study Session") as pl:
    pl.add(Track("T04", "White Noise", "Ambient", -60))

    


