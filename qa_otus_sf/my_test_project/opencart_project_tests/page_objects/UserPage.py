from locators import Common, Admin
from .BasePage import BasePage


class UserPage(BasePage):

    def login_user(self, email, password):
        self._input(Common.email_input, email)
        self._input(Common.password_input, password)
        self._click_ac(Common.login_button)
        return self

    def my_account_dropdown(self, dropdown_item):
        self._click_ac(Common.Header.my_account)
        self._click_ac(Common.Header.my_account_dropdown(dropdown_item))
        return self

    def open_right_menu_item(self, item_name):
        self._click_ac(Admin.UserMenu.RightMenu.item(item_name))
        return self

    def verify_payment_form(self):
        self._wait_for_visible(Admin.UserMenu.PaymentForm.it)
        return self

    def verify_product(self, name):
        self._wait_for_visible(name, link_text=True)
        return self

    def get_h2_text(self):
        return self._get_element_text(Admin.ClientAdminPage.Account.h2, 0)

    def input_field_name(self, field_name, value):
        if field_name == 'Password':
            self._input(Common.password_input, value)
        elif field_name == 'Confirm':
            self._input(Common.confirm_password_input, value)

    def click_button_continue(self):
        return self._click(Common.button_submit)

    def change_password(self, value):
        self._input(Common.password_input, value)
        self._input(Common.confirm_password_input, value)
        self._click(Common.button_submit)
        return self