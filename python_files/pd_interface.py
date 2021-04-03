from pythonosc import udp_client

local = "127.0.0.1"
port = 7699
client = udp_client.SimpleUDPClient(local, port)


def main(*args):
	cmd_info, *_ = args
	print("pd_main", cmd_info)
	if cmd_info[0] == "dmx" and cmd_info[5]:
		if cmd_info[5] == "on":
			client.send_message(f"/dmx", 1)
		else:
			client.send_message(f"/dmx", 0)
