#!/bin/bash

curDir=$(dirname $(realpath $0))
projectDir=$(dirname $(dirname curDir))

# call the expect script with given filename as a background process
# once process is complete, release the mpv_mutex
$curDir/expect_script.exp $curDir $1 && $projectDir/other/unlockMpvMutex.sh &

# give mpv some time to initialize
sleep 0.1

# reconnect mpv to pure data
# only use the left channel
jack_disconnect mpv:out_0 system:playback_1
jack_disconnect mpv:out_1 system:playback_2
jack_connect mpv:out_0 pure_data:input5
# jack_connect mpv:out_1 pure_data:input7
