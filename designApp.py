# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designApp.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 658)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BarraDeProgresso = QtWidgets.QProgressBar(self.centralwidget)
        self.BarraDeProgresso.setGeometry(QtCore.QRect(300, 590, 231, 23))
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.BarraDeProgresso.setFont(font)
        self.BarraDeProgresso.setProperty("value", 100)
        self.BarraDeProgresso.setObjectName("BarraDeProgresso")
        self.musicaSlider = QtWidgets.QSlider(self.centralwidget)
        self.musicaSlider.setGeometry(QtCore.QRect(700, 600, 211, 22))
        self.musicaSlider.setStyleSheet("QSlider {\n"
"    border: none; /* Remove a borda padrão do slider */\n"
"    background: #333; /* Cor de fundo escura */\n"
"    height: 10px; /* Altura do slider */\n"
"    border-radius: 10px; /* Borda arredondada */\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    background: #555; /* Cor da área da barra de música */\n"
"    border: 1px solid #666; /* Borda da área da barra de música */\n"
"    height: 10px; /* Altura da área da barra de música */\n"
"    border-radius: 5px; /* Borda arredondada */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #1E90FF; /* Cor da alça do slider (azul escuro) */\n"
"    border: 5px solid #1E90FF; /* Borda da alça do slider */\n"
"    width: 2px; /* Largura da alça do slider */\n"
"    height: 5px; /* Altura da alça do slider */\n"
"    border-radius: 10px; /* Borda arredondada da alça */\n"
"}")
        self.musicaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.musicaSlider.setObjectName("musicaSlider")
        self.botaoTocar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoTocar.setGeometry(QtCore.QRect(790, 555, 32, 32))
        self.botaoTocar.setAutoFillBackground(False)
        self.botaoTocar.setStyleSheet("QPushButton {\n"
"    color: white; \n"
"    border: none; \n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"}")
        self.botaoTocar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("reproduzir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botaoTocar.setIcon(icon)
        self.botaoTocar.setIconSize(QtCore.QSize(64, 64))
        self.botaoTocar.setObjectName("botaoTocar")
        self.botaoEscolher = QtWidgets.QPushButton(self.centralwidget)
        self.botaoEscolher.setGeometry(QtCore.QRect(120, 580, 91, 32))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.botaoEscolher.setFont(font)
        self.botaoEscolher.setStyleSheet("QPushButton {\n"
"    background-color: #1E90FF;\n"
"    color: white; \n"
"    border: none; \n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4169E1; \n"
"}")
        self.botaoEscolher.setObjectName("botaoEscolher")
        self.botaoBaixar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoBaixar.setGeometry(QtCore.QRect(10, 580, 96, 32))
        self.botaoBaixar.setMaximumSize(QtCore.QSize(16777215, 1600000))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.botaoBaixar.setFont(font)
        self.botaoBaixar.setStyleSheet("QPushButton {\n"
"    background-color: #1E90FF;\n"
"    color: white; \n"
"    border: none; \n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4169E1; \n"
"}")
        self.botaoBaixar.setObjectName("botaoBaixar")
        self.progressoLabel = QtWidgets.QLabel(self.centralwidget)
        self.progressoLabel.setGeometry(QtCore.QRect(350, 565, 101, 20))
        self.progressoLabel.setTextFormat(QtCore.Qt.AutoText)
        self.progressoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.progressoLabel.setObjectName("progressoLabel")
        self.botaoPular = QtWidgets.QPushButton(self.centralwidget)
        self.botaoPular.setGeometry(QtCore.QRect(830, 555, 31, 32))
        self.botaoPular.setStyleSheet("QPushButton {\n"
"    color: white; \n"
"    border: none; \n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"}")
        self.botaoPular.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("fim.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botaoPular.setIcon(icon1)
        self.botaoPular.setIconSize(QtCore.QSize(48, 48))
        self.botaoPular.setObjectName("botaoPular")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 40, 931, 511))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("QListWidget {\n"
"    background-color: #333; /* Dark background color */\n"
"    border: none; /* Remove the default border */\n"
"    padding: 10px; /* Internal padding for the list */\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    background: transparent;\n"
"    color: white; /* Text color in the list */\n"
"    padding: 5px; /* Internal padding for each item in the list */\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background: #1E90FF; /* Background color when an item is selected (dark blue) */\n"
"    color: white; /* Text color of the selected item */\n"
"    outline: none; /* Remove the focus outline */\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background: #666; /* Background color when the mouse hovers over an item */\n"
"}")
        self.listWidget.setObjectName("listWidget")
        self.botaoAnterior = QtWidgets.QPushButton(self.centralwidget)
        self.botaoAnterior.setGeometry(QtCore.QRect(750, 555, 31, 32))
        self.botaoAnterior.setStyleSheet("QPushButton {\n"
"    color: white; \n"
"    border: none; \n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"}")
        self.botaoAnterior.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("inicio.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botaoAnterior.setIcon(icon2)
        self.botaoAnterior.setIconSize(QtCore.QSize(48, 48))
        self.botaoAnterior.setObjectName("botaoAnterior")
        self.musicaTocando = QtWidgets.QLabel(self.centralwidget)
        self.musicaTocando.setGeometry(QtCore.QRect(10, 0, 911, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.musicaTocando.setFont(font)
        self.musicaTocando.setStyleSheet("")
        self.musicaTocando.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.musicaTocando.setObjectName("musicaTocando")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MP3 Player / Youtube Downloader"))
        self.botaoEscolher.setText(_translate("MainWindow", "Escolher"))
        self.botaoBaixar.setText(_translate("MainWindow", "Baixar"))
        self.progressoLabel.setText(_translate("MainWindow", "Progresso"))
        self.musicaTocando.setText(_translate("MainWindow", "Tocando: Nada"))
