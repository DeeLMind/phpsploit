"""Phpsploit framework core loader.

This pseudo module is designed to be imported (import lib) from
the phpsploit script launcher (./phpsploit).
It also can be imported from phpsploit root directory through a
python interpreter for debugging purposes.

It loads the phpsploit core, spreading required dependencies
(./deps directory) then overwriting sys.path's first element to
the current directory (./lib/), making all self contained elements
directly importable from python.

"""
# spread phpsploit dependencies and patches
import deps

# use current directory as main python path
import sys, os

basedir = os.path.truepath(sys.path[0]) + os.sep
coredir = os.path.join(basedir, __name__) + os.sep

sys.path[0] = coredir

del deps, sys, os
