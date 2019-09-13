from locators import Common, Admin
from .BasePage import BasePage


class UserPage(BasePage):

    def login_user(self, email, password):
        self._input(Common.email_input, email)
        self._input(Common.password_input, password)
        self._click(Common.login_button)

    def my_account_dropdown(self, dropdown_item):
        self._click(Common.Header.my_account)
        self._click(Common.Header.my_account_dropdown(dropdown_item))

    def open_right_menu_item(self, item_name):
        self._click(Admin.UserMenu.RightMenu.item(item_name))

    def verify_payment_form(self):
        self._wait_for_visible(Admin.UserMenu.PaymentForm.it)

    def verify_product(self, name):
        self._wait_for_visible(name, link_text=True)

