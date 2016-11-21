#!/usr/bin/env python

"""\
Ex2_main

Usage:
  ex2 [<nothing>]
  ex2 (-h|--help)
  ex2 --version
"""

__version__ = "{MAJOR}.{MINOR}.{PATCH}-{HASH}"

from docopt.docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__,version=__version__)
    print("I'm a dummy program and i do nothing but y have a version!")