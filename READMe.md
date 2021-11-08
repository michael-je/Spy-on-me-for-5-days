# My final BA project at Catalyst Berlin

## The Concept
I will be livestreaming my life for 5 days, __Sunday - Thursday__. During this time I'm going to be making live interactive music, playing some games, coding, talking with the audience and just trying to live my life as normally as possible...

You get to choose how much you interact with me during this time. You can of course just sit back and watch whatever I do, but you also have the option to directly engage in what I'm doing.

The first way you can do this is by using some specific commands that I've added to the stream chat. They will allow you to control stuff that happens both with the music and various other things in the room itself.
The stream will start out slow with only a few commands available, but every day at __14 Berlin time (UTC +02:00)__ I will hold a little presentation and introduce something new :)

Secondly, you can give me suggestions on stuff that you would like me to implement. This could, for example, be something you want to hear in the music or a weird new command to add in.

Since this is going to be a long, interactive peek into my life you can expect there to be some slow moments. I hope that you can still enjoy just having me in the background, or peeking in every once in a while and having fun with some of the new commands :)

## The Rules
- You should feel pretty free in how you engage with me, whether mean or nice. However, while I'm completely open to being fucked with myself, I'm not open to hate speech, intolerance or assholery towards others. If you're ruining the experience for other viewers then you will be banned.
- I'm only allowed to leave the room to:
    - go to the bathroom
    - grab food
    - brush my teeth
    - *maybe* shower once if I get really stinky
- New ways to interact will be presented every day at __14 Berlin time (UTC +02:00)__
- I cannot hide what I'm doing from you (*except* very sensitive information, like passwords, emails, etc).
- I'm not allowed to turn off anything that I've given you control over (music, etc). 
- I'm not allowed to check the stream page. This means that I will not know how many people are watching me at any given moment and I will also not be able to see messages that you hide from me.

## The commands
You'll need to first make a twitch account if you don't already have one.

In order to use commands, simply add them to the beginning of your message, for example: "*!hide haha Michael can't see this*"

New commands are added each day, but commands from previous days will still always be available.

#### Sunday
- __!screen__ - switch the view to my computer screen
- __!face__ - switch the view to my facecam
- __!hide__ - hide you message from me, I won't be able to see it in my chat feed.
- __!faster__ - make the music go faster
- __!slower__ - make the music go slower
#### Monday
- __!room__ - switch the view to the room cam
- __!dirtier__ - add some grit to the music
- __!cleaner__ - make the music sound cleaner
- __!drunker__ - make the music stumble around
- __!soberer__ - make the music less drunk
- __!goodnight__ - turn off the lamp in my room
#### Tuesday
- __!goodmorning__ - turn on the lamp in my room
- __!animal__ - play an animal sound! 
    - give it the name of an animal to make that animal's sound. eg: __!animal cow__
- __!lights__ - control the lights in various ways by adding one of the words below. e.g. __!lights blue__
    - __blue__ - turn the lights blue
    - __red__ - turn the lights red
    - __green__ - turn the lights green
#### Wednesday
- __!say__ - Add in text behind the command to speak like a robot. e.g. __!say michael you are a poop__

---
## Requirements
#### Software
- obs-studio
- puredata
- jackd2
- pulseaudio-module-jack
- libttspico*
- expect
- mpv
- catia - https://github.com/falkTX/Cadence
- obs-websocket https://github.com/Palakis/obs-websocket

#### Pure Data external libraries
- zexy
- cyclone
- freeverb~

#### Python libraries
- python-osc
- python-rtmidi
- obs-ws-rc
