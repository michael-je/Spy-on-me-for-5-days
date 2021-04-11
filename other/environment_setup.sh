#!/bin/bash

# launch main pd_sketch, sleep to give it time to connect to jack
pd $(cd ../ && pwd)/pd_files/main_palette/palette1.pd &
sleep 1

# launch catia
catia &

# run jack_setup.sh
./jack_setup.sh

# alias8 python script
python3 $(cd ../ && pwd)/python_files/utilities/alias8_osc.py &

# twitch bot python script
python3 $(cd ../ && pwd)/python_files/twitch_bot.py

# launch obs
