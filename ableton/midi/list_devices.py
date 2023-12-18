import rtmidi
import time

midiout = rtmidi.MidiOut()
ports = midiout.get_ports()
print(ports)

def send_notes(pitch=60, repeat=4):
    for note in range(repeat):
        note_on = [0x90, pitch, 80]
        note_off = [0x80, pitch, 0]
        midiout.send_message(note_on)
        time.sleep(0.5)
        midiout.send_message(note_off)


tempo = 0.4

with midiout:
    for bar in range(4):
        send_notes(pitch=60, repeat=4)
        send_notes(pitch=62, repeat=4)
        send_notes(pitch=67, repeat=4)
        send_notes(pitch=58, repeat=4)
