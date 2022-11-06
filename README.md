# BufferOverflow
Buffer Overflow Python Scripts

This runs on Linux

Don't forget to turn of ASLR if running on linux, this will temporarily disable ASLR

```
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
```

## Compile
Compile server.c with the Makefile
```
make all
```

## Python Scripts

Don't forget to change the IP address of the server

```python
s.connect(("172.16.110.135", 1337))
```

## Bad Character Generator for Python3

Just a badcharacter generator to copy and paste into your buffer overflow python script

## Fuzzer

Python3 Fuzzer to enable a buffer overflow

## BoF Template for OSCP.exe from TryHackMe

Simple BoF templatae for server

Don't forget to update the payload_shell with your own msfvenom generated reverse shell payload

Adjust the filler buffer to enable the overflow, adjust the eip address (JMP EAX)

Change the payload reference for the extend to caclulate the correct end of the buffer after your payload (this is not necessary, however it keeps the original BoF intact)

```python
filler = "A" * (1036 - ((len(nop_sled)) + len(payload_shell)))  # Filler 1036 Bytes - nop sled - size of payload
eip = "\x6f\x9b\x04\x08"    #0x08049b6f  Return Address JMP EAX
```

## Eip Test

Verification of Control of EIP register

Adjust the filler to enable the overflow and the correct header for the specific overflow program

```python
filler = "A" * 1036
```
