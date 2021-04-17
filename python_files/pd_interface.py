import cfg
from pythonosc import udp_client

local = cfg.local_IP
port = cfg.pd_osc_port
client = udp_client.SimpleUDPClient(local, port)


def main(*args):
	"""
	Send message directly to Pd via OSC
	If an argument is supplied then it is appended to the routing
	Messages can then be routed within Pd
	"""
	cmd_info, *_ = args

	command_name = "/" + cmd_info[0]
	arg = ""
	if cmd_info[5]:
		arg = "/" + cmd_info[5]
	val = 1
	if cmd_info[4]:
		val = cmd_info[4]
	
	osc_msg = command_name + arg
	#print("pd send", osc_msg, val)
	client.send_message(osc_msg, (val))

