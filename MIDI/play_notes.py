""" Send notes to MIDI device """
from midi_utils import send_notes, midiout, init_rtmidi

init_rtmidi(port=0)

with midiout:
    for bar in range(4):
        send_notes(pitch=60, repeat=4)
        send_notes(pitch=62, repeat=4)
        send_notes(pitch=67, repeat=4)
        send_notes(pitch=58, repeat=4)
