from unittest import TestCase as TestCase
from PyQt5.QtWidgets import QApplication, QMainWindow
from ViewController.ViewController import ViewController
from ViewController.Client import Client
import sys

from View.UnionRepresentor import UnionRepresentorWindow


class TestUCs(TestCase):

    def test_login(self):
        server_address = ('localhost', 10000)
        app = QApplication(sys.argv)
        controller = ViewController(Client(server_address))
        controller.show_login()

        self.assertTrue(controller.log_reg_win.isVisible())
        print(controller.log_reg_win.isActiveWindow())
        controller.log_reg_win.set_username('asd')
        controller.log_reg_win.set_password('asd')
        controller.log_reg_win.click_login()

        self.assertTrue(controller.msg.isVisible())
        controller.close_popup()
        self.assertFalse(controller.msg.isVisible())
        self.assertTrue(controller.log_reg_win.isVisible())

        controller.log_reg_win.set_username('dor')
        controller.log_reg_win.set_password('1234')
        controller.log_reg_win.click_login()
        self.assertTrue(controller.user_win.isVisible())
        self.assertFalse(controller.log_reg_win.isVisible())

    def test_create_policies(self):
        server_address = ('localhost', 10000)
        app = QApplication(sys.argv)
        controller = ViewController(Client(server_address))
        controller.user_win = UnionRepresentorWindow(controller)
        controller.show_user_win()
        sys.exit(app.exec_())


