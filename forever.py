#!/usr/bin/python
from subprocess import Popen
import sys

filename = sys.argv[1]
while True:
    print("\nStarting " + filename)
    p = Popen("python " + filename, shell=True)
    p.wait()

# this is just to make the bot restart when it crashes. cuz it crashes a lot. mainly due to internet disconnects.