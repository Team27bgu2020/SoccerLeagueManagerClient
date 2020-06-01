from unittest import TestCase as TestCase
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ViewController.ViewController import ViewController
from ViewController.Client import Client
import sys

from View.UnionRepresentor import UnionRepresentorWindow
from View.TeamOwner import TeamOwnerWindow
from View.Referee import RefereeWindow


class TestUCs(TestCase):

    def test_login(self):
        """ test - login UC """
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
        """ test - create new policies UC """
        server_address = ('localhost', 10000)
        app = QApplication(sys.argv)
        controller = ViewController(Client(server_address))
        controller.user_id = 'dor'
        controller.user_win = UnionRepresentorWindow(controller)
        controller.show_user_win()
        self.assertTrue(controller.user_win.isVisible())
        # test - create new points policy UC
        controller.user_win.display_policies()
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

    def test_create_team(self):
        """ test - create new team UC """
        server_address = ('localhost', 10000)
        app = QApplication(sys.argv)
        controller = ViewController(Client(server_address))
        controller.user_id = 'dor'
        controller.user_win = TeamOwnerWindow(controller)
        controller.show_user_win()

        # test - create new team
        self.assertTrue(controller.user_win.isVisible())
        controller.user_win.open_team()
        controller.user_win.set_team_name('Barcelona')
        controller.user_win.click_create_team()
        self.assertTrue(controller.msg.isVisible())
        self.assertTrue(controller.msg.icon() == QMessageBox.Information)
        controller.close_popup()
        # test - Error when trying to create a team with a duplicate names
        self.assertTrue(controller.user_win.isVisible())
        controller.user_win.open_team()
        controller.user_win.set_team_name('Barcelona')
        controller.user_win.click_create_team()
        self.assertTrue(controller.msg.isVisible())
        self.assertTrue(controller.msg.icon() == QMessageBox.Critical)
        controller.close_popup()
        controller.user_win.close_open_team_dialog()

    def test_manage_game(self):
        """ test - manage game UC """
        server_address = ('localhost', 10000)
        app = QApplication(sys.argv)
        controller = ViewController(Client(server_address))
        controller.user_id = 'oscar'
        controller.user_win = RefereeWindow(controller)
        controller.show_user_win()

        # test - create new game event
        self.assertTrue(controller.user_win.isVisible())
        controller.user_win.click_create_game_event()
        self.assertTrue(controller.msg.isVisible())
        self.assertTrue(controller.msg.icon() == QMessageBox.Information)
        controller.close_popup()
        # test - edit new game event
        controller.user_win.edit_game_event(0, 0, 0, 'update', 12)
        controller.user_win.click_edit_game_event()
        self.assertTrue(controller.msg.icon() == QMessageBox.Information)
        controller.close_popup()





