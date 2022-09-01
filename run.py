from app.controllers import selectAll
from app.models import db_setup
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def main():
    db_setup.init_db()
    # Show all users
    print('All users')
    selectAll()


def app_gui():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Hello")
    window.setGeometry(300, 250, 350, 200)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    app_gui()
