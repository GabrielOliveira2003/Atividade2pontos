from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from moduloCadastrar import inserir
from converterData import converterData

class TelaPrincipal(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        carregador = QUiLoader()
        self.tela = carregador.load("Tela.ui")
        self.componentes()
    
    def componentes(self):
        self.caixaCliente = self.tela.findChild(QtWidgets.QLineEdit, "caixaCliente")
        self.caixaDataViagem = self.tela.findChild(QtWidgets.QDateEdit, "caixaDataViagem")
        self.caixaLocalOrigem = self.tela.findChild(QtWidgets.QComboBox, "caixaLocalOrigem")
        self.caixaLocalDestino = self.tela.findChild(QtWidgets.QComboBox, "caixaLocalDestino")
        self.caixaFormaPagamento = self.tela.findChild(QtWidgets.QComboBox, "caixaFormaPagamento")
        self.btnCadastrar = self.tela.findChild(QtWidgets.QPushButton, "btnCadastrar")
        self.btnCadastrar.clicked.connect(self.cadastrarDados)
        

    def cadastrarDados(self):
        clnt = self.caixaCliente.text()
        data = self.caixaDataViagem.text()
        origm = self.caixaLocalOrigem.currentText()
        dstn = self.caixaLocalDestino.currentText()
        formpgm = self.caixaFormaPagamento.currentText()
        inserir(clnt, converterData(data), origm, dstn, formpgm)
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    interface = TelaPrincipal()
    interface.tela.show()
    app.exec()