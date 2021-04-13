import cfg

import os.path
import subprocess
from random import randint

# get relative path of shell script
file_path = os.path.abspath(__file__)
file_dir = os.path.abspath(os.path.join(file_path, os.path.pardir))
file_parent_dir = os.path.abspath(os.path.join(file_dir, os.path.pardir))
t2s_script_path = file_parent_dir + "/" + cfg.t2s_script_path

def text2speech(_commands, message, sender_username) -> None:
    message = message[5:] # remove the "!say " at the beginning of message
    text = f"{sender_username} says: {message}"
    speak(text)


def speak(text) -> None:
    """calls the text2speech shell script"""
    text = filter_text(text)
    subprocess.call([t2s_script_path, text])


def filter_text(text) -> str:
    """filters text by checking all words against cfg.blacklisted_words
    Any matches are replaced with a randomly chosen word from cfg.replacement_words"""
    filtered_word_list = []
    for word in text.split():

        check_word = ''.join(l.lower() for l in word if l.isalnum())
        if check_word in cfg.blacklisted_words:
            word = cfg.replacement_words[randint(0, cfg.lenrp - 1)]

        filtered_word_list.append(word)

    filtered_text = ' '.join(filtered_word_list)
    return filtered_text
