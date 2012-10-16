# -*- coding: utf-8 -*-

""" Because markdown just rocks!
    Get python-markdown2 from: https://github.com/trentm/python-markdown2

    @author  Alexander Dormann <alexander.dormann@30doradus.de>
    @date    16.10.2012
    @version 1.0.1-b1
    @package MarkdownProcessor
    @file    processor.py
"""

from trac.core import Component, implements
from trac.wiki.macros import WikiMacroBase
from trac.wiki.formatter import Formatter, system_message
from trac.web.chrome import ITemplateProvider

from genshi.builder import tag

import re
import pkg_resources
from StringIO import StringIO

# links, autolinks, and reference-style links
LINK = re.compile(r'(\]\()([^) ]+)([^)]*\))|(<)([^>]+)(>)|(\n\[[^]]+\]: *)([^ \n]+)(.*\n)')
HREF = re.compile(r'href=[\'"]?([^\'" ]*)', re.I)

# set some cool extras:
MD_EXTRAS = [
    "code-friendly",      # ignore _ + __ formattings
    "fenced-code-blocks", # syntax highlighting!
    "header-ids",         # explains itself by name
    "smarty-pants",       # typo goodness (cf. http://daringfireball.net/projects/smartypants)
    "wiki-tables",         # render trac-wiki tables within md macro
]

class mdMacro(WikiMacroBase):
    """enables the markdown processor macro."""
    implements(ITemplateProvider)
    
    def expand_macro(self, formatter, name, content):

        env = formatter.env
        abs = env.abs_href.base
        abs = abs[:len(abs) - len(env.href.base)]
        f = Formatter(formatter.env, formatter.context)
        
        def convert_links(m):
            pre, target, suf = filter(None, m.groups())
            out = StringIO()
            f.format(target, out)
            url = re.search(HREF, out.getvalue()).groups()[0]
            # Trac creates relative links, which Markdown won't touch inside
            # <autolinks> because they look like HTML
            if pre == '<' and url != target:
                pre += abs
            return pre + str(url) + suf
        
	def emojify(html):
            pattern = ":([a-z0-9\\+\\-_]+):"
            link = "<img alt=\"\\1\" height=\"20\" style=\"vertical-align:middle\" width=\"20\" src=\"/chrome/markdown/emoji/\\1.png\" />"

            emojify_html = re.sub(pattern, link, html)
            return emojify_html

        try:
            # Import & convert
            import markdown2
            # autolink http:// n stuff
            autolinked_content = re.sub(LINK, convert_links, content)
            # convert to markdown
            html = markdown2.markdown(autolinked_content, extras=MD_EXTRAS)
            # substitute emojis
            emojified_html = emojify(html)

            return emojified_html
        except ImportError:
            # no markdown2 package found?
            msg = 'Error importing python-markdown2, install it from '
            url = 'https://github.com/trentm/python-markdown2'
            return system_message(tag(msg, tag.a('here', href="%s" % url), '.'))

    # ITemplateProvider methods
    def get_htdocs_loc(self):
        return pkg_resources.resource_filename('markdown', 'htdocs')
    htdocs_loc = property(get_htdocs_loc)

    def get_htdocs_dirs(self):
        return [('markdown', self.htdocs_loc)]

    def get_templates_dirs(self):
        return []
