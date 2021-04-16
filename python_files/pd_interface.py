import cfg
from pythonosc import udp_client

local = "127.0.0.1"
port = cfg.pd_osc_port
client = udp_client.SimpleUDPClient(local, port)


def main(*args):
	"""
	Send message directly to Pd via OSC
	"""
	cmd_info, *_ = args
	
	args = cmd_info[5]
	if args:
		print("pd send", cmd_info)
		client.send_message(f"/{cmd_info[0]}/{args[0]}", 1)
