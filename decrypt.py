import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == 'amt.py' or file == 'key.key' or file == 'decrypt.py':
        continue
    if os.path.isfile(file):
        files.append(file)


print(files)

#key = Fernet.generate_key()
key = None
with open('key.key', 'rb') as f:
    key = f.read()

for file in files:
    with open(file, 'rb') as f:
        content = f.read()
    content_decrypted = Fernet(key).decrypt(content)
    with open(file, 'wb') as f:
        f.write(content_decrypted)

