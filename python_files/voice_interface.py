import cfg
import utilities

import os.path
import subprocess
from random import randint
from time import sleep
import threading

# get relative path of shell script
t2s_script_path = utilities.get_file_path(__file__, cfg.t2s_script_path)


def text2speech(_commands, message, sender_username) -> None:
    message = message[5:] # remove the "!say " at the beginning of message
    message = filter_text(message)
    text = f"{sender_username} says: {message}"
    
    speech_thread = threading.Thread(target=speak, args=(text,))
    speech_thread.start()


def speak(text) -> None:
    """
    calls the text2speech shell script
    """
    # wait for mutex to unlock
    while utilities.mpv_mutex:
        sleep(0.5) 
    # lock mutex
    utilities.mpv_mutex = 1
    # start the mpv script
    subprocess.call([t2s_script_path, text])
    # unlcok mutex
    utilities.mpv_mutex = 0


def filter_text(text) -> str:
    """
    filters text by checking all words against cfg.blacklisted_words
    Any matches are replaced with a randomly chosen word from cfg.replacement_words
    """
    filtered_word_list = []
    for word in text.split():

        check_word = ''.join(l.lower() for l in word if l.isalnum())
        if check_word in cfg.blacklisted_words:
            word = cfg.replacement_words[randint(0, cfg.lenrp - 1)]

        filtered_word_list.append(word)

    filtered_text = ' '.join(filtered_word_list)
    return filtered_text
