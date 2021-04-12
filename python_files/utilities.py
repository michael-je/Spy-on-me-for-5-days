import cfg
import pd_interface
import obs_interface
import rpi_interface
import voice_interface

from datetime import datetime

# interface functions to be called once a command match is found
interface_func_calls = {
	"obs":obs_interface.main,
	"pd": pd_interface.main,
	"rpi": rpi_interface.main,
	"text2speech": voice_interface.text2speech
}


def call_interface(cmd_info, message, sender_username) -> None:
    """Does some checks and then calls the apporopriate interface to handle the command"""
    # check whether the command has been unlocked
    if cmd_info[5]:
        if cmd_info[5] <= datetime.now():
            interface_func_calls.get(cmd_info[1])(cmd_info, message, sender_username)