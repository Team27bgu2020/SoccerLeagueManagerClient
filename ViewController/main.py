from PyQt5.QtWidgets import QApplication, QMainWindow
from ViewController import ViewController
from Client import Client
import sys


def main():
    server_address = ('localhost', 10000)

    app = QApplication(sys.argv)
    controller = ViewController(Client(server_address))
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()