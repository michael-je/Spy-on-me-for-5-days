import obs_interface
import utilities

from time import sleep

# twitch_commands relative path
path_to_twitch_commands = utilities.get_file_path(__file__, "other/twitch_commands.txt")

print('Launching term_utils')

def set_blur(state):
    obs_interface.set_blur(state)


def blur(state):
    set_blur(state)


def chat(message, prefix='chat'):
	"""
	send command to twitch_commands.txt to be processed within the twitch_bot.py script
	"""
    # wait for mutex to unlock
	while utilities.twitch_commands_mutex:
		sleep(0.5) 
	# lock mutex
	utilities.twitch_commands_mutex = 1
	# start the mpv script
	
	with open(path_to_twitch_commands, 'a') as twitch_commands_file:
		twitch_commands_file.write(f"{prefix} {message}")

	# unlock mutex
	utilities.twitch_commands_mutex = 0    


def ban(username):
    chat(username, prefix='ban')


help = ', '.join([
	'set_blur/blur(state)',
	'chat(msg)',
	'ban(user)'
])