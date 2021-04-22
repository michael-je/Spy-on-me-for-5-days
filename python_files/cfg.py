import secrets
import extra_commands

from datetime import datetime


# ============================= TWITCH =====================================
# connection to twitch server
HOST = "irc.chat.twitch.tv"
PORT = 6667

# credentials for twitch bot account are stored in a separate file
try:
	NICK = secrets.NICK # bot channel name
	PASS = secrets.PASS # bot oauth token https://twitchapps.com/tmi/
	CHAN = secrets.CHAN # streaming channel name
except AttributeError:
	print("secrets.py does not exist\ncreating dummy variables")
	NICK = "NICK"
	PASS = "PASS"
	CHAN = "CHAN"

enable_time = True # whether or not to block commands based on time blocking param (index 6 of commands)
twitch_chat_spam_filter_seconds = 2 # block messages from users if sent within this long of each other
twitch_bot_loop_delay = 1 / 1000 # delay (in seconds) between each twitch_bot loop

chat_log_path = "other/.chat_log"


# ============================= OSC ========================================
# ports for osc connections
qlc_osc_port = secrets.qlc_osc_port # listed here but actually configured in pd
pd_osc_port = secrets.pd_osc_port
rpi_osc_port = secrets.rpi_osc_port

# local ip addresses
desktop_ip = secrets.desktop_ip
rpi_ip = secrets.rpi_ip
local_IP = "127.0.0.1"


# ============================= ARDUINO ====================================
# arduino
arduino_com_port = "/dev/ttyACM1"
arduino_baud_rate = 9600


# ============================= ANIMAL SOUNDS ==============================
animal_soundfiles_path = "other/animal_sounds/sound_files"
animal_sounds_script_path = "other/animal_sounds/play_animal_sound.sh"


# ============================= UTILITIES ==================================
states_path = "other/states.txt"


# ============================= MISC =======================================
twitch_chat_spam_filter_seconds = 1 			# how long the spam filter should ignore messages after last received
obs_recording_time_split = 2 * 60 * 60 			# how long to wait between recording splits in OBS in seconds


# ============================= TEXT2SPEECH ================================
t2s_script_path = "text2speech/text2speech.sh"
replacement_words = [
	"flower,", "kitty,", "sunshine,", "happy,", "wonderful,", "sexy", "handsome", "dreamy"
]
replacement_words = replacement_words + extra_commands.extra_replacement_words
lenrp = len(replacement_words)


