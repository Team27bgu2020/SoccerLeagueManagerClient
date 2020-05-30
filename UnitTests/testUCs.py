from unittest import TestCase as TestCase
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
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
        controller.user_id = 'dor'
        controller.user_win = UnionRepresentorWindow(controller)
        controller.show_user_win()
        self.assertTrue(controller.user_win.isVisible())
        # test - create new points policy UC
        controller.user_win.showPolicies()
        controller.user_win.set_points_policy(10, 0, 10)
        controller.user_win.save_points_policy()
        self.assertTrue(controller.msg.isVisible())
        self.assertTrue(controller.msg.icon() == QMessageBox.Information)
        controller.close_popup()
        self.assertTrue(controller.user_win.isVisible())
        # test - Error for creating duplicated policies
        controller.user_win.save_points_policy()
        self.assertTrue(controller.msg.isVisible())
        self.assertTrue(controller.msg.icon() == QMessageBox.Critical)
        controller.close_popup()

        # test - creating new game policy
        controller.user_win.set_game_policy(2, 2, 1)
        controller.user_win.save_game_policy()
        self.assertTrue(controller.msg.isVisible())
        self.assertTrue(controller.msg.icon() == QMessageBox.Information)
        controller.close_popup()
        # test - Error for creating duplicated policies
        controller.user_win.save_game_policy()
        self.assertTrue(controller.msg.isVisible())
        self.assertTrue(controller.msg.icon() == QMessageBox.Critical)
        controller.close_popup()

        # test - creating new team budget policy
        controller.user_win.set_budget_policy(1000)
        controller.user_win.save_budget_policy()
        self.assertTrue(controller.msg.isVisible())
        self.assertTrue(controller.msg.icon() == QMessageBox.Information)
        controller.close_popup()
        # test - Error for creating duplicated policies
        controller.user_win.save_budget_policy()
        self.assertTrue(controller.msg.isVisible())
        self.assertTrue(controller.msg.icon() == QMessageBox.Critical)
        controller.close_popup()





