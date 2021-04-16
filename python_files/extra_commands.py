"""
	"command name":[
		"command name", 					# 0 command name
		"obs", 								# 1 which program interface to target 
		["match", "any", "of", "these"], 	# 2 match against any word in this list
		["match this phrase"], 				# 3 match against any exact phrase in this list
		[0, 127], 							# 4 if match, check this numeric range
		["extra argument"],					# 5 if match, then also search for this
		datetime(2021, 1, 1, 12, 0, 0)		# 6 time when command becomes available
	],
"""

extra_commands = {

}