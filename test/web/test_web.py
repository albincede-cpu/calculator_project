from test.web.test_base import WebBase
from test.web.pages.login_page import LoginPage
from test.web.pages.register_page import RegisterPage
from playwright.sync_api import expect
from test.web.pages.methods_page import Methods_page
from test.web.pages.history_page import HistoryPage
import pytest

class TestWeb(WebBase):
    def test_register(self):
        RegisterPage(self.page).register("albin", "cisco123", "cisco123")

    def test_login(self):
        LoginPage(self.page).login(username="admin", password="test1234")

    def test_method(self):
        Methods_page(self.page).methods()

    def test_history(self):
        #HistoryPage(self.page).history(username="username", password="password")
        HistoryPage(self.page).history()