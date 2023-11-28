import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

sr = 44100
freq = 500
lenght = 1.0

t = np.arange(0, lenght, 1.0/sr)
x = np.pi * 2 * freq * t

plt.plot(t, x)
plt.show()
