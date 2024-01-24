from Crypto.Cipher import DES
import binascii
from tqdm import tqdm

encrypted_flag = binascii.unhexlify("cfa30fafd13cf67b5f53cfa04013126f6a763bdb8f284a6631af16634c3fb4dcfbf6bf65b1e9dbfc")
#since the flag will be hexlified at the end of source code

def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()

plaintext=pad(binascii.unhexlify("12345678").decode()) #input needs to be unhexlified, decoded, and padded (as the input in source code)
ciphertext=binascii.unhexlify("23fb1cccd8c47a04") #same reason as "encrypted flag"

encodes={}
decodes={}
for key in tqdm(range(999999),desc="brute forcing keys"):
    key=pad(f'{key:06}')
    DESkey=DES.new(key,DES.MODE_ECB) #Key transformation(step 1)
    #key1
    enc_plain=DESkey.encrypt(plaintext)
    encodes[enc_plain]=key
    #key2
    dec_cipher=DESkey.decrypt(ciphertext)
    decodes[dec_cipher]=key

print("###finding intersection###")

encodes_texts=set(encodes.keys()) #set of "enc_plain"
decodes_texts=set(decodes.keys()) #set of "dec_cipher"



for same_inter_text in encodes_texts.intersection(decodes_texts):
    k1=encodes[same_inter_text] #k1=key
    k2=decodes[same_inter_text]
    print(k1,k2)
    break

DESkey1=DES.new(k1,DES.MODE_ECB)
DESkey2=DES.new(k2,DES.MODE_ECB)
inter_flag=DESkey2.decrypt(encrypted_flag)
flag=DESkey1.decrypt(inter_flag)
print(flag)
