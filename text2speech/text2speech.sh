#!/bin/bash

curDir=$(dirname $(realpath $0))
projectDir=$(dirname curDir)

# create the wav file from argument using pico2wave
pico2wave -w=/tmp/t2s.wav "$1"

# call expect script with given text as a background process
# once the process is done, release the mpv_mutex
$(dirname $(realpath $0))/expect_script.exp && rm /tmp/t2s.wav && $projectDir/other/unlockMpvMutex.sh &

# give mpv some time to initialize
sleep 0.3

# reconnect mpv to pure data
jack_disconnect mpv:out_0 system:playback_1
jack_connect mpv:out_0 pure_data:input4
