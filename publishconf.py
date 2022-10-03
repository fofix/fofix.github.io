# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://fofix.github.io'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
PIWIK_URL = os.getenv('PIWIK_URL')
PIWIK_SITE_ID = os.getenv('PIWIK_SITE_ID')
#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
