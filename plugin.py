import requests
import string
import supybot.conf as conf
import supybot.utils as utils
from supybot.commands import *
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks


def doggo(self, irc, msg, args):
    r = requests.get(url='https://random.dog/woof.json')
    dogURL = r.json()['url']
    irc.reply("%s: %s" % (msg.nick, dogURL))
doggo = wrap(doggo)

def cat(self, irc, msg, args):
    r = requests.get(url='https://aws.random.cat/meow')
    catURL = r.json()['file']
    irc.reply("%s: %s" % (msg.nick, catURL))
cat = wrap(cat)

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
