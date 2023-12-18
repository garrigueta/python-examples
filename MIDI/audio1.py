import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

sr = 44100
freq = 200
lenght = 1.0

t = np.arange(0, lenght, 1.0/sr)
x = np.pi * 2 * freq * t

sine = np.sin(np.pi * 2 * freq * t)
sine *= 32767
signal = np.int16(sine)
wavfile.write("./file_sine.wav", sr, signal)

triangle = np.abs((x/np.pi-0.5) % 2-1)*2-1
triangle *= 32767
signal = np.int16(triangle)
wavfile.write("./file_triangle.wav", sr, signal)

square = np.where(x/np.pi % 2 > 1, -1, 1)
square *= 32767
signal = np.int16(square)
wavfile.write("./file_square.wav", sr, signal)

sawtooth = -((x/np.pi) % 2) + 1
sawtooth *= 32767
signal = np.int16(sawtooth)
wavfile.write("./file_sawtooth.wav", sr, signal)
