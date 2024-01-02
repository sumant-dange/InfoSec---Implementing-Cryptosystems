import aes
from Crypto import Random
from Crypto.Cipher import AES

BLOCK_SIZE = AES.block_size

key="989"
print(str(iv = Random.new().read(BLOCK_SIZE)))
print(str(iv = Random.new().read(BLOCK_SIZE)))