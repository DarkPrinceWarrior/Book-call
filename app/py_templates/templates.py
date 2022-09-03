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
        MainWindow.resize(430, 397)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: #22222e")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(93, 166, 200)")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_app_name = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_app_name.setFont(font)
        self.label_app_name.setStyleSheet("background-color: #FFFFE0")
        self.label_app_name.setObjectName("label_app_name")
        self.verticalLayout.addWidget(self.label_app_name)
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setStyleSheet("background-color: #FFFFFF")
        self.login.setInputMask("")
        self.login.setText("")
        self.login.setObjectName("login")
        self.verticalLayout.addWidget(self.login)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setStyleSheet("background-color: #FFFFFF")
        self.password.setInputMask("")
        self.password.setText("")
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.signin = QtWidgets.QPushButton(self.centralwidget)
        self.signin.setStyleSheet("background-color: green")
        self.signin.setObjectName("signin")
        self.horizontalLayout.addWidget(self.signin)
        self.register_2 = QtWidgets.QPushButton(self.centralwidget)
        self.register_2.setStyleSheet("background-color: grey")
        self.register_2.setObjectName("register_2")
        self.horizontalLayout.addWidget(self.register_2)
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setStyleSheet("background-color: red")
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.show_password = QtWidgets.QCheckBox(self.centralwidget)
        self.show_password.setStyleSheet("background-color: white")
        self.show_password.setObjectName("show_password")
        self.verticalLayout.addWidget(self.show_password)
        self.remember_me = QtWidgets.QCheckBox(self.centralwidget)
        self.remember_me.setStyleSheet("background-color: white")
        self.remember_me.setObjectName("remember_me")
        self.verticalLayout.addWidget(self.remember_me)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setStyleSheet("background-color: #FFFFE0")
        icon = QtGui.QIcon.fromTheme("свсвс")
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.verticalLayout.addWidget(self.commandLinkButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_app_name.setText(_translate("MainWindow", "Телефонная книга"))
        self.signin.setText(_translate("MainWindow", "Войти"))
        self.register_2.setText(_translate("MainWindow", "Регистрация"))
        self.cancel.setText(_translate("MainWindow", "Отмена"))
        self.show_password.setText(_translate("MainWindow", "Показать пароль"))
        self.remember_me.setText(_translate("MainWindow", "Запомнить меня"))
        self.commandLinkButton.setText(_translate("MainWindow", "Забыли пароль"))


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
        self.ui.signin.clicked.connect(self.login_app)
        self.ui.cancel.clicked.connect(self.logout_app)

    def logout_app(self):
        self.ui.login.setText("")
        self.ui.password.setText("")

    def login_app(self):
        print(self.ui.login.text())
        print(self.ui.password.text())
