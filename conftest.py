import pytest
from playwright.sync_api import Page
from pages.login import LoginPage
from pages.invoice import InvoicePage

@pytest.fixture(scope='session')
def base_url():
    return "https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/"

@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def invoice_list_page(page) -> InvoicePage:
    return InvoicePage(page)
