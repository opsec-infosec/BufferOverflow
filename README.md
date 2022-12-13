# BufferOverflow
***Buffer Overflow Python Scripts***

*Copyright (C) 2022  Dale Furneaux (opinfosec)*
*Released under GNU GPL v2*

This runs on Linux


## A word of caution
The server.c is exploitable and containes a buffer overflow.  Please don't run the program on any public facing machine.  I should not have to say this, but you never know what some people might do!!  I use this repo for teaching others about the importance of preventing exploitable code.  If you have participated in the presentation and you enjoyed it, please star this repo and let others know about its existence.

## OS Protections
Don't forget to turn of ASLR if running on linux, this will temporarily disable ASLR.  Don't do this on a production server please!!!

```
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
```

## Python Scripts

Don't forget to change the IP address of the server

```python
s.connect(("172.16.110.135", 1337))
```

## Logical progression of a buffer overflow exploit
The logical progression of tests should be:

1. fuzzer (fuzz)
2. test for bad characters
3. pattern to determine the EIP offset
4. confirm the EIP with eip-test
5. ExPlOiT

## Fuzzer

Python3 Fuzzer to enable a buffer overflow

## Pattern Generator

Finds the correct offset of the EIP register which is used to load the EIP register with our JMP instruction.

## Bad Character Generator for Python3

Just a badcharacter generator to copy and paste into your bad character python script

## Test for bad character

This sends every bad character in a buffer overflow, which should be checked in the dugger to make sure they all arrive.  If the program doesn't crash or some characters don't appear, then we need to exclude them (bad characters) when we generate our payload

## Eip Test

Verification of the Control of EIP register

Adjust the filler to enable the overflow, the EIP offset is taken from the Pattern Generator offset.

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
The NOP sled is used to allow variables to be place on the stack without overwriting the payload.  NOP stands for no-operation... the execution by the CPU does not change the state of the CPU, esentially executing a NULL statement.

## Server (server.c)

This is our fantastic C program, with excellent quality and lots of testing prior to the long holiday weekend.  Because the offices will be closed over the weekend, we had to rush and deploy the server on 50 machines to minimize any disruptions over the weekend.  The Quality, IT and Testing departments said it was good to go, and it was easy to test...

We came back into the office on Monday, and all 50 of our servers were hacked... not to mention our internal network, voip, databases, and a few of our clients.  One of my developer friends took a look at the code and said to me "I hope you didn't deploy that sofware on any internet facing machines."..  I of course said No, with a nervous smile.

I have spent hours looking for the problem, but I can't see any.  The server recieves only 100 Bytes from our client application, so there is no way it will crash.  Can you spot the problem?

To make the server executable (which runs on linux), use the attached make file and execute:

```sh
make clean && make all
```

Then use a debugger such as Olly or edb to run the server executable and test out the python scripts.


\<opsecinfosec\> @  42-AbuDhabi
