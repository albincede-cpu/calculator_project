from playwright.sync_api import Page
from test.web.pages.page_base import PageBase


class Methods_page(PageBase):
    def __init__(self, page: Page) -> None:
        super().__init__(page, 
        elements={            
            "key-add": "#key-add",
            "key-2": "#key-2",
            "key-equals": "#key-equals",
            "key-multiply": "#key-multiply",
            "key-subtract": "#key-subtract",
            "key-divide": "#key-divide",
            "key-clear": "#key-clear",
            "calculator-screen": "#calculator-screen",
            "username":  "#username",
            "password": "#password",
            "login": "#login",
        })

    def methods(self, username="admin", password="test1234"):
        self.element("username").fill(username)
        self.element("password").fill(password)
        self.element("login").click()

        self.element("key-2").click()
        self.element("key-add").click()
        self.element("key-2").click()
        self.element("key-equals").click()

        self.element("key-2").click()
        self.element("key-subtract").click()
        self.element("key-2").click()
        self.element("key-equals").click()

        self.element("key-2").click()
        self.element("key-multiply").click()
        self.element("key-2").click()
        self.element("key-equals").click()

        self.element("key-2").click()
        self.element("key-divide").click()
        self.element("key-2").click()
        self.element("key-equals").click()
        
