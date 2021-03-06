# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from future.builtins import object
from future.builtins import str

import plexpy
if plexpy.PYTHON2:
    import logger
else:
    from plexpy import logger


class DummyObject(object):
    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return self

    def __getattr__(self, attr):
        return self

    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration


PlexObject = DummyObject


def initialize_plexapi():
    from plexapi.server import PlexServer
    global PlexObject
    PlexObject = PlexServer


class Plex(object):
    def __init__(self, url=None, token=None):
        url = url or plexpy.CONFIG.PMS_URL
        token = token or plexpy.CONFIG.PMS_TOKEN
        self.PlexServer = PlexObject(url, token)

    def get_library(self, section_id):
        return self.PlexServer.library.sectionByID(int(section_id))

    def get_library_items(self, section_id):
        return self.get_library(section_id).all()

    def get_item(self, rating_key):
        return self.PlexServer.fetchItem(rating_key)
