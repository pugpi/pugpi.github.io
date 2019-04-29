#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
from collections import namedtuple

import os
import yaml

AUTHOR = 'PUG-PI'
SITENAME = 'Python User Group - Piauí'
SITEURL = ''
THEME = 'theme'
SITEIMAGE = '/images/pugpi.jpeg width=200 height=200'

PATH = 'content'

TIMEZONE = 'America/Fortaleza'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Blog', '/archives.html'),)

# Social widget
ICONS = (('github', 'https://github.com/pugpi'),
         ('telegram', 'https://t.me/pugpi'),)

DEFAULT_PAGINATION = False


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

with open('data/events.yml') as events:
    events_converted = yaml.load(events.read())
    EVENTS = []

    # Convert dates to datetimes
    for event in events_converted:
        event['date'] = datetime.strptime(event['date'], '%d-%m-%Y').date()

    # Sort events by date
    for event in sorted(events_converted,
                        key=lambda event: event['date'], reverse=True):
        e = namedtuple('Event', event.keys())(**event)
        EVENTS.append(e)
