#!/usr/bin/python3
import sys

#
# opsec-infosec -- Bad Character Generator for Python3
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
