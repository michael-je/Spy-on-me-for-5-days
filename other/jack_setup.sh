# configure initial jac connections

# =========== DISCONNECT ===========

# disconnect desktop input from system output
jack_disconnect "PulseAudio JACK Sink:front-left" system:playback_1
jack_disconnect "PulseAudio JACK Sink:front-right" system:playback_2

# disconnect system (soundcard) input from Jack source (OBS)
jack_disconnect system:capture_1 "PulseAudio JACK Source":front-left
jack_disconnect system:capture_2 "PulseAudio JACK Source":front-right

# disconnect system (soundcard) input from Pd input
jack_disconnect system:capture_1 pure_data:input0
jack_disconnect system:capture_2 pure_data:input1

# =========== CONNECT ===========

# connect desktop output to Pd input
jack_connect "PulseAudio JACK Sink:front-left" pure_data:input0
jack_connect "PulseAudio JACK Sink:front-right" pure_data:input1

# connect system (soundcard) input to Pd input
jack_connect system:capture_1 pure_data:input2
jack_connect system:capture_2 pure_data:input3

# connect Pd out to Jack Source (into OBS)
jack_connect pure_data:output2 "PulseAudio JACK Source":front-left
jack_connect pure_data:output3 "PulseAudio JACK Source":front-right

