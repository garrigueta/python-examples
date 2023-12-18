from mingus.core import chords

chord_progression = ["Cmaj7", "Cmaj7", "Fmaj7", "Gdom7"]

array_of_notes = []
for chord in chord_progression:
    array_of_notes.extend(chords.from_shorthand(chord))

print(array_of_notes)
