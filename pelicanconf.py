#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'SeanRGB'
SITENAME = 'SeanRGB'
SITEURL = 'http://seanrgb.github.io'

PATH = 'content'

TIMEZONE = 'America/Anchorage'

DEFAULT_LANG = 'en'

OUTPUT_PATH = 'output'
PATH = 'content'
LOAD_CONTENT_CACHE = False

#ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
#ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}index.html'

# THEME STUFF (a lot of this is specifically for the Flex theme)

THEME = u'Flex'
SITETITLE = 'Sean RG Barberie'
SITESUBTITLE = 'Drones | Disasters | Data Science'
SITELOGO = './gravatar.png'
DISQUS_SITENAME = 'SeanRGB'
MAIN_MENU = False
ADD_THIS_ID = 'ra-56a037c909478ef3'



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('acuasi', 'http://www.acuasi.alaska.edu'),
#	('software carpentry', 'http://software-carpentry.org'),
 #        ('data carpentry', 'http://www.datacarpentry.org'),
  #       ('esip', 'http://www.esipfed.org'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/SeanBarberie'),
          ('github', 'http://github.com/SeanRGB'),
		('linkedin', 'https://br.linkedin.com/in/seanbarberie/en'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
