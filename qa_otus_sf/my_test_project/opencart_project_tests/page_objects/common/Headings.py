from locators import Common
from ..BasePage import BasePage


class Headings(BasePage):

    def get_h1_text(self, index):
        return self._get_element_text(Common.h1_text, index)
