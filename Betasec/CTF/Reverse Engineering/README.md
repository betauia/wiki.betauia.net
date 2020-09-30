# Reverse Engineering

Reverse engineering or "rev" is the art of analyzing a binary or code, understanding what it does and in some way replicating or running the code to find the flag.

### Div.

command line tool: gdb
examples:
```disassemble function1
break *0x080484bb
r
info registers
command line tool: objdump
objdump -d FILE```

Easy command-line tools to see some of the code being executed as you follow through a binary:
```ltrace and strace
ltrace BINARY```

ser systemcalls

##### Other tools
java
jd-gui
ghidra
pwntools
apktool
android
ILSpry
.net
radare