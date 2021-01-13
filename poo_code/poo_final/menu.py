


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_alugue_mais(object):
    def setupUi(self, alugue_mais):
        alugue_mais.setObjectName("alugue_mais")
        alugue_mais.resize(851, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(alugue_mais.sizePolicy().hasHeightForWidth())
        alugue_mais.setSizePolicy(sizePolicy)
        alugue_mais.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.centralwidget = QtWidgets.QWidget(alugue_mais)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_veiculos = QtWidgets.QPushButton(self.centralwidget)
        self.bt_veiculos.setGeometry(QtCore.QRect(150, 200, 521, 41))
        self.bt_veiculos.setObjectName("bt_veiculos")
        self.bt_clientes = QtWidgets.QPushButton(self.centralwidget)
        self.bt_clientes.setGeometry(QtCore.QRect(150, 290, 521, 41))
        self.bt_clientes.setObjectName("bt_clientes")
        self.bt_relatorio = QtWidgets.QPushButton(self.centralwidget)
        self.bt_relatorio.setGeometry(QtCore.QRect(150, 390, 521, 41))
        self.bt_relatorio.setObjectName("bt_relatorio")
        self.bt_sair = QtWidgets.QPushButton(self.centralwidget)
        self.bt_sair.setGeometry(QtCore.QRect(580, 520, 191, 41))
        self.bt_sair.setObjectName("bt_sair")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 60, 551, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        alugue_mais.setCentralWidget(self.centralwidget)

        self.retranslateUi(alugue_mais)
        QtCore.QMetaObject.connectSlotsByName(alugue_mais)

    def retranslateUi(self, alugue_mais):
        _translate = QtCore.QCoreApplication.translate
        alugue_mais.setWindowTitle(_translate("alugue_mais", "MainWindow"))
        self.bt_veiculos.setText(_translate("alugue_mais", "VEICULOS"))
        self.bt_clientes.setText(_translate("alugue_mais", "CLIENTES"))
        self.bt_relatorio.setText(_translate("alugue_mais", "ALUGUEIS / RELATORIOS"))
        self.bt_sair.setText(_translate("alugue_mais", "SAIR"))
        self.label.setText(_translate("alugue_mais", "GRUPO VIAGE MAIS+"))
