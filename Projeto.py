#Primeiro projeto em python repositorio
from PyQt5 import uic,QtWidgets
import mysql.connector
from mysql.connector import connect

connect = mysql.connector.connect (
    host = "localhost",
    user= "root",
    passwd="",
    database = "Cadastro"
)
def Fazer_login():   
    login.label.setText ()
    Usuario = login.User.text ("")
    Senha = login.Senha.text()
    if Usuario == "eze" and Senha == "123":        
        db_info = connect.get_server_info()
        print ("Conectado com sucesso a verção {}, do MYSQL.".format (db_info))
        cursor = connect.cursor()
        cursor.execute ("select database();")
        linha = cursor.fetchone()
        print ("Conectado à {}.".format (linha))
    else:
        print ("Login incorreto!")


app=QtWidgets.QApplication([]) 
login = uic.loadUi("Login1.ui")
login.ButtonLogin.clicked.connect(connect)
login.show()
app.exec()