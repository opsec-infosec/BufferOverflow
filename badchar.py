#!/usr/bin/python3
import sys

#
# Copyright (C) 2022  Dale Furneaux (opinfosec)
# Released under GNU GPL v2
# Bad Character Generator for Python3
# https://github.com/opsec-infosec/BufferOverflow
#


print("\n")

print("badchars = (")
print("\"", end='')
for x in range(1,256):
    sys.stdout.write ("\\x" + '{:02x}'.format(x))
    if((x % 16) == 0):
        print("\"")
        print("\"", end='')
print("\" )\n")
