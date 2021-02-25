# recycled twitch bot from my Performuino project
# stores outgoing commands in commands-buffer.txt

# TODO write the extract-commands function
# TODO review the spam_filter function
# TODO test the code

import cfg
import states

import socket
import re
from time import sleep
from datetime import datetime

# store usernames along with last time they sent a message. This is used for the spam filter
chatter_times = {}

# compile regex to match twitch's message formatting
CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
CHAT_MSG_SENDER = re.compile(r"^:\w+")

def main():
    # connect to the twitch API and give credentials provided in cfg
    s = socket.socket()
    s.connect((cfg.HOST, cfg.PORT))
    s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
    s.send("JOIN #{}\r\n".format(cfg.CHAN).encode("utf-8"))

    connected_flag = False # flag will be set to true if we connect to the chat
    while not states.terminate_flag:
        try:
            response_buffer = s.recv(1024).decode("utf-8")
            seperated_responses = [x for x in response_buffer.split('\r\n') if x]

            for raw_response in seperated_responses:
                # When the server sends over a ping we must reply with pong, else we get disconnected
                if raw_response == "PING :tmi.twitch.tv":
                    s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
                    print("PONG sent.")

                # this block runs while the bot is establishing a connection
                elif not connected_flag:
                    if __name__ == "__main__":  # debugging
                        print(raw_response)
                    if raw_response == f':{cfg.NICK}.tmi.twitch.tv 366 {cfg.NICK} #{cfg.CHAN} :End of /NAMES list':
                        connected_flag = True
                        # setblocking(0) along with the try/except block seems to fix the socket blocking problem
                        s.setblocking(False)
                        print("Twitch bot connected.")

                # runs once the bot is connected
                # parses and filters the raw message and appends a command to command-buffer.txt if valid
                else:
                    message = CHAT_MSG.sub("", raw_response)
                    sender_username = CHAT_MSG_SENDER.search(raw_response).group()[1:]
                    
                    if __name__ == "__main__" and message:  # debugging
                        print("raw_response:", raw_response)
                        print("message:", message)
                        print("message_sender:", sender_username)

                    elif message.find('tmi.twitch.tv') == -1 and message:
                        if not spam_filter(sender_username):
                            commands = extract_command(message)
                            if commands:
                                with open("command-buffer.txt", "a") as buffer:
                                    for c in commands:
                                        buffer.write(c)

        # this exception is raised if there is no data in the recv buffer, we want to ignore it and keep running
        except BlockingIOError:
            pass

        sleep(cfg.threads_delay)
        
    s.close()
    print("Twitch bot terminated.")


def spam_filter(chatter):
    # returns True if message should be ignored, false otherwise
    # also manages data in the global chatter_times dictionary
    output = False

    global chatter_times
    now = datetime.now()
    chatter_last_message_time = chatter_times.get(chatter)

    if chatter_last_message_time is not None:       # check whether the chatter already has a recorded time in the dict
        delta_datetime = now - chatter_last_message_time
        time_delta = delta_datetime.total_seconds()
        if time_delta < cfg.twitch_chat_spam_filter_seconds:    # if length between messages is less than set output to True, to block the message
            output = True
        else:
            chatter_times[chatter] = now    # otherwise leave output alone and just update their last message time
    else:
        chatter_times[chatter] = now
    return output


def extract_command(message):
    # parse incoming messages and return any matching commands
    # will always return a list, list will be empty if there are no matching commands
    pass

# currently unused
def send_chat_msg(sock, msg):
    sock.send("PRIVMSG #{} :{}\r\n".format(cfg.CHAN, msg).encode("utf-8"))

if __name__ == "__main__":
    main()
