# The MIDI maker iterates through a database of chords and automatically
# generates a MIDI file with those chords

from midiutil import MIDIFile
import os

# To be replaced with data from part 1. The chordname doubles as the file name, and it maps to a tuple containing the notes
test_data = {"Am": ("A", "C", "E"), "Bb": ("Bb", "D", "F"), "G": ("G", "B", "D"), "F": ("F", "A", "C"), "Fm": ("F", "Ab", "C")}

#Maps between the note name and the corresponding MIDI note value
note_values = {"A": 57, "A#": 58, "Bb": 58, "B": 59, "C": 60, "C#": 61, "Db": 61, "D": 62, "D#": 63, "Eb": 63, "E": 64, "F": 65, "F#": 66, "Gb": 66, "G": 67, "G#": 68, "Ab": 68}

# The number of octaves to raise or lower the chord
octave = 0

track = 0
channel = 0
time = 0
duration = 4
tempo = 60
volume = 100

# Iterates through the test data and generates a MIDI file for each item
for chord, notes in test_data.items():
    MyMIDI = MIDIFile(1)
    MyMIDI.addTempo(track, time, tempo)

    # Changes the instrument being played, stored as an integer. For example, 1 -> piano, 6 -> harpsichord
    instrument = 6
    MyMIDI.addProgramChange(0, 0, 0, 4);

    for note in notes:
        pitch = note_values[note] + 12 * octave
        MyMIDI.addNote(track, channel, pitch, 0, duration, volume)

    print("Creating file " + chord + ".mid")
    with open(chord + ".mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)

    # This part only works on a Linux system with timidity installed (should work on CSIL machines)
    # It basically converts the MIDI file to a wav file
    command = "timidity " + chord + ".mid -Ow -o " + chord + ".wav"
    os.system(command)

