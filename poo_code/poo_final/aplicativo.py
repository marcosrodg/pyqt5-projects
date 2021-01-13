from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from poo_final.menu import *
from poo_final.carros import *
from poo_final.aluguel import *
from poo_final.cliente import *
from poo_final.banco import *
from datetime import datetime


class Carros(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.con = conecta()
        self.cursor = self.con.cursor()

        self.bt_cadaastro_car.clicked.connect(self.add)
        self.bt_editar_car.clicked.connect(self.edit)
        self.bt_del_car.clicked.connect(self.exc)
        self.pushButton_4.clicked.connect(self.sair)

    def add(self):
        try:
            self.query = 'insert into Carros values(%s,%s,%s);'
            if self.con:
                self.cursor.execute(self.query,(self.ln_placa.text(),self.ln_modelo.text(),self.ln_descricao.text()))
                self.con.commit()
                self.label_2.setText('VEICULO CADASTRADO')
            else:
                self.label_2.setText('CONEXÃO FALHOU')
        except:
            self.label_2.setText('PLACA JA CADASTRADA')
        self.ln_placa.setText('')
        self.ln_modelo.setText('')
        self.ln_descricao.setText('')

    def edit(self):
        try:
            if self.con:
                self.query1 = 'UPDATE Carros SET placa = %s, modelo = %s, descricao = %s WHERE placa = %s'
                self.cursor.execute(self.query1,(self.ln_placa.text(),self.ln_modelo.text(),self.ln_descricao.text(),self.ln_placa.text()))
                self.con.commit()
                self.label_2.setText('EDIÇÃO SALVA')

            else:
                self.label_2.setText('CONEXÃO FALHOU')
        except:
            self.label_2.setText('VEICULO NAO ENCONTRADO')
        self.ln_placa.setText('')
        self.ln_modelo.setText('')
        self.ln_descricao.setText('')

    def exc(self):
        try:
            if self.con:
                self.query2='DELETE FROM Carros WHERE placa = %s'
                self.cursor.execute(self.query2,(self.ln_placa.text()))
                self.con.commit()
                self.label_2.setText('VEICULO EXCLUIDO')

            else:
                self.label_2.setText('CONEXÃO FALHOU')
        except:
            self.label_2.setText('VEICULO NAO ENCONTRADO')
        self.ln_placa.setText('')
        self.ln_modelo.setText('')
        self.ln_descricao.setText('')

    def sair(self):
        self.root = App()
        self.root.show()
        Carros.hide(self)


class Aluguel(QMainWindow, Ui_relatorios):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.con = conecta()
        self.cursor = self.con.cursor()

        self.bt_exc_aluguel.clicked.connect(self.excl)
        self.bt_inserir_aluguel.clicked.connect(self.inser)
        self.bt_imprimir_relatorio.clicked.connect(self.imprim)
        self.bt_sair_relatorio.clicked.connect(self.sair)

    def excl(self):
        try:
            if self.con:
                self.query6='DELETE FROM Aluguel WHERE cpfcliente = %s'
                self.cursor.execute(self.query6,(self.ln_cpf_aluguel.text()))
                self.con.commit()
                self.label_2.setText('ALUGUEL EXCLUIDO')

            else:
                self.label_2.setText('CONEXÃO FALHOU')
        except:
            self.label_2.setText('ERRO:NAO ENCONTRADO')
        self.ln_cpf_aluguel.setText('')
        self.ln_placa_aluguel.setText('')

    def inser(self):
        try:
            self.query5 = 'insert into Aluguel values(%s,%s,%s,%s)'
            if self.con:
                self.cursor.execute(self.query5,(self.bt_pagamento.currentText(),datetime.now(),self.ln_cpf_aluguel.text(),self.ln_placa_aluguel.text()))
                self.con.commit()
                self.label_2.setText('ALUGUEL CADASTRADO')
            else:
                self.label_2.setText('CONEXÃO FALHOU')
        except:
            self.label_2.setText('ERRO AO CADASTRAR')
        self.ln_cpf_aluguel.setText('')
        self.ln_placa_aluguel.setText('')

    def imprim(self):
        if self.ln_pesquisa.text() != '':
            try:
                self.query8 = 'select * from Aluguel WHERE cpfcliente = %s'
                self.cursor.execute(self.query8,self.ln_pesquisa.text())
                self.linha = self.cursor.fetchone()[:]
                self.lb_resultado.setText(f'Forma de pagamento: {self.linha[0]}\nData\Horario da locação: {self.linha[1]}'
                                          f'\nCPF locador: {self.linha[2]}\nPlaca do veiculo: {self.linha[3]}')
                self.con.commit()
            except TypeError:
                self.lb_resultado.setText('NENHUM CLIENTE COM ESSE CPF FOI LOCALIZADO!')
        else:
            self.lb_resultado.setText('PREENCHA O CAMPO CPF PARA PROCURAR')


    def sair(self):
        self.root = App()
        self.root.show()
        Aluguel.hide(self)


class Clientes(QMainWindow, Ui_cadastro_cliente):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.con = conecta()
        self.cursor = self.con.cursor()

        self.bt_add_cliente.clicked.connect(self.add)
        self.bt_edt_cliente.clicked.connect(self.edt)
        self.bt_del_cliente.clicked.connect(self.dele)
        self.bt_voltar_cliente.clicked.connect(self.sair)

    def add(self):
        try:
            self.query = 'insert into Clientes values(%s,%s);'
            if self.con:
                self.cursor.execute(self.query, (self.ln_cpf_cliente.text(), self.ln_name_cliente.text()))
                self.con.commit()
                self.lb_retorno.setText('CLIENTE foi  CADASTRADO')
            else:
                self.lb_retorno.setText('CONEXÃO FALHOU')
        except:
            self.lb_retorno.setText('ERRO AO CADASTRAR')
        self.ln_cpf_cliente.setText('')
        self.ln_name_cliente.setText('')

    def edt(self):
        try:
            if self.con:
                self.query1 = 'UPDATE Clientes SET cpf = %s, nome = %s WHERE cpf = %s'
                self.cursor.execute(self.query1,(self.ln_cpf_cliente.text(),self.ln_name_cliente.text(),self.ln_cpf_cliente.text()))
                self.con.commit()
                self.lb_retorno.setText('EDIÇÃO SALVA')

            else:
                self.lb_retorno.setText('CONEXÃO FALHOU')
        except:
            self.lb_retorno.setText('CLIENTE NAO ENCONTRADO')
        self.ln_cpf_cliente.setText('')
        self.ln_name_cliente.setText('')

    def dele(self):
        try:
            if self.con:
                self.query3 = 'DELETE FROM Clientes WHERE cpf = %s'
                self.cursor.execute(self.query3, (self.ln_cpf_cliente.text()))
                self.con.commit()
                self.lb_retorno.setText('CLIENTE EXCLUIDO')

            else:
                self.lb_retorno.setText('CONEXÃO FALHOU')
        except:
            self.lb_retorno.setText('CLIENTE NAO ENCONTRADO')
        self.ln_cpf_cliente.setText('')
        self.ln_name_cliente.setText('')

    def sair(self):
        self.root = App()
        self.root.show()
        Clientes.hide(self)


class App(QMainWindow, Ui_alugue_mais):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.bt_veiculos.clicked.connect(self.open_veiculos)
        self.bt_clientes.clicked.connect(self.open_clientes)
        self.bt_relatorio.clicked.connect(self.open_aluguel)
        self.bt_sair.clicked.connect(self.menu_sair)

    def open_veiculos(self):
        self.tela_carros = Carros()
        self.tela_carros.show()
        App.hide(self)

    def open_clientes(self):
        self.tela_clientes = Clientes()
        self.tela_clientes.show()
        App.hide(self)

    def open_aluguel(self):
        self.tela_aluguel= Aluguel()
        self.tela_aluguel.show()
        App.hide(self)

    def menu_sair(self):
        App.close(self)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
