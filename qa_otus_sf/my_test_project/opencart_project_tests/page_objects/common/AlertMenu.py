from locators import Common
from ..BasePage import BasePage


class AlertDialog(BasePage):

    def click_login(self):
        self._click(Common.Alert.Success.link_to_login)

    def click_to_cart(self):
        self._click(Common.Alert.Success.link_to_cart)

    def click_create_account(self):
        self._click(Common.Alert.Success.link_to_create_account)

    def click_link_product(self):
        self._click(Common.Alert.Success.link_to_product)

    def click_to_wish_list(self):
        self._click(Common.Alert.Success.link_to_wish_list)
