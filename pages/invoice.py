from playwright.sync_api import Page, expect


class InvoicePage:
    def __init__(self, page: Page):
        self.page = page

    def choose_first_invoice(self):
        with self.page.expect_popup() as popup_info:
            self.page.get_by_role("link", name="Invoice Details").first.click()
        invoice_details_page = popup_info.value
        expect(invoice_details_page.get_by_role("heading", name="Invoice Details")).to_be_visible()
        return invoice_details_page
