import string
import random
import os
import datetime

import pywintypes
import win32com.client as win32 # utilize pip install pywin32 - nesta biblioteca você consegue utilizar a integração com outlook

# ascii_uppercase - retorna letras maiúscula
# digits - retorna os numeros
from time import sleep
from zipfile import ZipFile

data = datetime.datetime.today()
diretorynow = f'./{data.year}/{data.month}/{data.day}/{data.hour}/{data.minute}'


def random_generator4kbs(size=4000, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_files(size=100, counting_create=1):
    for _ in range(size):
        file = open(f"file{counting_create.__str__().zfill(3)}.txt", "w")
        file.write(random_generator4kbs())
        file.close()
        counting_create += 1


def create_zip(diretory, counting_zipfiles=1, counting_read=1):
    if not os.path.isdir(diretory):
        os.makedirs(diretory)
    for _ in range(10):
        with ZipFile(f'{diretory}/zipfile{counting_zipfiles}.zip', "w") as newzip:
            for _ in range(10):
                newzip.write(f"file{counting_read.__str__().zfill(3)}.txt")
                counting_read += 1
            counting_zipfiles += 1


def send_email(emailto, senddiretory):
    global attachment
    counting_zip = 1
    outlook = win32.Dispatch('outlook.application')
    email = outlook.CreateItem(0)
    for _ in range(10):
        path = os.path.abspath(f"{senddiretory}/zipfile{counting_zip}.zip")
        attachment = f'{path}'
        email.Attachments.Add(attachment)
        counting_zip += 1

    email.To = emailto
    email.Subject = "Resultado do teste"
    if attachment:
        email.HTMLBody = f"""<p>Teste concluido com sucesso</p>"""
    else:
        email.HTMLBody = f"""<p>Teste foi concluido com falhas</p>"""

    email.Send()


def delete_files(counting_delete=1):
    for _ in range(100):
        os.remove(f"file{counting_delete.__str__().zfill(3)}.txt")
        counting_delete += 1


def main():
    try:
        create_files()
        create_zip(diretory=diretorynow)
        send_email(emailto=input('Escreva seu email = '), senddiretory=diretorynow)
        delete_files()
    except pywintypes.com_error:
        print('\n Você digitou um e-mail incorreto, tente novamente')
        main()


if __name__ == '__main__':
    main()


