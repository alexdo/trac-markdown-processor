# About the Processor

This TracProcessor enables the usage of Markdown
(http://daringfireball.net/projects/markdown/) within Trac wiki pages and
issues.

As the existing processors rely on outdated libraries, this one relies on
the actively developed
[python-markdown2](https://github.com/trentm/python-markdown2)
and bundles the following python-markdown2
[extras](https://github.com/trentm/python-markdown2/wiki/Extras):   
code-friendly, fenced-code-blocks, header-ids, smarty-pants, wiki-tables

Since 1.0.1, this processor supports Emojis according to http://emoji-cheat-sheet.com


# Dependencies

* python-markdown2
* pygments
* Trac >= 0.12


# Install

### python-markdown2

To install python-markdown2 run *one* of the following:

    pip install markdown2
    pypm install markdown2      # if you use ActivePython (activestate.com/activepython)
    easy_install markdown2      # if this is the best you have
    python setup.py install

However, everything you need is in "lib/markdown2.py" of the markdown2 repo.
If it is easier for you, you can just copy that file to somewhere on your
PythonPath.


### The Processor

Run *one* of the following commands:

    pip install https://github.com/alexdo/trac-markdown-processor/zipball/master
    easy_install https://github.com/alexdo/trac-markdown-processor/zipball/master

or just clone the repository and run setup.py.


### Enabling the Processor

Navigate to your TracWebAdmin and enable `markdown.processor.*` within the plugin
panel.

If it's easier for you, add the following line to your `trac.ini` in the
`[components]` section:

    markdown.processor.* = enabled


# Quick Usage

Anything within a `#!md` processor tag will be parsed /w markdown:

    {{{
    #!md
    # h1!
    
    Lorem *ipsum* dolor sit **amet**.
    
    :smiley: <- an emoji!

    + One
    + Two
    + Three
    
    ```python
    if True:
        print "hi"
    ```
    
    An example [link](http://example.com/ "With a Title").
    }}}

