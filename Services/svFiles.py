import os
import random
import string
from zipfile import ZipFile

file = 'file'


def random_generator4kbs(size=4000, chars=string.ascii_uppercase + string.digits):
    """
        ascii_uppercase - retorna letras maiúscula
        digits - retorna os numeros
    """
    return ''.join(random.choice(chars) for _ in range(size))


def create_files(size=100, counting_create=1, new_file='file'):
    global file
    file = new_file
    for _ in range(size):
        files = open(f"{file}{counting_create.__str__().zfill(3)}.txt", "w")
        files.write(random_generator4kbs())
        files.close()
        counting_create += 1


def create_zip(diretory, counting_zipfiles=1, counting_read=1):
    global file
    if not os.path.isdir(diretory):
        os.makedirs(diretory)
    for _ in range(10):
        with ZipFile(f'{diretory}/zipfile{counting_zipfiles}.zip', "w") as newzip:
            for _ in range(10):
                newzip.write(f"{file}{counting_read.__str__().zfill(3)}.txt")
                counting_read += 1
            counting_zipfiles += 1


def delete_files(counting_delete=1):
    global file
    for _ in range(100):
        os.remove(f"{file}{counting_delete.__str__().zfill(3)}.txt")
        counting_delete += 1
