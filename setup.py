#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
from setuptools import setup

setup(
    name = 'TracMarkdownProcessor',
    packages = ['markdown'],
    version = '1.0-b3',

    author = 'Alexander Dormann',
    author_email = 'alexander.dormann@30doradus.de',
    description = 'Markdown WikiProcessor',
    long_description = 'Uses python-markdown2 to process markdown within trac wiki pages',
    keywords = '1.0 processor wiki markdown',
    url = 'http://alexdo.de',
    license = 'CC-BY-SA 3.0',

    entry_points = { 'trac.plugins': [ 'markdown.macro = markdown.macro' ] },
    classifiers = ['Framework :: Trac'],
    install_requires = ['Trac'],
)
