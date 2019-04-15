import mysql.connector


class ConnectionFactory:
    def getconnection(self):
        try:
            con = mysql.connector.connect(
                host="localhost",
                port="3306",
                user="root",
                passwd="root",
                database="contatodb"
            )
        except:
            print('Não foi possível realizar a conexão.')
        finally:
            return con

    def closeconnection(self, con):
        con.close
