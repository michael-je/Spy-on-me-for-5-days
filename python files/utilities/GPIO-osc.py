import RPi.GPIO as GPIO
from pythonosc import udp_client
from time import sleep

PRINT_MSG = True

# configure IP address and port
IP_ADDR = "127.0.0.1"
UDP_PORT = 6031 # same as script script running on mbp

# PI board type
GPIO.setmode(GPIO.BOARD)

# set up GPIO pins here
INPUT_PINS = [11]
GPIO.setup(INPUT_PINS, GPIO.IN)

# set up OSC client
client = udp_client.SimpleUDPClient(IP_ADDR, UDP_PORT)


while True:
    for pin in INPUT_PINS:
        pin_val = GPIO.input(pin)
        client.send_message("/GPIO", (pin, pin_val))
        if PRINT_MSG:
            print(f"{pin}, {pin_val}")
    sleep(0.01)