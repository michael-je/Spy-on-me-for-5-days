import cfg
from pythonosc import udp_client

local = "127.0.0.1"
port = cfg.pd_osc_port
client = udp_client.SimpleUDPClient(local, port)

arguments = {
	"dmx":{"on":1, "off":0}
}


def main(*args):
	cmd_info, *_ = args
	
	if cmd_info[5]:
		print("pd send", cmd_info)
		client.send_message(f"/{cmd_info[0]}", arguments.get(
			cmd_info[0]).get(
			cmd_info[5]))
