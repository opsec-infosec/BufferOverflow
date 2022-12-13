# BufferOverflow
Buffer Overflow Python Scripts
Copyright (C) 2022  Dale Furneaux (opinfosec)
Released under GNU GPL v2

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


## Fuzzer

Python3 Fuzzer to enable a buffer overflow

## Pattern Generator

Finds the correct offset of the EIP register which is used to load the EIP register with our JMP instruction.

## Bad Character Generator for Python3

Just a badcharacter generator to copy and paste into your bad character python script

## Test for bad character

This sends every bad character in a buffer overflow, which should be checked in the dugger to make sure they all arrive.  If the program doesn't crash or some characters don't appear, then we need to exclude them (bad characters) when we generate our payload

## Eip Test

Verification of Control of EIP register

Adjust the filler to enable the overflow and the correct header for the specific overflow program

```python
filler = "A" * 1036
```

## BoF Exploit local and reverse shell

Simple BoF Exploit for server

Let the fun begin!!!

Don't forget to update the payload_shell with your own msfvenom generated reverse shell payload

Adjust the filler buffer to enable the overflow, adjust the eip address (JMP EAX)

Change the payload reference for the extend to caclulate the correct end of the buffer after your payload (this is not necessary, however it keeps the original BoF intact)

```python
filler = "A" * (1036 - ((len(nop_sled)) + len(payload_shell)))  # Filler 1036 Bytes - nop sled - size of payload
eip = "\x6f\x9b\x04\x08"    #0x08049b6f  Return Address JMP EAX
```

## Server (server.c)

This is our fantastic C program, with excellent quality and lots of testing prior to the long holiday weekend.  Because the offices will be closed over the weekend, we had to rush and deploy the server on 50 machines to minimize any disruptions over the weekend.  The Quality, IT and Testing departments said it was good to go, and it was easy to test...

We came back into the office on Monday, and all 50 of our servers were hacked... not to mention our internal network, voip, databases, and a few of our clients.  One of my developer friends took a look at the code and said to me "I hope you didn't deploy that sofware on any internet facing machines."..  I of course said No, with a nervous smile.

I have spent hours looking for the problem, but I can't see any.  The server recieves only 100 Bytes from our client application, so there is no way it will crash.  Can you spot the problem?

To make the server executable (which runs on linux), use the attached make file and execute:

```sh
make clean && make all
```

Then use a debugger such as Olly or edb to run the server executable and test our the python scripts.  The logical progression of tests should be the

1. fuzzer (fuzz)
2. test for bad characters
3. pattern to determine the EIP offset
4. confirm the EIP with eip-test
5. ExPlOiT
