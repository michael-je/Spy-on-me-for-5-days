# configure initial jac connections
jack_disconnect "PulseAudio JACK Sink:front-left" system:playback_1
jack_disconnect "PulseAudio JACK Sink:front-right" system:playback_2
jack_connect "PulseAudio JACK Sink:front-left" pure_data:input2
jack_connect "PulseAudio JACK Sink:front-right" pure_data:input3
jack_connect pure_data:output2 "PulseAudio JACK Source":front-left
jack_connect pure_data:output3 "PulseAudio JACK Source":front-right

