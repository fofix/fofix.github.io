#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'FoFiX team'
SITENAME = 'Frets On Fire X'
SITETITLE = 'Frets On Fire X'
SITESUBTITLE = ''
SITEURL = 'http://localhost:8000'
SITELOGO = '/images/fofix_logo.png'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

PATH = 'content'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Frets On Fire', 'http://fretsonfire.sourceforge.net'),
)

# Social widget
SOCIAL = (
    ('GitHub', 'https://github.com/fofix'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = "themes/Flex"
