""" Set of MIDI functions reused across several scripts"""
import time
import numpy as np
import matplotlib.pyplot as plt
import rtmidi
from rtmidi.midiconstants import CONTROL_CHANGE
from scipy import signal
import sys


CHANNEL = 0
CC_NUM = 75
SPEED = 0.02
midiout = rtmidi.MidiOut()


def init_rtmidi(port=0):
    """ Initialize the RtMidi object """
    ports = midiout.get_ports()
    print("Available ports:", ports)
    print("Selected port:", ports[port])
    midiout.open_port(port)


def convert_range(value, in_min, in_max, out_min, out_max):
    """ Map the range value to a 0-127 range """
    l_span = in_max - in_min
    r_span = out_max - out_min
    scaled_value = (value - in_min) / l_span
    scaled_value = out_min + (scaled_value * r_span)
    return np.round(scaled_value)


def send_mod(amplitude, repeat):
    """ A function which will send CC data to a MIDI driver"""
    scaled = []
    for amp in amplitude:
        val = convert_range(amp, -1, 1.0, 0, 127)
        scaled.append(val)
    for _ in range(repeat):
        for value in scaled:
            mod = ([CONTROL_CHANGE | CHANNEL, CC_NUM, value])
            midiout.send_message(mod)
            time.sleep(SPEED)


def send_modulation_shape(repeat=1):
    """ Function which shows a modulation shape """
    t = np.arange(0, 80, 0.1)
    amplitude = np.sin(t)
    plt.plot(t[1:60], amplitude[1:60])
    plt.title("Modulation Shape")
    plt.xlabel('Time')
    plt.ylabel('Amplitude = sin(time)')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.show()
    send_mod(amplitude, repeat)


def modulation_shape_type(signal="sine"):
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


def modulation_shape(shape: str, period: float, max_duration: float):
    """ Function which shows a modulation shape """
    x = np.arange(0, max_duration, 0.01)
    if shape == 'sine':
        y = np.sin(2 * np.pi / period * x)
    elif shape == 'saw':
        y = signal.sawtooth(2 * np.pi / period * x)
    elif shape == 'square':
        y = signal.square(2 * np.pi / period * x)
    else:
        print("That wave is not supported")
        sys.exit()
    plt.plot(x, y)
    plt.ylabel(f"Amplitude = {shape} (time)")
    plt.xlabel('Time')
    plt.title(f'Modulation Shape: {shape}')
    plt.axhline(y=0, color='blue')
    plt.show()


def send_notes(pitch=60, repeat=4):
    """ Send MIDI notes """
    for _ in range(repeat):
        note_on = [0x90, pitch, 80]
        note_off = [0x80, pitch, 0]
        midiout.send_message(note_on)
        time.sleep(0.5)
        midiout.send_message(note_off)
