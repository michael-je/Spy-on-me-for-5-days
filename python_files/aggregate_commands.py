import call_interface_util
import rpi_interface

# interface functions to be called once a command match is found
interface_func_calls = {
	"rpi":rpi_interface.main,
}

available_commands = {
    "goodmorning":[
        [
            "series",
            "rpi",
            ["series"],
            None,
            None,
            "on",
            None,
	    ],
        [
            "lamp",
            "rpi",
            ["lamp"],
            None,
            None,
            "on",
            None
        ]
    ],
    "goodnight":[
        [
            "series",
            "rpi",
            ["series"],
            None,
            None,
            "off",
            None,
	    ],
        [
            "lamp",
            "rpi",
            ["lamp"],
            None,
            None,
            "off",
            None
        ]
    ]
}


def call_interfaces(cmd_info, message, sender_username) -> None:
    """
    behaves similarly to call_interface_util.call_interface
    This is used for commands that need to communicate with multiple interfaces
    """
    given_command_name = cmd_info[0]
    commands_to_send = available_commands.get(given_command_name)
    
    for command in commands_to_send:
        interface_func_calls.get(command[1])(command, message, sender_username)