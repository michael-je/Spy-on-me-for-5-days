import cfg

from datetime import datetime
import os.path as path
from datetime import datetime


# ============================= FORMATTING ================================
def format_msg_for_logging(message, sender_username) -> str:
	time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	sender = sender_username.ljust(25, ".")
	logstring = f"{time} - {sender}: {message}" + "\n"
	return logstring


# ============================= MUTEXES ===================================
# used by animals and voice_interface 
mpv_mutex = 0
# used by talk_to_michael
talk_to_michael_mutex = 0
# used by term_utils and twitch_bot
twitch_commands_mutex = 0


# ============================= PATH ======================================
def get_file_path(python_file_object, relative_path) -> str:
	"""
	gives absolute path from given __file__ object and relative path
	"""
	file_path = path.abspath(python_file_object)
	file_dir = path.abspath(path.join(file_path, path.pardir))
	file_parent_dir = path.abspath(path.join(file_dir, path.pardir))
	return file_parent_dir + '/' + relative_path


# ============================= STATES ====================================
def print_states() -> None:
	with open(states_path) as states:
		print(states.read().strip())


def get_state(state_name) -> bool:
	with open(states_path) as states:
		line = states.readline()
		
		while line:
			words = line.split()
			if words[0] == state_name:
				return bool(int(words[1]))
			line = states.readline()
		
		return False


def set_state(arg_state_name, arg_state_status) -> None:
	# put states file into a string variable
	with open(states_path, 'r') as state_file:
		states_list = state_file.read().split('\n')

	states_list = [l for l in states_list if l]
	with open(states_path, 'w') as state_file:
		output_text = ""

		for state in states_list:
			state = state.split()
			current_state_name = state[0]
			current_state_status = state[1]
			
			if current_state_name == arg_state_name:
				current_state_status = int(arg_state_status)

			state = f"{current_state_name} {current_state_status}\n"

			output_text += state
		
		state_file.write(output_text)


# ============================= VARIABLES ====================================
# relative path of states file
states_path = get_file_path(__file__, cfg.states_path)