import serial
import subprocess
from pythonosc import udp_client
from time import sleep

# configurations
# USB_PORT_NAME_PI = "/dev/ttyACM0"
# USB_PORT_NAME_MAC = "/dev/tty.usbmodem14201"
BAUD_RATE = 115200

LOCAL_ADDR = "127.0.0.1"
MAC_ADDR = "192.168.1.214"
PI_ADDR = "192.168.1.227"
PORT = 6031

# function taken from Perfomuino project
def get_arduino_port():
    # finds the arduino COM port using the os
    ports = subprocess.check_output(["ls /dev/*"], shell=True)
    ports = ports.decode('utf-8')
    ports_list = ports.split('\n')
    for port in ports_list:
        if port.find("usbmodem") != -1:
            return port
        elif port.find("ACM0") != -1:
            return port
    return None

# prompt user for information
print("Which device are you running on?\n")
device = input("mac/pi? > ")
if device == "m" or device == "mac":
    device = "mac"
#     USB_PORT_NAME = USB_PORT_NAME_MAC
# else:
#     USB_PORT_NAME = USB_PORT_NAME_PI

USB_PORT_NAME = get_arduino_port()
if USB_PORT_NAME is None:
    raise Exception("Arduino not found.")

print("Where would you like to connect?\n")
connection = input(f"local/{'pi' if device == 'mac' else 'mac'}? > ")
if connection == "l" or connection == "local":
    IP_ADDR = LOCAL_ADDR
elif device == "mac":
    IP_ADDR = PI_ADDR
else:
    IP_ADDR = MAC_ADDR

# setup
ser = serial.Serial(USB_PORT_NAME, BAUD_RATE)
ser.baudrate = BAUD_RATE

client = udp_client.SimpleUDPClient(IP_ADDR, PORT)

ser.flushInput()

print(f"\nBAUD RATE: {BAUD_RATE}")
print(f"PORT: {PORT}")
print(f"USB PORT: {USB_PORT_NAME}")
print(f"IP ADDR: {IP_ADDR}\n")

# loop
while True:
    read_ser = ser.readline()[0:-2].decode()
    if read_ser == "!":
        pin = int(ser.readline()[0:-2].decode())
        val = int(ser.readline()[0:-2].decode())
        if pin >= 14:
            pin = f"A{pin - 14}"

        client.send_message("/Arduino", (pin, val))
        print(pin, val)
