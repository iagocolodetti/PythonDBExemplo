from ConnectionFactory import *
from Contato import *

class ContatoDAO:
    def __init__(self):
        self.__cf = ConnectionFactory()

    def add(self, contato):
        try:
            con = self.__cf.getconnection()
            if con.is_connected():
                cursor = con.cursor()
                cursor.execute("INSERT INTO contato(nome, telefone, email) VALUES(%s, %s, %s)", (contato.getnome(), contato.gettelefone(), contato.getemail()))
                con.commit()
                if cursor.rowcount > 0:
                    print('Contato adicionado.')
                else:
                    print('Contato não adicionado.')
        except:
            print('Não foi possível adicionar o contato.')
            con.rollback()
        finally:
            self.__cf.closeconnection(con)

    def getcontato(self, id):
        try:
            con = self.__cf.getconnection()
            if con.is_connected():
                cursor = con.cursor()
                cursor.execute("SELECT * FROM contato WHERE id = %s", (id,))
                result = cursor.fetchone()
                if result is not None:
                    contato = Contato(result[0], result[1], result[2], result[3])
                    return contato
                else:
                    print('Não existe contato com esse ID.')
        except:
            print('Não foi possível buscar o contato.')
        finally:
            self.__cf.closeconnection(con)

    def getcontatospornome(self, nome):
        try:
            con = self.__cf.getconnection()
            if con.is_connected():
                cursor = con.cursor()
                cursor.execute("SELECT * FROM contato WHERE nome LIKE %s", ('%' + nome + '%',))
                result = cursor.fetchall()
                length = len(result)
                if length > 0:
                    contatos = []
                    for i in range(length):
                        contatos.append(Contato(result[i][0], result[i][1], result[i][2], result[i][3]))
                    return contatos;
                else:
                    print('Não existem contatos com esse nome ou parte dele.')
        except:
            print('Não foi possível buscar os contatos.')
        finally:
            self.__cf.closeconnection(con)

    def getcontatosportelefone(self, telefone):
        try:
            con = self.__cf.getconnection()
            if con.is_connected():
                cursor = con.cursor()
                cursor.execute("SELECT * FROM contato WHERE telefone LIKE %s", ('%' + telefone + '%',))
                result = cursor.fetchall()
                length = len(result)
                if length > 0:
                    contatos = []
                    for i in range(length):
                        contatos.append(Contato(result[i][0], result[i][1], result[i][2], result[i][3]))
                    return contatos;
                else:
                    print('Não existem contatos com esse telefone ou parte dele.')
        except:
            print('Não foi possível buscar os contatos.')
        finally:
            self.__cf.closeconnection(con)

    def getcontatosporemail(self, email):
        try:
            con = self.__cf.getconnection()
            if con.is_connected():
                cursor = con.cursor()
                cursor.execute("SELECT * FROM contato WHERE email LIKE %s", ('%' + email + '%',))
                result = cursor.fetchall()
                length = len(result)
                if length > 0:
                    contatos = []
                    for i in range(length):
                        contatos.append(Contato(result[i][0], result[i][1], result[i][2], result[i][3]))
                    return contatos;
                else:
                    print('Não existem contatos com esse email ou parte dele.')
        except:
            print('Não foi possível buscar os contatos.')
        finally:
            self.__cf.closeconnection(con)

    def getcontatos(self):
        try:
            con = self.__cf.getconnection()
            if con.is_connected():
                cursor = con.cursor()
                cursor.execute("SELECT * FROM contato")
                result = cursor.fetchall()
                length = len(result)
                if len(result) > 0:
                    contatos = []
                    for i in range(length):
                        contatos.append(Contato(result[i][0], result[i][1], result[i][2], result[i][3]))
                    return contatos;
                else:
                    print('Não existem contatos.')
        except:
            print('Não foi possível buscar os contatos.')
        finally:
            self.__cf.closeconnection(con)

    def update(self, contato):
        try:
            con = self.__cf.getconnection()
            if con.is_connected():
                cursor = con.cursor()
                cursor.execute("UPDATE contato SET nome = %s, telefone = %s, email = %s WHERE id = %s", (contato.getnome(), contato.gettelefone(), contato.getemail(), contato.getid()))
                con.commit()
                if cursor.rowcount > 0:
                    print('Contato alterado com sucesso.')
                else:
                    print('Não existe contato com esse ID.')
        except:
            print('Não foi possível alterar/atualizar o contato.')
        finally:
            self.__cf.closeconnection(con)

    def delete(self, id):
        try:
            con = self.__cf.getconnection()
            if con.is_connected():
                cursor = con.cursor()
                cursor.execute("DELETE FROM contato WHERE id = %s", (id,))
                con.commit()
                if cursor.rowcount > 0:
                    print('Contato deletado com sucesso.')
                else:
                    print('Não existe contato com esse ID.')
        except:
            print('Não foi possível excluir/remover o contato.')
        finally:
            self.__cf.closeconnection(con)
