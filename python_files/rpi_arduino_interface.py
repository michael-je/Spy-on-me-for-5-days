import cfg

from pythonosc import osc_server, dispatcher
import serial

COM_PORT = cfg.arduino_com_port
BAUD = cfg.arduino_baud_rate

OSC_PORT = cfg.rpi_osc_port
IP = cfg.rpi_ip

# Arduino
ser = serial.Serial(COM_PORT, BAUD)


def handler(*args):
	print(args)
	filter_arg, value = args
	try:
		ser.write(str(value).encode())
	except serial.serialutil.SerialException:
		print("Arduino: connection lost")
	except AttributeError:
		print("Arduino: incorrect command")


# OSC Server
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/rpi", handler)

server = osc_server.BlockingOSCUDPServer((IP, OSC_PORT), dispatcher)
try:
	print("starting server")
	server.serve_forever()
except KeyboardInterrupt:
	print("RPi Arduino interface: terminating")
