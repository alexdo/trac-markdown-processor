#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
from setuptools import setup

setup(
    name = 'TracMarkdownMacro',
    packages = ['markdown'],
    version = '1.0-b2',

    author = 'Alexander Dormann',
    author_email = 'alexander.dormann@30doradus.de',
    description = 'Markdown WikiProcessor',
    long_description = 'Uses python-markdown2 to process markdown within trac wiki pages',
    keywords = '0.12 1.0 processor macro wiki markdown',
    url = 'http://alexdo.de',
    license = 'CC-BY-SA 3.0',

    entry_points = { 'trac.plugins': [ 'markdown.macro = markdown.macro' ] },
    classifiers = ['Framework :: Trac'],
    install_requires = ['Trac'],
)
