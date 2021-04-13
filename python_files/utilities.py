import cfg
import pd_interface
import obs_interface
import rpi_interface
import voice_interface

from datetime import datetime
import os.path

# interface functions to be called once a command match is found
interface_func_calls = {
	"obs":obs_interface.main,
	"pd": pd_interface.main,
	"rpi": rpi_interface.main,
	"text2speech": voice_interface.text2speech
}

# relative path of states file
file_path = os.path.abspath(__file__)
file_dir = os.path.abspath(os.path.join(file_path, os.path.pardir))
file_parent_dir = os.path.abspath(os.path.join(file_dir, os.path.pardir))
states_path = file_parent_dir + "/" + cfg.states_path


def call_interface(cmd_info, message, sender_username) -> None:
    """Does some checks and then calls the apporopriate interface to handle the command"""
    # variable will be set to False if it fails a check
    command_unlocked = True
    
    # check whether the command has been unlocked
    if cmd_info[6]:
        if cmd_info[6] >= datetime.now():
            print(f"utilities: command {cmd_info[0]} is time locked")
            command_unlocked = False
        else:
            print(f"utilities: command {cmd_info[0]} is time unlocked")
    
    if command_unlocked:
        interface_func_calls.get(cmd_info[1])(cmd_info, message, sender_username)


# ============================= STATES ====================================
def print_states() -> None:
    with open(states_path) as states:
        print(states.read().strip())

def check_state(state_name) -> bool:
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

    