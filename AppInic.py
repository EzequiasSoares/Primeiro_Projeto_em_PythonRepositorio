# Área de importações do projeto
from PyQt5 import uic, QtWidgets
# Fim área de importações


def start():
    if:
        primeira_tela.avisotc.setText("Ola mundo")
print("Funcionou")

app = QtWidgets.QApplication([])
primeira_tela = uic.loadUi("Login1.ui")
primeira_tela.ButtonLogin.clicked.connect(start)

primeira_tela.show()
