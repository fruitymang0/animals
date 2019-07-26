import requests
import supybot.conf as conf
import supybot.utils as utils
from supybot.commands import *
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
      
class Animals(callbacks.Plugin):
    def doggo(self, irc, msg, args):
        r = requests.get('https://random.dog/woof.json')
        dogURL = r.json()['url']
        irc.reply("{}: {}".format(msg.nick, dogURL))
    doggo = wrap(doggo)

    def cat(self, irc, msg, args):
        r = requests.get('https://aws.random.cat/meow')
        catURL = r.json()['file']
        irc.reply("{}: {}".format(msg.nick, catURL))
    cat = wrap(cat)
    
    
Class = Animals

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
