from itertools import *
from Crypto.Cipher import DES
from tqdm import tqdm
import binascii
import string

string = '0123456789'
a = permutations(string,6)
ad = [''.join(permutation) for permutation in a]
ad = [''.join(i+'  ') for i in ad]
k = '0468eace57281a58'
flag = '4589f4a82a10890d8c29ae66dda239a9f08a53c96473260563a90ac80c9d9e4bb7bc33dd0faab521'

def double_decrypt(ciphertext,key1,key2):
    cipher2 = DES.new(key2, DES.MODE_ECB)
    decrypted_msg = cipher2.decrypt(binascii.unhexlify(ciphertext))

    cipher1 = DES.new(key1, DES.MODE_ECB)
    original_msg = cipher1.decrypt(decrypted_msg)

    return original_msg.decode('utf-8')

def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()

def find_keys(m):
    msg = pad(m)
    for key1 in tqdm(ad):
        cipher1 = DES.new(key1.encode('utf-8'), DES.MODE_ECB)
        enc_msg = cipher1.encrypt(msg)

key1,key2 = find_keys('12345678')
print(double_decrypt(flag,key1,key2))