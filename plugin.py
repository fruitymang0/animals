import requests
from supybot.commands import *
import supybot.plugins as plugins
import supybot.callbacks as callbacks
import supybot.ircdb as ircdb
import supybot.ircmsgs as ircmsgs
import supybot.log as log
import supybot.conf as conf

def doggo(self, irc, msg):
    r = requests.get(url='https://random.dog/woof.json')
    dogURL = r.json()['url']
    irc.reply("%s: %s" % (msg.nick, dogURL))
doggo = wrap(doggo)

def cat(self, irc, msg):
    r = requests.get(url='https://aws.random.cat/meow')
    catURL = r.json()['file']
    irc.reply("%s: %s" % (msg.nick, catURL))
cat = wrap(cat)

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
