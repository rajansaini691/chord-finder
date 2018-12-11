# The MIDI maker iterates through a database of chords and automatically
# generates a MIDI file with those chords

from midiutil import MIDIFile
import os

# To be replaced with data from part 1. The chordname doubles as the file name, and it maps to a tuple containing the notes
test_data = {"Cmadd9": ("C", "Eb", "G", "Bb", "D"), "Am": ("A", "C", "E"), "Bb": ("Bb", "D", "F"), "G": ("G", "B", "D"), "F": ("F", "A", "C"), "Fm": ("F", "Ab", "C")}

#Maps between the note name and the corresponding MIDI note value
note_values = {"A": 57, "A#": 58, "Bb": 58, "B": 59, "C": 60, "C#": 61, "Db": 61, "D": 62, "D#": 63, "Eb": 63, "E": 64, "F": 65, "F#": 66, "Gb": 66, "G": 67, "G#": 68, "Ab": 68}

# Arpeggiates chords
delay = 0.05

inversion = 0

# The number of octaves to raise or lower the chord
octave = 1
track = 0
channel = 0
time = 0
duration = 4
tempo = 60
volume = 100

# Creates a directory per soundfont and populates it with wav files
for soundfont in range(1, 23):
	os.system("mkdir " + str(soundfont))

	# Iterates through the test data and generates a MIDI file for each item
	for chord, notes in test_data.items():
		# Creates MIDI files once
		if soundfont == 1:
			MyMIDI = MIDIFile(1)
			MyMIDI.addTempo(track, time, tempo)
	
			# Changes the instrument being played, stored as an integer. For example, 1 -> piano, 6 -> harpsichord
			instrument = 1
			MyMIDI.addProgramChange(0, 0, 0, soundfont);

			# Used for creating rolled chords
			t = 0.0

			# Rotates chord based on inversion
			n = inversion % len(notes)
			notes = notes[n:] + notes[0:n]

			# Keeps chords in root position 
			last_note = 0
			for note in notes:
				pitch = note_values[note] + 12 * octave
				
				if(pitch < last_note): 
					pitch += 12
				else:
					last_note = pitch

				MyMIDI.addNote(track, channel, pitch, t, duration, volume)
				t += delay

			# Creates MIDI files
			with open(chord + ".mid", "wb") as output_file:
				MyMIDI.writeFile(output_file)

		# This part only works on a Linux system with fluidsynth installed
		extension = ".sf2 " if soundfont < 19 else ".SF2 "
		command = "fluidsynth -F " + str(soundfont) + "/" + chord + ".wav soundfonts/" + str(soundfont).zfill(4) + extension + chord + ".mid"
		os.system(command)


