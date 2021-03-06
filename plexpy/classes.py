# -*- coding: utf-8 -*-

#########################################
## Stolen from Sick-Beard's classes.py ##
#########################################


from __future__ import unicode_literals

from future.moves.urllib.request import FancyURLopener

import plexpy
if plexpy.PYTHON2:
    from common import USER_AGENT
else:
    from plexpy.common import USER_AGENT


class PlexPyURLopener(FancyURLopener):
    version = USER_AGENT


class AuthURLOpener(PlexPyURLopener):
    """
    URLOpener class that supports http auth without needing interactive password entry.
    If the provided username/password don't work it simply fails.

    user: username to use for HTTP auth
    pw: password to use for HTTP auth
    """

    def __init__(self, user, pw):
        self.username = user
        self.password = pw

        # remember if we've tried the username/password before
        self.numTries = 0

        # call the base class
        FancyURLopener.__init__(self)

    def prompt_user_passwd(self, host, realm):
        """
        Override this function and instead of prompting just give the
        username/password that were provided when the class was instantiated.
        """

        # if this is the first try then provide a username/password
        if self.numTries == 0:
            self.numTries = 1
            return (self.username, self.password)

        # if we've tried before then return blank which cancels the request
        else:
            return ('', '')

    # this is pretty much just a hack for convenience
    def openit(self, url):
        self.numTries = 0
        return PlexPyURLopener.open(self, url)
