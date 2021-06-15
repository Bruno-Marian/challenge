import os

import win32com.client as win32
"""utilize pip install pywin32 - nesta biblioteca você consegue utilizar a integração com outlook"""


def send_email(emailto, diretory, attachment):
    counting_zip = 1
    outlook = win32.Dispatch('outlook.application')
    email = outlook.CreateItem(0)
    for _ in range(10):
        path = os.path.abspath(f"{diretory}/zipfile{counting_zip}.zip")
        attachment = f'{path}'
        email.Attachments.Add(attachment)
        counting_zip += 1

    email.To = emailto
    email.Subject = "Resultado do teste"
    if attachment:
        email.HTMLBody = f"""<p>Envido dos arquivos com sucesso</p>"""
    else:
        email.HTMLBody = f"""<p>Email enviado porem ouve falha nos arquivos</p>"""

    email.Send()
