import secrets



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



# ============================= OSC ========================================
# ports for osc connections
qlc_osc_port = 7700 # listed here but actually configured in pd
pd_osc_port = 7699
rpi_osc_port = 7691

# local ip addresses
desktop_ip = "192.168.1.225"
rpi_ip = "192.168.1.110"



# ============================= ARDUINO ====================================
# arduino
arduino_com_port = "/dev/ttyACM0"
arduino_baud_rate = 9600


# ============================= TEXT2SPEECH ================================
t2s_script_relative_path = "/../text2speech/text2speech.sh"
replacement_words = ["flower,", "kitty,", "sunshine,", "happy,", "wonderful,", "sexy", "handsome", "dreamy"]
lenrp = len(replacement_words)
blacklisted_words = ["anal", "anus", "arrse", "arse", "ass", "ass-fucker", 
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
	"nigga", "niggah", "niggas", "niggaz", "nigger", "niggers", "nob", "nob jokey", "nobhead", "nobjocky", "nobjokey", 
	"numbnuts", "nutsack", "orgasim", "orgasims", "orgasm", "orgasms", "pawn", "pecker", "penis", "penisfucker", 
	"phonesex", "phuck", "phuk", "phuked", "phuking", "phukked", "phukking", "phuks", "phuq", "pigfucker", "pimpis", 
	"piss", "pissed", "pisser", "pissers", "pisses", "pissflaps", "pissin", "pissing", "pissoff", "poop", "porn", 
	"porno", "pornography", "pornos", "prick", "pricks", "pron", "pube", "pusse", "pussi", "pussies", "pussy", "pussys", 
	"rectum", "retard", "rimjaw", "rimming", "sadist", "schlong", "screwing", "scroat", "scrote", 
	"scrotum", "semen", "sex", "shag", "shagger", "shaggin", "shagging", "shemale",
	"shit", "shitdick", "shite", "shited", "shitey", "shitfuck", "shitfull", "shithead", "shiting", "shitings", "shits", 
	"shitted", "shitter", "shitters", "shitting", "shittings", "shitty", "skank", "slut", "sluts", "smegma", "smut", 
	"snatch", "spac", "spunk", "teets", "teez", "testical", "testicle", 
	"tit", "titfuck", "tits", "titt", "tittiefucker", "titties", "tittyfuck", "tittywank", "titwank", "tosser", 
	"turd", "twat", "twathead", "twatty", "twunt", "twunter", "vagina", "viagra", "vulva", 
	"wang", "wank", "wanker", "wanky", "whoar", "whore", "willies", "willy"]


# ============================= MISC =======================================
threads_delay = 1 # delay time inserted into thread loops in seconds
twitch_chat_spam_filter_seconds = 2 # how long the spam filter should ignore messages after last received


# ============================= COMMANDS ===================================
# refer to the example for correct protocol
# use the keyword None if no parameters are needed at an index
command_matches = [
	[
		"command name", 					# 0 command name
		"obs", 								# 1 which program interface to target 
		["match", "any", "of", "these"], 	# 2 match against any word in this list
		["match this phrase"], 				# 3 match against any exact phrase in this list
		[0, 127], 							# 4 if match, check this numeric range
		["extra argument"]					# 5 if match, then also search for this
	],
	[
		"desktop",
		"obs",
		["desktop", "screen","ass"], 
		None,
		None,
		None,
	],
	[
		"facecam",
		"obs",
		["front", "face", "facecam"],
		None,
		None,
		None,
	],
	[
		"roomcam",
		"obs",
		["room"],
		None,
		None,
		None,
	],
	[
		"dmx",
		"pd",
		["light", "lights", "disco"],
		None,
		None,
		["on", "off"]
	],
	[
		"series",
		"rpi",
		["series"],
		None,
		None,
		["on", "off", "brighter", "dimmer"]
	],
	[
		"lamp",
		"rpi",
		["lamp"],
		None,
		None,
		["on", "off"]
	]
]
