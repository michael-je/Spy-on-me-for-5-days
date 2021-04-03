import cfg
import states
import pd_interface
import obs_interface

import importlib
import socket
import re
from time import sleep
from time import time

# compile regex to match twitch's message formatting
CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
CHAT_MSG_SENDER = re.compile(r"^:\w+")

# interface functions to be called once a command match is found
interface_func_calls = {
	"obs":obs_interface.main,
	"pd": pd_interface.main
}


def main() -> None:
	s = socket.socket()
	connect(s)
	s.setblocking(False)

	while not states.terminate_flag:
		try:
			importlib.reload(cfg)

			# separate individual messages
			response_buffer = s.recv(1024).decode("utf-8")
			seperated_responses = [x for x in response_buffer.split('\r\n') if x]

			# process each message
			for raw_response in seperated_responses:

				if raw_response == "PING :tmi.twitch.tv": # reply to server pings
					s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
					print("PONG sent.")
				
				else:
					# parse raw messages for message and user data,
					# pass data to parsing function
					message = CHAT_MSG.sub("", raw_response)
					sender_username = CHAT_MSG_SENDER.search(raw_response).group()[1:]
					
					if message.find('tmi.twitch.tv') == -1 and message:
						print(f"\n{sender_username}: {message}") # debug
						cmd_info = parse_commands(message, sender_username)
						print(cmd_info)

						if cmd_info[0]:
							interface_func_calls.get(cmd_info[1])(cmd_info, message, sender_username)


		# this exception is raised if there is no data in the recv buffer,
		# we want to ignore it and keep running
		except BlockingIOError:
			pass

		try:
			sleep(cfg.threads_delay)
		except KeyboardInterrupt:
			break
		
	s.close()
	print("Twitch bot terminated.")


def connect(s) -> None:
	"""connect to the twitch API via given socket and credentials provided in cfg.py"""
	s.connect((cfg.HOST, cfg.PORT))
	s.send("PASS {}\r\n".format(cfg.PASS).encode('utf-8'))
	s.send("NICK {}\r\n".format(cfg.NICK).encode('utf-8'))
	s.send("JOIN #{}\r\n".format(cfg.CHAN).encode('utf-8'))

	# loop until we are successfully connected
	while not states.terminate_flag:
		try:
			response_buffer = s.recv(1024).decode('utf-8')
			seperated_responses = [x for x in response_buffer.split('\r\n') if x]
			
			for raw_response in seperated_responses:
				if __name__ == "__main__":
					print(raw_response)
				if raw_response == f":{cfg.NICK}.tmi.twitch.tv 366 {cfg.NICK} #{cfg.CHAN} :End of /NAMES list":
					# s.setblocking(False)
					print("Twitch bot connected")
					return
		except BlockingIOError:
			pass
		sleep(cfg.threads_delay)


def parse_commands(message, sender_username) -> list:
	"""Compare message against command_matches in cfg.py
	matches are returned as lists along with relevant data in the form
	[interface, word_match, number_match, argument_match]"""
	start = time()

	message = message.lower()
	message = message.strip()

	cmd_info = [None, None, None, None, None, None]
	word_list = message.split()[:10] # only check first 10 words
	for word in word_list:

		# return at most one command per message
		for cmd in cfg.command_matches:
			
			if cmd[2] and word in cmd[2]: 		# check if any of the words match command keywords
				cmd_info[0] = cmd[0]
				cmd_info[1] = cmd[1]
				cmd_info[2] = word
				break

			elif cmd[3] and message in cmd[3]:	# check if the message matches an exact phrase
				cmd_info[0] = cmd[0]
				cmd_info[1] = cmd[1]
				cmd_info[3] = word
				break

		if cmd_info[0]:
			break

	if cmd_info[0]:
		for word in word_list:

			for cmd in cfg.command_matches:

				if cmd[4] and word.isnumeric():	# check numeric range
					if cmd[4][0] < word < cmd[4][1]:
						cmd_info[4] = word

				if cmd[5] and word in cmd[5]:	# check for arguments
					cmd_info[5] = word

				if cmd_info[4] and cmd_info[5]:
					break

			if cmd_info[4] and cmd_info[5]:
				break

	end = time()
	print(end - start)
	return cmd_info



if __name__ == "__main__":
	main()
