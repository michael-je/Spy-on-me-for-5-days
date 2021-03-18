from pythonosc import udp_client
from rtmidi.midiutil import open_midiinput
from time import sleep

local_IP = "127.0.0.1"
pi_IP = "192.168.1.227"

print("\nWhere would you like to connect?")
selection = input("local/pi? > ")
if selection == "pi" or selection == "p":
	UDP_IP = pi_IP
else:
	UDP_IP = local_IP

# variables
# UDP_IP =  override
UDP_PORT = 6031

print(f"\nCurrent IP is: {UDP_IP}\nCurrent Port is: {UDP_PORT}")
print("OSC messages are sent in the form:\nbank, control type, control number, value.\n")

# instantiate objects
client = udp_client.SimpleUDPClient(UDP_IP, UDP_PORT)

# make sure we only connect to the Alias8
MIDI_PORT = 0
port_name = "0"
while "Alias_8" not in port_name:
	MIDI_PORT += 1
	midiin, port_name = open_midiinput(MIDI_PORT)
	if MIDI_PORT >= 10:
		break

# define midi handler class
class MidiInputHandler(object):
	def __init__(self, port):
		self.port = port

	def __call__(self, event, data=None):
		message, *_ = event
		channel, ctrl_num, val = message
		if channel < 159 :
			ctrl_type = "pad"
			bank = channel - 143
			ctrl_num += 1 
		elif ctrl_num < 17:
			ctrl_type = "knob"
			bank = channel - 175
		elif ctrl_num == 25:
			ctrl_type = "master"
			bank = channel - 175
			ctrl_num = 1
		else:
			ctrl_type = "slider"
			bank = channel - 175
			ctrl_num -= 16
		print(f"bank {bank}, {ctrl_type} {ctrl_num}, value = {val}")
		# print(event)
		client.send_message("/alias8", (bank, ctrl_type, ctrl_num, val))


midiin.set_callback(MidiInputHandler(port_name))

print("Connected to", port_name, "\n")

try:
	while True:
		sleep(0.01)
except KeyboardInterrupt:
	pass
finally:
	midiin.close_port()
	del midiin
	print("\nClosed")