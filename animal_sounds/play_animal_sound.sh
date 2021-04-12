#!/bin/bash

curDir=$(dirname $(realpath $0))

# call the script with given filename
$curDir/expect_script.exp $curDir $1 &

# give mpv some time to initialize
sleep 0.3

# reconnect mpv to pure data
jack_disconnect mpv:out_0 system:playback_1
jack_disconnect mpv:out_1 system:playback_2
jack_connect mpv:out_0 pure_data:input6
jack_connect mpv:out_0 pure_data:input7
