from PyQt5 import QtWidgets

from app.controllers import selectAll
from app.models import db_setup
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from app.ui_templates.templates import Ui_MainWindow


def main():
    db_setup.init_db()
    # Show all users
    print('All users')
    selectAll()


def app_gui():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    app_gui()
