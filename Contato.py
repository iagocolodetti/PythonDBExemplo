class Contato:
    def __init__(self, id = None, nome = None, telefone = None, email = None):
        self.__id = id
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email

    def setid(self, id):
        self.__id = id

    def getid(self):
        return self.__id

    def setnome(self, nome):
        self.__nome = nome

    def getnome(self):
        return self.__nome

    def settelefone(self, telefone):
        self.__telefone = telefone

    def gettelefone(self):
        return self.__telefone

    def setemail(self, email):
        self.__email = email

    def getemail(self):
        return self.__email
