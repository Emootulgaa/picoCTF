# zaa eniig bol haltuurdsan2 chadku bolhoorn write up harchla

from pwn import *
import string

sh = remote("mercury.picoctf.net", 2431)

def oracle(text):
    sh.recvuntil("encrypted:")
    sh.sendline(text)
    sh.recvline()
    sh.recvline()
    return int(sh.recvline().decode())

known = "picoCTF{"

length = oracle(known)
print(known, end="")

current = ""
while current != "}":
    for c in string.printable:
        if oracle(known + c) == length:
            known += c
            current = c
            print(c, end="")
            break
