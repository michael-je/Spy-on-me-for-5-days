#!/bin/bash

# launch main pd_sketch, sleep to give it time to connect to jack
#pd $(cd ../ && pwd)/pd_files/main_palette/palette1.pd &
#sleep 1

# launch catia
catia &

# run jack_setup.sh
$(dirname $(realpath $0))/jack_setup.sh

# twitch bot python script
python3 $(dirname $(realpath $0))/../python_files/twitch_bot.py

# alias8 python script
python3 $(dirname $(realpath $0))/../python_files/alias8_osc.py &

# launch obs
