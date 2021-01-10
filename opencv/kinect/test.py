from primesense import openni2
import cv2 as cv

openni2.initialize()     # can also accept the path of the OpenNI redistribution

dev = openni2.Device.open_any()
# dev.get_sensor_info(openni2.Device.)

depth_stream = dev.create_depth_stream()
depth_stream.start()
frame = depth_stream.read_frame()
frame_data = frame.get_buffer_as_uint16()

# cv.imshow('Test',frame)

depth_stream.stop()

cv.waitKey(0)

openni2.unload()