import cfg
import term_utils

def main(cmd_info, message, sender_username):
    if cmd_info[2] == "!commands":
        cmd_list = []
        for cmd in cfg.command_matches:
            cmd_list.append(cmd)
        cmd_txt = "\n - !".join(cmd_list)
        print_txt = "Here's a list of all the current commands:\n - !" + cmd_txt + "\nVisit https://github.com/mikkmakk88/spy-on-me-info for more info."
        term_utils.chat(print_txt)