# modified list from https://github.com/MauriceButler/badwords
blacklisted_words = [
	"anal", "anus", "arrse", "arse", "ass", "ass-fucker", 
	"asses", "assfucker", "assfukka", "asshole", "assholes", "asswhole", 
	"ballbag", "balls", "ballsack", "bastard", "beastial", "beastiality", "bestial", "bestiality", 
	"biatch", "bitch", "bitcher", "bitchers", "bitches", "bitchin", "bitching", "blowjob", 
	"blowjobs", "boiolas", "boner", "boob", "boobs", "booobs", "boooobs", "booooobs", "booooooobs", 
	"breasts", "buceta", "bugger", "bum", "butt", "butthole", "buttmuch", "buttplug",
	"cawk", "chink", "cipa", "clit", "clitoris", "clits", "cnut", "cock", "cock-sucker", "cockface", 
	"cockhead", "cockmunch", "cockmuncher", "cocks", "cocksuck", "cocksucked", "cocksucker", "cocksucking", "cocksucks", 
	"cocksuka", "cocksukka", "cok", "cokmuncher", "coksucka", "coon", "cox", "crap", "cum", "cummer", "cumming", 
	"cums", "cumshot", "cunilingus", "cunillingus", "cunnilingus", "cunt", "cuntlick", "cuntlicker", "cuntlicking", 
	"cunts", "cyalis", "cyberfuc", "cyberfuck", "cyberfucked", "cyberfucker", "cyberfuckers", "cyberfucking",
	"damn", "dick", "dickhead", "dildo", "dildos", "dink", "dinks", "dirsa", "dlck", "dog-fucker", "doggin", "dogging", 
	"donkeyribber", "doosh", "duche", "dyke", "ejaculate", "ejaculated", "ejaculates", "ejaculating", "ejaculatings", 
	"ejaculation", "ejakulate","fag", "fagging", "faggitt", "faggot", "faggs", 
	"fagot", "fagots", "fags", "fanny", "fannyflaps", "fannyfucker", "fanyy", "fatass", "fcuk",
	"feck", "fecker", "felching", "fellate", "fellatio", "fingerfuck", "fingerfucked", "fingerfucker", "fingerfuckers", 
	"fingerfucking", "fingerfucks", "fistfuck", "fistfucked", "fistfucker", "fistfuckers", "fistfucking", 
	"fistfuckings", "fistfucks", "flange", "fook", "fooker", "fuck", "fucka", "fucked", "fucker", "fuckers", 
	"fuckhead", "fuckheads", "fuckin", "fucking", "fuckings", "fuckingshitmotherfucker", "fuckme", "fucks", 
	"fuckwhit", "fuckwit", "fudge packer", "fudgepacker", "fuk", "fuker", "fukker", "fukkin", "fuks", "fukwhit", 
	"fukwit", "fux","gangbang", "gangbanged", "gangbangs", "gaylord", "gaysex", "goatse", 
	"God", "god-dam", "god-damned", "goddamn", "goddamned", "hardcoresex", "hell", "heshe", "hoar", "hoare", "hoer", 
	"homo", "hore", "horniest", "horny", "hotsex", "jack-off", "jackoff", "jap", "jerk-off", "jism", "jiz", "jizm", 
	"jizz", "kawk", "knobjocky", "knobjokey", "kock", "kondum", 
	"kondums", "kum", "kummer", "kumming", "kums", "kunilingus", "labia",
	"master-bate", "masterb8", "masterbat*", 
	"masterbat3", "masterbate", "masterbation", "masterbations", "masturbate", "mothafuck", 
	"mothafucka", "mothafuckas", "mothafuckaz", "mothafucked", "mothafucker", "mothafuckers", "mothafuckin", 
	"mothafucking", "mothafuckings", "mothafucks", "motherfuck", "motherfucked", "motherfucker", 
	"motherfuckers", "motherfuckin", "motherfucking", "motherfuckings", "motherfuckka", "motherfucks", "muff", 
	"mutha", "muthafecker", "muthafuckker", "muther", "mutherfucker", "nazi",
	"nigga", "niggah", "niggas", "niggaz", "nigger", "niggers", 
	"numbnuts", "nutsack", "orgasim", "orgasims", "orgasm", "orgasms", "pawn", "pecker", "penis", "penisfucker", 
	"phonesex", "phuck", "phuk", "phuked", "phuking", "phukked", "phukking", "phuks", "phuq", "pigfucker", "pimpis", 
	"piss", "pissed", "pisser", "pissers", "pisses", "pissflaps", "pissin", "pissing", "pissoff", "porn", 
	"porno", "pornography", "pornos", "prick", "pricks", "pron", "pube", "pusse", "pussi", "pussies", "pussy", "pussys", 
	"rectum", "retard", "rimjaw", "rimming", "sadist", "schlong", "screwing", "scroat", "scrote", 
	"scrotum", "semen", "sex", "shag", "shagger", "shaggin", "shagging", "shemale",
	"shit", "shitdick", "shite", "shited", "shitey", "shitfuck", "shitfull", "shithead", "shiting", "shitings", "shits", 
	"shitted", "shitter", "shitters", "shitting", "shittings", "shitty", "skank", "slut", "sluts", "smegma", "smut", 
	"snatch", "spac", "spunk", "teets", "teez", "testical", "testicle", 
	"tit", "titfuck", "tits", "titt", "tittiefucker", "titties", "tittyfuck", "tittywank", "titwank", "tosser", 
	"turd", "twat", "twathead", "twatty", "twunt", "twunter", "vagina", "viagra", "vulva", 
	"wang", "wank", "wanker", "wanky", "whoar", "whore", "willies", "willy"
]

blacklisted_words = blacklisted_words + extra_commands.extra_blacklisted_words












































# ============================= COMMANDS ===================================
# refer to the example for correct protocol
# use the keyword None if no parameters are needed at an index
# extra commands can be added in the extra_commands.py file!
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

command_matches = {
	"text2speech":[
		"text2speech",
		"text2speech",
		["!say"],
		None,
		None,
		None,
		datetime(2021, 4, 21, 14, 0, 0)
	],
	"desktop":[
		"desktop",
		"obs",
		["!screen"], 
		None,
		None,
		None,
		None
	],
	"facecam":[
		"facecam",
		"obs",
		["!face"],
		None,
		None,
		None,
		None
	],
	"roomcam":[
		"roomcam",
		"obs",
		["!room"],
		None,
		None,
		None,
		datetime(2021, 4, 19, 14, 0, 0)
	],
	"goodmorning":[
		"goodmorning",
		"aggregate_commands",
		["!goodmorning"],
		None,
		None,
		None,
		datetime(2021, 4, 19, 14, 0, 0)
	],
	"goodnight":[
		"goodnight",
		"aggregate_commands",
		["!goodnight"],
		None,
		None,
		None,
		datetime(2021, 4, 19, 14, 0, 0)
	],
	"random_animal":[
		"random_animal",
		"animal_sounds",
		['!animal'],
		None,
		None,
		None,
		datetime(2021, 4, 20, 14, 0, 0)
	]
}
command_matches.update(extra_commands.extra_commands)
