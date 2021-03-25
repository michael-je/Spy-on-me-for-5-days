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

# commands
