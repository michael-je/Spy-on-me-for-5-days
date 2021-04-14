import cfg
import utilities
import random
from time import sleep

import subprocess
import threading

animal_sounds_script_path = utilities.get_file_path(__file__, cfg.animal_sounds_script_path)
animal_soundfiles_path = utilities.get_file_path(__file__, cfg.animal_soundfiles_path)


def play_animal_sound(commands, message, sender_username) -> None:
    if commands[0] == "random_animal":
        play_random_animal()


def play_random_animal() -> None:
    """
    plays a random animals sound from other/animal_sounds/sound_files
    """
    # get list of animals
    sound_files = subprocess.check_output([f'ls {animal_soundfiles_path}'], shell=True)
    sound_files = sound_files.decode()
    sound_files_list = [x for x in sound_files.split('\n') if x]
    
    sound_file = random.choice(sound_files_list)
    play_sound_file(sound_file)


def play_sound_file(sound_file) -> None:
    # wait for mutex to unlock
    while utilities.get_state("mpv_mutex"):
        sleep(0.5)
    # set mutex
    utilities.set_state("mpv_mutex", 1)
    # start the mpv script
    subprocess.call([animal_sounds_script_path, sound_file])