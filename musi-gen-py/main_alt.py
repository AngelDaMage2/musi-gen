import winsound
import random
import time
#default stuff, note: try to integrate octaves
end_gen = True
A, Asharp, B, C, Csharp, D, Dsharp, E, F, Fsharp, G, Gsharp = 220, 233, 247, 262, 277, 294, 311, 330, 349, 370, 392, 415

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
piece_length = whole * 16
notes = []
timings = []

#does what it says on the tin, returns a tuple of note pitch and whatever the timing is
def generate_note(scale):
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
    return random.choice(possible_picks), random.choice([whole, half, quarter, eighth])

#the fun part, actually making it
while end_gen:
    if sum(timings) == piece_length:
        end_gen = False
    elif sum(timings) > piece_length:
        timings[len(timings)-1] /= 2
    else:
        note = generate_note(scale)
        notes.append(note[0])
        timings.append(note[1])
#beep boop
for i in range(len(notes)):
    winsound.Beep(notes[i], int(timings[i]))