import serial, time


SERIALPORT = "/dev/ttyUSB0"
BAUDRATE = 19200


ser = serial.Serial(SERIALPORT,baudrate=BAUDRATE)  # open serial port
print(f"serial_name = {ser.name}")         # check which port was really used
ser.write(b'hello')     # write a string
ser.close()             # close port
