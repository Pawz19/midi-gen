import random
from midiutil import MIDIFile
MyMIDI = MIDIFile(1)

degrees = []

for i in range(4):
    tempNotes=[]
    for i in range(5):
        tempNotes.append(random.randrange(24, 72)) 
    degrees.append(tempNotes) 

time=0
for i in range(len(degrees)):
    for pitch in degrees[i]:
        MyMIDI.addNote(0, 0, pitch, time, 4, 90)
    time+=4

with open("random-progression.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)