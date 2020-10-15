import serial, time


SERIALPORT = "/dev/ttyUSB0"
BAUDRATE = 19200


ser = serial.Serial(SERIALPORT,BAUDRATE,timeout=1)  # open serial port
print(f"serial_name = {ser.name}")         # check which port was really used

while 1:
    #ser.write(b'hello')     # write a string
    print(str(ser.readline()))             # close port
