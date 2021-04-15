# This is the entry into the script. It parses twitch comments and triggers the rest of the scripts.

import cfg
import utilities
import states
import call_interface_util
import talk_to_michael


import importlib
import socket
import re
import os.path
from datetime import datetime
from time import sleep

# chat log relative path
chat_log_path = utilities.get_file_path(__file__, cfg.chat_log_path)


# compile regex to match twitch's message formatting
CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
CHAT_MSG_SENDER = re.compile(r"^:\w+")


def main() -> None:
	utilities.set_state("terminate_flag", 0)
	utilities.set_state("mpv_mutex", 0)
	
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
				
				# respond to server pings to avoid disconnect
				if raw_response == "PING :tmi.twitch.tv": # reply to server pings
					s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
					print("PONG sent.")
				
				# process user messages
				else:
					# parse raw messages for message contents and username,
					message = CHAT_MSG.sub("", raw_response)
					sender_username = CHAT_MSG_SENDER.search(raw_response).group()[1:]
					
					if message.find('tmi.twitch.tv') == -1 and message:
						# append message to chat log
						log_msg(message, sender_username)
						# send message to output terminal handled by talk_to_michael.py
						talk_to_michael.process_msg(message, sender_username)

						# only run if message is not filtered out
						if not filter_message(sender_username):

							# parse info into correct format
							cmd_info = parse_commands(message, sender_username)

							# if message contained a relevant command then call the appropriate function to execute it
							if cmd_info[0]:
								call_interface_util.call_interface(cmd_info, message, sender_username)

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



chatter_times = {}
def filter_message(chatter) -> bool:
	"""
	Filters out messages, currently only spam. Spam timer is set in .cfg
	returns True if message should be ignored, false otherwise
	"""
	output = False

	now = datetime.now()
	chatter_last_message_time = chatter_times.get(chatter)

	# filter out spammy messages
	# if chatter is already in chatter_times
	if chatter_last_message_time is not None:
		# diff between current message and previous message
		delta_datetime = now - chatter_last_message_time
		time_delta = delta_datetime.total_seconds()
		# if diff is less than time set in .cfg then filter it out
		if time_delta < cfg.twitch_chat_spam_filter_seconds:
			print(f"Spam filter: Message from {chatter} blocked.") #debug
			output = True
	
	# set chatter time to current time
	chatter_times[chatter] = now
	return output


def log_msg(message, sender_username) -> None:
	"""
	logs given message to other/.chat_log file
	"""
	time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	sender = sender_username.ljust(25, ".")
	logstring = f"{time} - {sender}: {message}" + "\n"
	with open(chat_log_path, 'a') as chat_log:
		chat_log.write(logstring)
		print(logstring.strip()) # debug


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
		except ConnectionResetError:
			pass
		sleep(cfg.twitch_bot_loop_delay)


def parse_commands(message, sender_username) -> list:
	"""Compare message against command_matches in cfg.py
	matches are returned as lists along with relevant data in the form
	[command_name, interface, word_match, number_match, argument_match, lock_datetime_object]
	Returns only the first command that the message matches, and only checks first 10 words of the message"""
	# first reload cfg
	importlib.reload(cfg)
	
	message = message.lower()
	message = message.strip()

	cmd_info = [None, None, None, None, None, None, None]
	word_list = message.split()[:10] # only check first 10 words for commands
	# this block checks for matches
	for word in word_list:

		for cmd in cfg.command_matches.values():
			
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

	# checks for extra arguments and appends datetime lock to cmd_info
	# block only runs if match was found
	if cmd_info[0]:
		cmd = cfg.command_matches.get(cmd_info[0])
		for word in word_list:

			if cmd[4] and word.isnumeric():	# check numeric range
				if cmd[4][0] < word < cmd[4][1]:
					cmd_info[4] = word

			if cmd[5] and word in cmd[5]:	# check for arguments
				cmd_info[5] = word

			if cmd_info[4] and cmd_info[5]: # break early if both arguments where satisfied
					break

		cmd_info[6] = cmd[6]

	return cmd_info


if __name__ == "__main__":
	main()
