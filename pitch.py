from sys import argv
from math import pow

script, bpm = argv

bpm = float(bpm)
SEMITONES = [-1,-2,-3,-4,-5,-6]
x = 1.0594631

for semi in SEMITONES:
    newBPM = round((pow(x,semi)*bpm*1000), -1)/1000
    print (f"{semi} semitones is {newBPM} bpm")
