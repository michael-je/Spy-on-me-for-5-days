import cfg
import utilities

from time import sleep
import threading
from datetime import datetime

path_to_text4michael = utilities.get_file_path(__file__, "other/text4michael.txt")


def process_msg(_cmd_info, message, sender_username) -> None:
	"""
	Entry point for script to receive commands. Launches threads which append
	text to other/text4michael
	"""
	write_to_text4michael_thread = threading.Thread(
		target=write_to_text4michael, args=(message, sender_username))
	write_to_text4michael_thread.start()


def write_to_text4michael(message, sender_username) -> None:
	"""
	format text, then wait for other/text4michael.txt to be available to
	append the text to it
	"""
	# format text
	time = datetime.now().strftime("%H:%M:%S")
	logstring = f"{time} - {sender_username}: {message}" + "\n"
	
	# wait for mutex to unlock
	while utilities.talk_to_michael_mutex:
		sleep(0.5) 
	# lock mutex
	utilities.talk_to_michael_mutex = 1
	# start the mpv script
	
	with open(path_to_text4michael, 'a') as file4michael:
		file4michael.write(logstring)

	# unlock mutex
	utilities.talk_to_michael_mutex = 0


def print_to_term() -> None:
	"""
	Reads from other/text4michael.txt and prints contents to terminal
	sleepts for one second every loop
	"""
	while not utilities.get_state("terminate_flag"):
		text = ""
		# wait for mutex to unlock
		while utilities.talk_to_michael_mutex:
			sleep(0.1) 
		# lock mutex
		utilities.talk_to_michael_mutex = 1
		# start the mpv script

		with open(path_to_text4michael, 'r+') as file4michael:
			text = file4michael.read()
			file4michael.seek(0)
			file4michael.truncate()
		
		# only print if there was a message
		if text:
			print(text, end="")

		# unlock mutex
		utilities.talk_to_michael_mutex = 0

		sleep(1)




if __name__ == "__main__":
	print_to_term()
