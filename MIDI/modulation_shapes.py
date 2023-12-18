import numpy as np
import matplotlib.pyplot as plt


def modulation_shape(signal="sine"):
    """ Function which shows a modulation shape """
    t = np.arange(0, 80, 0.1)

    if signal == "sine":
        amplitude = np.cos(t)
    if signal == "triangle":
        amplitude = np.abs((t/np.pi-0.5) % 2-1)*2-1
    if signal == "square":
        amplitude = np.where(t/np.pi % 2 > 1, -1, 1)
    if signal == "sawtooth":
        amplitude = -((t/np.pi) % 2) + 1

    plt.plot(t[1:80], amplitude[1:80])
    plt.title("Modulation Shape: " + signal)
    plt.xlabel('Time')
    plt.ylabel('Amplitude = sin(time)')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.show()
    return amplitude


def convert_range(value, in_min, in_max, out_min, out_max):
    l_span = in_max - in_min
    r_span = out_max - out_min
    scaled_value = (value - in_min) / l_span
    scaled_value = out_min + (scaled_value * r_span)
    return np.round(scaled_value)


amp = modulation_shape("sine")

converted_amplitude = []
for number in amp:
    result = convert_range(number, -1.0, 1, 0, 127)
    converted_amplitude.append(result)