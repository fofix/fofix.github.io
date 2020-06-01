#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime


AUTHOR = 'FoFiX team'
SITENAME = 'Frets On Fire X'
SITETITLE = 'Frets On Fire X'
SITESUBTITLE = ''
SITEURL = 'http://localhost:8000'
SITELOGO = SITEURL + '/images/fofix_logo.png'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

PATH = 'content'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Main page
MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = True
MENUITEMS = (
    ("Blog", "/blog.html"),
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

INDEX_URL = "blog"
INDEX_SAVE_AS = "blog.html"
# pages
PAGE_URL = "pages/{slug}.html"
PAGE_SAVE_AS = "pages/{slug}.html"
# articles
ARTICLE_PATHS = ['blog']
ARTICLE_URL = "blog/{slug}.html"
ARTICLE_SAVE_AS = "blog/{slug}.html"
# static
STATIC_PATHS = ['images']

# Blogroll
LINKS = (
    ("Blog", "/blog.html"),
)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/fofix'),
)

DEFAULT_PAGINATION = 10
COPYRIGHT_YEAR = datetime.now().year

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = "themes/Flex"

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    'post_stats',
]
