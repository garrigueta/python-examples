""" Send modulation data via MIDI Port """
from midi_utils import send_modulation_shape, init_rtmidi

init_rtmidi(port=1)
send_modulation_shape(repeat=1)
