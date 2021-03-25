import secrets

# connection to twitch server
HOST = "irc.chat.twitch.tv"
PORT = 6667
# credentials for twitch bot account are stored in a separate file
NICK = secrets.NICK # bot channel name
PASS = secrets.PASS # bot oauth token https://twitchapps.com/tmi/
CHAN = secrets.CHAN # streaming channel name


threads_delay = 1 # delay time inserted into thread loops in seconds
twitch_chat_spam_filter_seconds = 2 # how long the spam filter should ignore messages after last received


# refer to the example for correct protocol
# use the keyword None if no parameters are needed at an index
command_matches = [
	[
		"command name", # command name, duh
		"obs", # which program interface to target 
		["match", "any", "of", "these"], # match against any word in this list
		["match this phrase"], # match against any exact phrase in this list
		[0, 127], # numeric range to match
	],
	[
		"desktop",
		"obs",
		["desktop"], 
		None,
		None,
	],
	[
		"facecam",
		"obs",
		["front", "face", "facecam"],
		None,
		None,
	],
	[
		"roomcam",
		"obs",
		["room"],
		None,
		None,
	]
]