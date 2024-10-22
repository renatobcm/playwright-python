import pytest
from playwright.sync_api import Page, expect


def test_page_has_title(login_page, page: Page):
    login_page.navigate()
    # expect Page to contain title "Login"
    expect(page.get_by_role("heading", name="Login")).to_be_visible


def test_valid_login(login_page, page: Page):
    # login with valid credentials
    login_page.login()
    # validate that invoice list is visible
    expect(page.get_by_role("heading", name="Invoice List")).to_be_visible()


# the data table iteration #4 has valid credentials and will be omitted
@pytest.mark.parametrize(("username", "password"), [("Demouser_", "abc123"), ("demouser_", "xyz"), ("demouser", "nananana")])
def test_invalid_login(login_page, page: Page, username, password):
    # try to login with invalid credentials
    login_page.login(username, password)
    # validating if error message is visible and has the proper css color property
    expect(page.get_by_text("Wrong username or password.")).to_be_visible()
    expect(page.get_by_text("Wrong username or password.")
           ).to_have_css("color", "rgb(114, 28, 36)")


@pytest.mark.parametrize(
    "invoice_data",
    [
        {
            "hotelName": "Rendezvous Hotel",
            "invoiceDate": "14/01/2018",
            "dueDate": "15/01/2018",
            "invoiceNumber": "110",
            "bookingCode": "0875",
            "customerDetailsName": "JOHNY SMITH",
            "customerDetailsAddress": "R2, AVENUE DU MAROC",
            "customerDetailsZipCode": "123456",
            "room": "Superior Double",
            "checkIn": "14/01/2018",
            "checkOut": "15/01/2018",
            "totalStayCount": "1",
            "totalStayAmount": "$150",
            "depositNow": "USD $20.90",
            "taxVat": "USD $19",
            "totalAmount": "USD $209",
        },
    ]
)
def test_invalid_login(login_page,invoice_list_page: Page, invoice_data):
    # login
    login_page.login()
    
    invoice_details_page = invoice_list_page.choose_first_invoice()
    # performing validations
    expect(invoice_details_page.get_by_role("heading", name=invoice_data["hotelName"])).to_be_visible()
    expect(invoice_details_page.get_by_role("heading", name=f"Invoice #{invoice_data['invoiceNumber']}")).to_be_visible()
    expect(invoice_details_page.get_by_text(f"Invoice Date: {invoice_data['invoiceDate']}")).to_be_visible()
    expect(invoice_details_page.get_by_text(f"Due Date: {invoice_data['dueDate']}")).to_be_visible()
    expect(invoice_details_page.get_by_role("cell", name=invoice_data['bookingCode'])).to_be_visible()
    expect(invoice_details_page.get_by_role("cell", name=invoice_data['room'])).to_be_visible()
    expect(invoice_details_page.get_by_role("cell", name=invoice_data['totalStayCount'], exact=True)).to_be_visible()
    expect(invoice_details_page.get_by_role("cell", name=invoice_data['totalStayAmount'])).to_be_visible()
    expect(invoice_details_page.get_by_role("cell", name=invoice_data['checkIn'])).to_be_visible()
    expect(invoice_details_page.get_by_role("cell", name=invoice_data['checkOut'])).to_be_visible()
    expect(invoice_details_page.get_by_text(f"{invoice_data['customerDetailsName']}")).to_be_visible()
    expect(invoice_details_page.get_by_text(f"{invoice_data['customerDetailsAddress']}")).to_be_visible()
    expect(invoice_details_page.get_by_text(f"{invoice_data['customerDetailsZipCode']}")).to_be_visible()
    expect(invoice_details_page.get_by_role("table").nth(1).get_by_role("cell", name=invoice_data['depositNow'])).to_be_visible()
    expect(invoice_details_page.get_by_role("table").nth(1).get_by_role("cell", name=invoice_data['taxVat'])).to_be_visible()
    expect(invoice_details_page.get_by_role("table").nth(1).get_by_role("cell", name=invoice_data['totalAmount'])).to_be_visible()

