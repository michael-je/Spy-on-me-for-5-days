import cfg
import states
import pd_interface
import obs_interface

import socket
import re
from time import sleep

# compile regex to match twitch's message formatting
CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
CHAT_MSG_SENDER = re.compile(r"^:\w+")

# interface functions to be called once a command match is found
interface_func_calls = {
	"obs":obs_interface.main
}


def main() -> None:
	s = socket.socket()
	connect(s)
	s.setblocking(False)

	while not states.terminate_flag:
		try:
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
						print(f"{sender_username}: {message}") # debug
						parse_commands(message, sender_username)

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


def parse_commands(message, sender_username) -> None:
	"""Compare message against command_matches in cfg.py
	If we get a match then call the appropriate interface to process it"""
	word_list = message.split()
	for word in word_list:
		for cmd in cfg.command_matches:
			print(word, cmd)
			if word in cmd[2]:
				interface_func_calls.get(cmd[1])(cmd[0], message, sender_username)



if __name__ == "__main__":
	main()
