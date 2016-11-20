#!/usr/bin/env python

"""\
Ex2

Usage:
  ex2 <repository_path> <major> <minor> <patch> <filename>
  ex2 (-h|--help)
"""

from docopt.docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)

    print(arguments)

    # get the hash of the current commit of the repository

        # suprocess module with a git command ?

    # keep the 8 first characters of the hash

    # generate a python file which contains  major, minor, patch & the short hash

# test it with the ex2_main.py

