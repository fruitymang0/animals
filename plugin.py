import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('Animals')
except:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x:x
    
    
class Animals(callbacks.Plugin):
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

    
Class = Animals

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
