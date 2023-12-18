from pygame import midi
import math
import itertools
import pyaudio
import numpy as np

SAMPLE_RATE = 4000
FRAMES_PER_BUFFER = 256
NOTE_AMP = 0.1


def get_sin_oscillator(freq=55, amp=1, sample_rate=SAMPLE_RATE):
	increment = (2 * math.pi * freq) / sample_rate
	return (math.sin(v) * amp * NOTE_AMP 
		for v in itertools.count(start=0, step=increment))


def get_samples(notes_dict, num_samples=FRAMES_PER_BUFFER):
	return [sum([int(next(osc) * 127)
		for _, osc in notes_dict.items()])
		for _ in range(num_samples)]

midi.init()
midi_input = midi.Input(device_id=midi.get_default_input_id())

p = pyaudio.PyAudio()
stream = p.open(
	rate=SAMPLE_RATE, channels=1, format=pyaudio.paInt8,
	output=True, frames_per_buffer=FRAMES_PER_BUFFER)

try:
	notes_dict = {}
	while True:
		if notes_dict:
			samples = get_samples(notes_dict)
			samples = np.int8(samples).tobytes()
			stream.write(samples)

		if midi_input.poll():
			for event in midi_input.read(num_events=8):
				(status, note, vel, _), _  = event
				print(event)
				if status == 0x80 and note in notes_dict:
					del notes_dict[note]
				elif status == 0x90 and note not in notes_dict:
					freq = midi.midi_to_frequency(note)
					notes_dict[note] = get_sin_oscillator(freq=freq, amp=vel/127)

except KeyboardInterrupt:
	stream.stop_stream()
	stream.close()
	midi_input.close()
	p.terminate()