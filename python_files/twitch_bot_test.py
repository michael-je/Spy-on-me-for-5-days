# This is the entry into the script. It parses twitch comments and triggers the rest of the scripts.

import cfg
import utilities
# import call_interface_util
import talk_to_michael
import extra_message_parser
# import extra_commands

PASS = "oauth:uz6fa34hp71k42kgnus5igq4cxofl0"
NICK = "testytest1234567890"
CHAN = "testytest1234567890"

























































































# ==================================================================================================================

import importlib
import socket
import re
import os.path
from datetime import datetime
from time import sleep

# remember last PONG message time
last_pong = datetime.now()

# chat log relative path
chat_log_path = utilities.get_file_path(__file__, cfg.chat_log_path)

# twitch_commands relative path
path_to_twitch_commands = utilities.get_file_path(__file__, "other/twitch_commands.txt")


# compile regex to match twitch's message formatting
CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
CHAT_MSG_SENDER = re.compile(r"^:\w+")


def main() -> None:
	s = socket.socket()
	connect(s)
	s.setblocking(False)

	while True:
		# check if last PONG was too long ago
		now = datetime.now()
		delta = now - last_pong
		if delta.seconds >= 600:
			print("\nLAST PONG MORE THAN 6 MINUTES OLD. RECONNECTING\n")
			s.close()
			s = socket.socket()
			connect(s)
			s.setblocking(False)

		# attempt to reconnect to twitch if disconnected every 2 minutes
		time_minutes = datetime.now().minute
		if time_minutes % 2 == 0:
			try:
				connect(s)
				print(f"{datetime.now()} - Twitch bot: Reconnected")
			except OSError:
				pass

		try:		
			# separate individual messages
			response_buffer = s.recv(1024).decode("utf-8")
			seperated_responses = [x for x in response_buffer.split('\r\n') if x]

			# process each message
			for raw_response in seperated_responses:
				print(raw_response)
				
				# respond to server pings to avoid disconnect
				if raw_response == "PING :tmi.twitch.tv": # reply to server pings
					s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
					now = datetime.now()
					print(f"{now} - Twitch bot: PONG sent.")

		# this exception is raised if there is no data in the recv buffer,
		# we want to ignore it and keep running
		except BlockingIOError:
			pass
		try:
			sleep(cfg.twitch_bot_loop_delay)
		except KeyboardInterrupt:
			utilities.set_state("terminate_flag", 1)
			break
		
	s.close()
	print("Twitch bot terminated.")


def connect(s) -> None:
	"""connect to the twitch API via given socket and credentials provided in cfg.py"""
	s.connect((cfg.HOST, cfg.PORT))
	s.send("PASS {}\r\n".format(PASS).encode('utf-8'))
	s.send("NICK {}\r\n".format(NICK).encode('utf-8'))
	s.send("JOIN #{}\r\n".format(CHAN).encode('utf-8'))

	# loop until we are successfully connected
	while True:
		try:
			response_buffer = s.recv(1024).decode('utf-8')
			seperated_responses = [x for x in response_buffer.split('\r\n') if x]
			
			for raw_response in seperated_responses:
				if __name__ == "__main__":
					print(raw_response)
				if raw_response == f":{cfg.NICK}.tmi.twitch.tv 366 {NICK} #{CHAN} :End of /NAMES list":
					# s.setblocking(False)
					print("Twitch bot connected")
					return
		except BlockingIOError:
			pass
		except ConnectionResetError:
			pass
		sleep(cfg.twitch_bot_loop_delay)


if __name__ == "__main__":
	main()
