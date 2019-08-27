#! /usr/bin/env python

import re
from cgi import escape

def index (environ, start_response)
    """This function will be mounted on "/" and display a link
    to the hello world page."""
    start_response('200 OK', [('Content_Type', 'text/html')])
    return ['''Hello World Application
                This is the Hello World Application:

`continue <hello/>` _   
'''l]
