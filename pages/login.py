from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("")

    def login(self, username="demouser", password="abc123"):
        self.navigate()
        self.page.locator("input[name=\"username\"]").type(username)
        self.page.locator("input[name=\"password\"]").type(password)
        self.page.get_by_role("button", name="Login").click()
