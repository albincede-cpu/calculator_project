from playwright.sync_api import Page
from test.web.pages.page_base import PageBase

class HistoryPage(PageBase):
    def __init__(self, page: Page) -> None:
        super().__init__(page, 
        elements={            
            "username":  "#username",
            "password": "#password",
            "login": "#login",
            "toggle-button": "#toggle-button",
            "key-2": "#key-2",
            "key-add": "#key-add",
            "key-equals": "#key-equals",
            "logout-button": "#logout-button",
        })  



    def history(self, username="admin", password="test1234"):
        #LogIn
        self.element("username").fill(username)
        self.element("password").fill(password)
        self.element("login").click()
        #Addition
        self.element("key-2").click()
        self.element("key-add").click()
        self.element("key-2").click()
        self.element("key-equals").click()
        #History
        self.element("toggle-button").click()
        self.element("logout-button").click()        
        