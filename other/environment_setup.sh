#!/bin/bash

# change terminate_flag to 0
sed -i "s|terminate_flag 1|terminate_flag 0|" $(dirname $(realpath $0))/states.txt

# launch catia
catia &

# launch obs
#obs &

# launch main pd_sketch, sleep to give it time to connect to jack
pd $(dirname $(dirname $(realpath $0)))/pd_files/main_palette/palette1.pd &

# alias8 python script
python3 $(dirname $(dirname $(realpath $0)))/python_files/alias8_osc.py &

sleep 1

# run jack_setup.sh
$(dirname $(realpath $0))/jack_setup.sh

# twitch bot python script
python3 $(dirname $(dirname $(realpath $0)))/python_files/twitch_bot.py
