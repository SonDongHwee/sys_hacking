from pwn import *

context.arch = "amd64"

asmcode = shellcraft.execve("/bin/sh",0,0)
shellcode = asm(asmcode)
print(shellcode)
