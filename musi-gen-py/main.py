import winsound
import random
from pydub import AudioSegment
from pydub.playback import play
import sys
#default stuff, note: try to integrate octaves
end_gen = True
A = AudioSegment.from_wav("a.wav")
Asharp  = AudioSegment.from_wav("asharp.wav")
B = AudioSegment.from_wav("b.wav")
C = AudioSegment.from_wav("c.wav")
Csharp = AudioSegment.from_wav("csharp.wav")
D = AudioSegment.from_wav("d.wav")
Dsharp = AudioSegment.from_wav("dsharp.wav")
E = AudioSegment.from_wav("e.wav")
F = AudioSegment.from_wav("f.wav")
Fsharp = AudioSegment.from_wav("fsharp.wav")
G = AudioSegment.from_wav("g.wav")
Gsharp = AudioSegment.from_wav("gsharp.wav")

#scale and bpm, default for scale is C major but i built that into the generator
scale = input('What scale do you want the piece in? ')
try:
    bpm = int(input('what do you want the bpm to be? '))
except:
    bpm = 120
#timing definitions, in 4/4 because i cant be arsed to do time signatures
whole = (60/bpm)*1000
half = whole/2
quarter = half/2
eighth = quarter/2
notes = []
timings = []

try:
    max_length = int(input("How long do you want the piece to be? "))
except:
    max_length = whole * 8
#does what it says on the tin, returns a tuple of note pitch and whatever the timing is
def generate_note(scale, piece_length, max_length):
    timing = 0
    if scale == 'C major':
        possible_picks = [C, D, E, F, G, A, B, C]
    elif scale == 'G major':
        possible_picks = [G, A, B, C, D, E, Fsharp, G]
    elif scale == 'D major':
        possible_picks = [D, E, Fsharp, G, A, B, Csharp, D]
    elif scale == 'A major':
        possible_picks = [A, B, Csharp, D, E, Fsharp, Gsharp, A]
    elif scale == 'E major':
        possible_picks = [E, Fsharp, Gsharp, A, B, Csharp, Dsharp, E]
    elif scale == 'B major':
        possible_picks = [B, Csharp, Dsharp, E, Fsharp, Gsharp, Asharp, B]
    else: 
        possible_picks = [C, D, E, F, G, A, B, C]
    timing = random.choice((whole, half, quarter, eighth))
    piece_length += timing
    return random.choice(possible_picks)[:timing], piece_length
current_len = 0
song_data = []
#the fun part, actually making it
while end_gen:
    song = (generate_note(scale, current_len, max_length))
    song_data.append(song[0])
    current_len = song[1]
    if current_len >= max_length:
        end_gen = False
song = AudioSegment.empty()
for i in range(len(song_data)):
    song = song + song_data[i]
play(song)