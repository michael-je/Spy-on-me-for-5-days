#!/bin/bash

curDir=$(dirname $(realpath $0))
projectDir=$(dirname $(dirname curDir))

# call the expect script with given filename as a background process
$curDir/expect_script.exp $curDir $1  &

# give mpv some time to initialize
sleep 0.3

# reconnect mpv to pure data
# only use the left channel
jack_disconnect mpv:out_0 system:playback_1
jack_disconnect mpv:out_1 system:playback_2
jack_connect mpv:out_0 pure_data:input5
# jack_connect mpv:out_1 pure_data:input7

# wait for child process
wait