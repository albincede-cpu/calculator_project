from playwright.sync_api import Page
from test.web.pages.page_base import PageBase
from playwright.sync_api import expect
class RegisterPage(PageBase):
    def __init__(self, page: Page) -> None:
        super().__init__(page, 
        elements={            
            "username": "#username",
            "register": "#register",
            "password1": "#password1",
            "password2": "#password2",
            "logout-button": "#logout-button",
            "user-name": "#user-name",


        })

    def register(self, username, password1, password2):
        self.element("register").click()
        self.element("username").fill(username)
        self.element("password1").fill(password1)
        self.element("password2").fill(password2)
        self.element("register").click()
        expect(self.element("user-name")).to_have_text("albin")

        self.element("logout-button").click()        