import cfg
from pythonosc import udp_client
from time import sleep

PORT = cfg.rpi_osc_port
IP = cfg.rpi_ip
client = udp_client.SimpleUDPClient(IP, PORT)

arguments = {
	"series":{"on":0, "off":1, "brighter":2, "dimmer":3},
	"lamp":{"on":4, "off":5}
}


def main(*args):
	cmd_info, *_ = args

	if cmd_info[5]:
		# The UDP protocol does not connect until we send a message,
		# this might lead to dropped messages
		# that's why we spam a bit before sending
		for _ in range(5):
			client.send_message("/trash", "x")
		client.send_message("/rpi", arguments.get(
			cmd_info[0]).get(
			cmd_info[5]))
		#print("rpi send:", cmd_info)