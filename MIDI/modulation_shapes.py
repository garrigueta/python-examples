""" Print some modulation shapes """
from midi_utils import modulation_shape_type, modulation_shape

modulation_shape_type("sine")
modulation_shape_type("triangle")
modulation_shape_type("square")
modulation_shape_type("sawtooth")

modulation_shape("sine", 1.0, 2.0)
modulation_shape("saw", 1.0, 2.0)
modulation_shape("square", 1.0, 2.0)
