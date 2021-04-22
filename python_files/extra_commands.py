"""
	"command name":[
		"command name", 					# 0 command name
		"obs", 								# 1 which program interface to target 
		["match", "any", "of", "these"], 	# 2 match against any word in this list MUST BE A LIST,	 EVEN IF THERE IS JUST ONE WORD
		["match this phrase"], 				# 3 match against any exact phrase in this list
		[0, 127], 							# 4 if match, check this numeric range
		["extra argument"],					# 5 if match, then also search for this
		datetime(2021, 1, 1, 12, 0, 0)		# 6 time when command becomes available
	],
"""

# make sure to set the interface to "extra_commands"!

extra_commands = {
	# "music":[
	# 	"music",
	# 	"pd",
	# 	["!music"],
	# 	None,
	# 	None,
	# 	None,
	# 	None
	# ],
	# "dance_like_monkey":[
	# 	"dance_like_monkey",
	# 	"pd",
	# 	["!monketastic"],
	# 	None,
	# 	None,
	# 	None,
	# 	None,
	# ],
	# "high_five":[
	# 	"high_five",
	# 	"",
	# 	"!highfive",
	# 	None,
	# 	None,
	# 	None,
	# 	None
	# ],
	"faster":[
		"faster",
		"pd",
		["!faster"],
		None,
		None,
		None,
		None
	],
	"slower":[
		"slower",
		"pd",
		["!slower"],
		None,
		None,
		None,
		None
	],
	"dirtier":[
		"dirtier",
		"pd",
		["!dirtier"],
		None,
		None,
		None,
		None
	],
	"cleaner":[
		"cleaner",
		"pd",
		["!cleaner"],
		None,
		None,
		None,
		None
	],
	"drunker":[
		"drunker",
		"pd",
		["!drunker"],
		None,
		None,
		None,
		None
	],
	"soberer":[
		"soberer",
		"pd",
		["!soberer"],
		None,
		None,
		None,
		None
	],
	"lights":[
		"lights",
		"pd",
		["!lights"],
		None,
		None,
		["red", "green", "blue", "on", "off"],
		None
	],
	"list_command":[
		"list_commands",
		"extra_commands",
		["!commands"],
		None,
		None,
		None,
		None
	]
}






































extra_blacklisted_words = [

]

extra_replacement_words = [

]





























































	# "lights":[
	# 	"lights",
	# 	"pd",
	# 	["light", "lights", "disco"],
	# 	None,
	# 	None,
	# 	["on", "off", "crazy", "music"],
	# 	None,
	# ],