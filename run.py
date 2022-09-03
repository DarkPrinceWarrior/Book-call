from PyQt5 import QtWidgets

from app.controllers import selectAll
from app.models import db_setup
import sys

from app.py_templates.templates import Book_call


def main():
    db_setup.init_db()
    # Show all users
    print('All users')
    selectAll()


def app_gui():
    app = QtWidgets.QApplication([])
    app.setStyle("Fusion")
    ui = Book_call()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    app_gui()
