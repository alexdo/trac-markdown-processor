# -*- coding: utf-8 -*-

""" Because markdown just rocks!
    Get python-markdown2 from: https://github.com/trentm/python-markdown2

    @author  Alexander Dormann <alexander.dormann@30doradus.de>
    @date    13.10.2012
    @version 1.0-b2
    @package MarkdownProcessor
    @file    processor.py
"""

from trac.core import Component, implements
from trac.wiki.macros import WikiMacroBase
from trac.wiki.formatter import Formatter, system_message

from genshi.builder import tag

import re
from StringIO import StringIO

# links, autolinks, and reference-style links
LINK = re.compile(
    r'(\]\()([^) ]+)([^)]*\))|(<)([^>]+)(>)|(\n\[[^]]+\]: *)([^ \n]+)(.*\n)'
)
HREF = re.compile(r'href=[\'"]?([^\'" ]*)', re.I)

class mdMacro(WikiMacroBase):
    """enables the markdown processor macro."""

    def expand_macro(self, formatter, name, content):

        env = formatter.env
        abs = env.abs_href.base
        abs = abs[:len(abs) - len(env.href.base)]
        f = Formatter(formatter.env, formatter.context)
        
        def convert(m):
            pre, target, suf = filter(None, m.groups())
            out = StringIO()
            f.format(target, out)
            url = re.search(HREF, out.getvalue()).groups()[0]
            # Trac creates relative links, which Markdown won't touch inside
            # <autolinks> because they look like HTML
            if pre == '<' and url != target:
                pre += abs
            return pre + str(url) + suf
            
        try:
            # Import the package
            import markdown2

            """
            Set some cool extras:
             * code-friendly:      ignore _ + __ formattings
             * fenced-code-blocks: syntax highlighting! 
             * header-ids:         doesn't need an expl., right?
             * smarty-pants:       typo goodness (cf. http://daringfireball.net/projects/smartypants)
             * wiki-tables:        render trac-wiki tables within md macro
            """
            markdown_extras = [
                "code-friendly",
                "fenced-code-blocks",
                "header-ids",
                "smarty-pants",
                "wiki-tables",
            ]

            # convert it, FFS!
            return markdown2.markdown(re.sub(LINK, convert, content), extras=markdown_extras)
        except ImportError:
            msg = 'Error importing python-markdown2, install it from '
            url = 'https://github.com/trentm/python-markdown2'
            return system_message(tag(msg, tag.a('here', href="%s" % url), '.'))


class markdownMacro(WikiMacroBase):
    """ an alias so #!markdown may also be used """

    def expand_macro(self, formatter, name, content):
        return mdMacro.expand_macro(formatter, name, content)

