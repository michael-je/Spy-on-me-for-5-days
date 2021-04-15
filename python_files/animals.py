import cfg
import utilities

from time import sleep
import subprocess
import threading
from random import choice
import re

animal_sounds_script_path = utilities.get_file_path(__file__, cfg.animal_sounds_script_path)
animal_soundfiles_path = utilities.get_file_path(__file__, cfg.animal_soundfiles_path)


def create_dict_of_filenames() -> dict:
    """
    Create a dict who's keys are names of available sound files without any suffixes.
    Values are lists containing all variations on that filename. This means that if there are 2 files named
    horse, horse1.mp3 and horse2.mp3, the equivalent dict entry would be horse:[horse1, horse2]
    """
    # get list of animals files
    sound_files = subprocess.check_output([f'ls {animal_soundfiles_path}'], shell=True)
    sound_files = sound_files.decode()
    # list of file names without the .mp3 suffix
    sound_files_list = [x.split('.')[0] for x in sound_files.split('\n') if x]
    
    # turn into a dictionary of lists, where file names of the same name but with different numbers appended,
    # e.g. 'horse1', 'horse2', 'horse3', etc, will be put into a single list in the dict with a key of 'horse'
    sound_files_dict = {}
    for file_name in sound_files_list:
        # filename with numbers stripped
        file_name_pure = ''.join(l for l in file_name if l.isalpha())
        
        if not sound_files_dict.get(file_name_pure): 
            sound_files_dict[file_name_pure] = [file_name]
        else:
            sound_files_dict[file_name_pure].append(file_name)
    
    return sound_files_dict


def play_animal_sound(commands, message, sender_username) -> None:
    """
    First check whether to play a specific animal sound by searching for a match to any
    of the file names after the !animal command. If none is found then play a random one.
    """ 
    sound_files_dict = create_dict_of_filenames()
    # search the message for the next work after the !animal command
    # if that word matches one of the filenames then play a random variation of that name
    # e.g. randomly play horse1.mp3, horse2.mp3 or horse3.mp3 if message contained the word 'horse'
    try:
        animal = re.search(r'!animal (\b\w+\b)', message).group(1)
        file_names_list = sound_files_dict.get(animal)
        
        if file_names_list:
            file_name = choice(file_names_list) + '.mp3'
            play_sound_file(file_name)
            return
    
    except AttributeError: # if the string contains nothing but "!animal"
        pass
    
    # executes if no match was found
    random_file = choice(choice(list(sound_files_dict.values()))) + '.mp3'
    play_sound_file(random_file)


def play_sound_file(sound_file) -> None:
    # wait for mutex to unlock
    while utilities.mpv_mutex:
        sleep(0.5)
    # lock mutex
    utilities.mpv_mutex = 1
    # start the mpv script
    subprocess.call([animal_sounds_script_path, sound_file])
    # unlock mutex
    utilities.mpv_mutex = 0