from ContatoDAO import *

def main():
    while (True):
        print('..PythonDB Opções..')
        print('1 -> Adicionar')
        print('2 -> Buscar Por ID')
        print('3 -> Buscar Por Nome')
        print('4 -> Buscar Por Telefone')
        print('5 -> Buscar Por E-mail')
        print('6 -> Buscar Todos')
        print('7 -> Alterar')
        print('8 -> Deletar')
        print('0 -> Encerrar')
        opcao = lerint('Opção..: ')

        print()

        if opcao == 0:
            encerrar()
        elif opcao == 1:
            adicionar()
        elif opcao == 2:
            buscar()
        elif opcao == 3:
            buscarpornome()
        elif opcao == 4:
            buscarportelefone()
        elif opcao == 5:
            buscarporemail()
        elif opcao == 6:
            buscartodos()
        elif opcao == 7:
            alterar()
        elif opcao == 8:
            deletar()
        else:
            print('Opção Incorreta.')
            print()

def encerrar():
    print('Encerrado.')
    exit(0)

def adicionar():
    print('------------- [ADICIONAR] -------------')
    try:
        contato = Contato()
        contato.setnome(input('Nome: '))
        contato.settelefone(input('Telefone: '))
        contato.setemail(input('Email: '))
        cdao.add(contato)
    except Exception as e:
        print(e)
    print('----------------------------------------')

def buscar():
    print('------------ [BUSCAR (ID)] ------------')
    try:
        contato = cdao.getcontato(lerint('ID: '))
        if contato is not None:
            print('Contato: (ID: {}) {} | {} | {}'.format(contato.getid(), contato.getnome(), contato.gettelefone(), contato.getemail()))
    except Exception as e:
        print(e)
    print('----------------------------------------')

def buscarpornome():
    print('----------- [BUSCAR (NOME)] -----------')
    try:
        contatos = cdao.getcontatospornome(str(input('Nome: ')))
        if contatos is not None:
            for contato in contatos:
                print('Contato: (ID: {}) {} | {} | {}'.format(contato.getid(), contato.getnome(), contato.gettelefone(), contato.getemail()))
    except Exception as e:
        print(e)
    print('----------------------------------------')

def buscarportelefone():
    print('---------- [BUSCAR (TELEFONE)] ----------')
    try:
        contatos = cdao.getcontatosportelefone(str(input('Telefone: ')))
        if contatos is not None:
            for contato in contatos:
                print('Contato: (ID: {}) {} | {} | {}'.format(contato.getid(), contato.getnome(), contato.gettelefone(), contato.getemail()))
    except Exception as e:
        print(e)
    print('----------------------------------------')

def buscarporemail():
    print('---------- [BUSCAR (E-MAIL)] ----------')
    try:
        contatos = cdao.getcontatosporemail(str(input('Email: ')))
        if contatos is not None:
            for contato in contatos:
                print('Contato: (ID: {}) {} | {} | {}'.format(contato.getid(), contato.getnome(), contato.gettelefone(), contato.getemail()))
    except Exception as e:
        print(e)
    print('----------------------------------------')

def buscartodos():
    print('----------- [BUSCAR (TODOS)] -----------')
    try:
        contatos = cdao.getcontatos()
        if contatos is not None:
            for contato in contatos:
                print('Contato: (ID: {}) {} | {} | {}'.format(contato.getid(), contato.getnome(), contato.gettelefone(), contato.getemail()))
    except Exception as e:
        print(e)
    print('----------------------------------------')

def alterar():
    print('-------------- [ALTERAR] --------------')
    try:
        contato = Contato()
        contato.setid(lerint('ID: '))
        contato.setnome(input('Novo nome: '))
        contato.settelefone(input('Novo telefone: '))
        contato.setemail(input('Novo email: '))
        cdao.update(contato)
    except Exception as e:
        print(e)
    print('----------------------------------------')

def deletar():
    print('-------------- [DELETAR] --------------')
    try:
        cdao.delete(lerint('ID: '))
    except Exception as e:
        print(e)
    print('----------------------------------------')

def lerint(mensagem):
    try:
        i = int(input(mensagem))
    except:
        i = -1
    return i


cdao = ContatoDAO()
main()
