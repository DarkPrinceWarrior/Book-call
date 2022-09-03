from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):

    def __init__(self):
        self.show_password = None
        self.remember_me = None
        self.cancel = None
        self.register = None
        self.signin = None
        self.password = None
        self.login = None
        self.label_app_name = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 400)
        MainWindow.setStyleSheet("background-color: #22222e")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_app_name = QtWidgets.QLabel(self.centralwidget)
        self.label_app_name.setGeometry(QtCore.QRect(50, 20, 600, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_app_name.setFont(font)
        self.label_app_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_app_name.setStyleSheet("background-color: #FFFFE0")
        self.label_app_name.setObjectName("label")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(90, 90, 400, 31))
        self.login.setStyleSheet("background-color: #FFFFFF")
        self.login.setObjectName("lineEdit")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(90, 130, 400, 31))
        self.password.setStyleSheet("background-color: #FFFFFF")
        self.password.setObjectName("lineEdit_2")
        self.signin = QtWidgets.QPushButton(self.centralwidget)
        self.signin.setGeometry(QtCore.QRect(100, 180, 75, 23))
        self.signin.setStyleSheet("background-color: green")
        self.signin.setObjectName("pushButton")
        self.register = QtWidgets.QPushButton(self.centralwidget)
        self.register.setGeometry(QtCore.QRect(200, 180, 100, 23))
        self.register.setStyleSheet("background-color: grey")
        self.register.setObjectName("pushButton_2")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(350, 180, 75, 23))
        self.cancel.setStyleSheet("background-color: red")
        self.cancel.setObjectName("pushButton_3")
        self.remember_me = QtWidgets.QCheckBox(self.centralwidget)
        self.remember_me.setGeometry(QtCore.QRect(200, 220, 170, 21))
        self.remember_me.setStyleSheet("background-color: white")
        self.remember_me.setObjectName("checkBox")
        self.show_password = QtWidgets.QCheckBox(self.centralwidget)
        self.show_password.setGeometry(QtCore.QRect(200, 260, 170, 21))
        self.show_password.setStyleSheet("background-color: white")
        self.show_password.setObjectName("checkBox_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_app_name.setText(_translate("MainWindow", "Телефонная книга"))
        self.signin.setText(_translate("MainWindow", "Войти"))
        self.register.setText(_translate("MainWindow", "Регистрация"))
        self.cancel.setText(_translate("MainWindow", "Отмена"))
        self.remember_me.setText(_translate("MainWindow", "Запомнить меня"))
        self.show_password.setText(_translate("MainWindow", "Показать пароль"))


class Book_call(QtWidgets.QMainWindow):
    def __init__(self):
        super(Book_call, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Телефонная книга')
        self.ui.login.setPlaceholderText('имя пользователя')
        self.ui.password.setPlaceholderText('пароль')
        self.ui.signin.clicked.connect(self.show_inf)


    def show_inf(self):
        print(self.ui.login.text())
        print(self.ui.password.text())
