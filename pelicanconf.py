#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'nicktgr15'
SITENAME = u'nicktgr15'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/pelican-alchemy/alchemy'

# SITESUBTITLE = 'Wisdom reveals as I unlearn to learn'

ICONS = [
    ('github', 'https://github.com/nicktgr15'),
    ('linkedin', 'https://www.linkedin.com/in/nikolaos-tsipas-a6103563'),
]

#SITEIMAGE = '/images/main-gray.jpg width=170 height=170'

LINKS = ()

HIDE_AUTHORS = True

SITEMAP_SAVE_AS = 'sitemap.xml'


