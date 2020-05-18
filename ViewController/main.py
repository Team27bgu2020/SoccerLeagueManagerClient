from PyQt5.QtWidgets import QApplication, QMainWindow
from ViewController import ViewController
import sys


def main():
    app = QApplication(sys.argv)
    controller = ViewController()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()