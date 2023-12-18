import numpy as np
import matplotlib.pyplot as plt


def modulation_shape(signal="sine"):
    """ Function which shows a modulation shape """
    t = np.arange(0, 80, 0.1)

    if signal == "sine":
        amplitude = np.sin(np.pi * 2 * t)
    if signal == "triangle":
        amplitude = np.abs((t/np.pi-0.5) % 2-1)*2-1
    if signal == "square":
        amplitude = np.where(t/np.pi % 2 > 1, -1, 1)
    if signal == "sawtooth":
        amplitude = -((t/np.pi) % 2) + 1

    plt.plot(t[1:60], amplitude[1:60])
    plt.title("Modulation Shape: " + signal)
    plt.xlabel('Time')
    plt.ylabel('Amplitude = sin(time)')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.show()


modulation_shape("sine")
modulation_shape("triangle")
modulation_shape("square")
modulation_shape("sawtooth")
