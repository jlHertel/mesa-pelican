#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mesa Release Manager'
SITENAME = 'Mesa 3D'
SITESUBTITLE = u'A open source implementation of the openGL spec'
SITEURL = ''

# Default path to read content from. If you don't specify a path after calling the pelican command, this path will be used
PATH = 'content'

# Configure the timezone to use when formatting dates
TIMEZONE = 'America/Los_Angeles'

# Configure how to display the dates
DEFAULT_DATE_FORMAT = '%B %d,%Y'

# Set the default language of the generated files
DEFAULT_LANG = 'en'

# Set the default locale to ignore users C Locale
LOCALE = ('usa', 'en_US')

# Disable Feed generation
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_ATOM = None
FEED_ALL_RSS = None

# Configure how the generated URLs should look like
ARTICLE_URL = '{slug}.html'
PAGE_URL = '{slug}.html'

# Configure where to save files
PAGE_SAVE_AS = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'

# Disable Categories, tags and Authors generation
CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

# Configure how many itens to show per page
DEFAULT_PAGINATION = 10

# Theme configuration
THEME = 'nisarg-theme'

NISARG_SHOW_SIDEBAR = 1
NISARG_PAGINATION_NEXT = u'Next'
NISARG_PAGINATION_PREVIOUS = u'Previous'
NISARG_HEADER = 'images/header.jpg'
NISARG_MINIFY_CSS = 1

NISARG_SIDEBAR = [
    ('Documentation', [
      ('Introduction',            'intro.html'),
      ('News',                    'index.html'),
      ('Developers',              'developers.html'),
      ('Platforms and Drivers',   'systems.html'),
      ('License &amp; Copyright', 'license.html'),
      ('FAQ',                     'faq.html'),
      ('Acknowledgements',        'thanks.html'),
      ('Conformance Testing',     'conform.html')
    ]),

    ('Download / Install', [
      ('Downloading / Unpacking', 'download.html'),
      ('Compiling / Installing',  'install.html'),
      ('Autoconf',                'autoconf.html'),
      ('Precompiled Libraries',   'precompiled.html')
    ]),

    ('Resources', [
      ('Mailing Lists', 'lists.html'),
      ('Bug Database',  'bugs.html'),
      ('Webmaster',     'webmaster.html'),
      ('Mesa/DRI Wiki', 'https://dri.freedesktop.org/')
    ]),

    ('User Topics', [
      ('Shading Language',           'shading.html'),
      ('EGL',                        'egl.html'),
      ('OpenGL ES',                  'opengles.html'),
      ('Environment Variables',      'envvars.html'),
      ('Off-Screen Rendering',       'osmesa.html'),
      ('Debugging Tips',             'debugging.html'),
      ('Performance Tips',           'perf.html'),
      ('Mesa Extensions',            'extensions.html'),
      ('GL Function Name Mangling',  'mangling.html'),
      ('Gallium llvmpipe driver',    'llvmpipe.html'),
      ('VMware SVGA3D guest driver', 'vmware-guest.html'),
      ('Gallium post-processing',    'postprocess.html'),
      ('Application Issues',         'application-issues.html'),
      ('Viewperf Issues',            'viewperf.html')
    ]),

    ('Developer Topics', [
      ('Source Code Repository', 'repository.html'),
      ('Source Code Tree',       'sourcetree.html'),
      ('Utilities',              'utilities.html'),
      ('Help Wanted',            'helpwanted.html'),
      ('Development Notes',      'devinfo.html'),
      ('Coding Style',           'codingstyle.html'),
      ('Submitting patches',     'submittingpatches.html'),
      ('Releasing process',      'releasing.html'),
      ('Source Documentation',   'sourcedocs.html'),
      ('GL Dispatch',            'dispatch.html')
    ]),
    
    ('Links', [
      ('OpenGL website', 'https://www.opengl.org/'),
      ('DRI website', 'https://dri.freedesktop.org/'),
      ('FreeDesktop.org', 'https://www.freedesktop.org/'),
      ('Developer Blogs', 'https://planet.freedesktop.org/')
    ])
]

# Static files
STATIC_PATHS = ['images']
