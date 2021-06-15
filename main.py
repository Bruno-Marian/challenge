from win32com.universal import com_error

from Services import svFiles
from Services import svEmail
from Services import svDiretory


def main():
    directory = svDiretory.get_diretory()
    try:
        svFiles.create_files(new_file=input('Infome o nome que deseja para o arquivo: '))
        svFiles.create_zip(diretory=svDiretory.get_diretory())
        svEmail.send_email(emailto=input('Escreva seu email = '), diretory=directory)
        svFiles.delete_files()
        print('Programa finalizado com sucesso!!')
    except com_error:
        print('\n Você digitou um e-mail incorreto, tente novamente')
        main()
    except Exception as ex:
        print(f"Ocorreu um erro no sistema :{ex!r}")
        main()


if __name__ == '__main__':
    main()
