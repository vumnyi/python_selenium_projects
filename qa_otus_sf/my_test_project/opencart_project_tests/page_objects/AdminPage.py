from locators import Admin
from .BasePage import BasePage
import allure


class AdminPage(BasePage):

    def navigation_panel_click(self, section):
        with allure.step(f'Кликаю по секции {section}'):
            return self._click(Admin.AdminNavigation.sections(section))

    def section_item_click(self, item):
        return self._click(Admin.AdminNavigation.sections_items(item))

    def add_new_button_click(self):
        return self._click(Admin.AdminButtonsEditItem.add_new)

    def delete_button_click(self):
        return self._click(Admin.AdminButtonsEditItem.delete_button)

    def edit_button_click(self):
        return self._click(Admin.AdminButtonsEditItem.edit_button)

    def filter_button_click(self):
        return self._click(Admin.AdminFilter.filter_button)

    def save_product_button_click(self):
        return self._click(Admin.AdminButtonsEditItem.save_button)

    def product_topics_click(self, topic):
        with allure.step(f'Кликаю по заголовку {topic}'):
            return self._click(Admin.AddProduct.topics(topic))

    def product_list_checkbox_click(self, current_product):
        return self._click(Admin.ProductList.current_product_check_box(current_product))

    def product_inputs(self, input_name, text):
        with allure.step(f'Ввожу в инпут значение {text}'):
            return self._input(Admin.AddProduct.General.product_name_input(input_name), text)

    def filter_inputs(self, input_name, text):
        return self._input(Admin.AdminFilter.filter_input(input_name), text)

    def products_names_in_list(self):
        return self._text_elements(Admin.ProductList.product_names)

    def models_names_in_list(self):
        return self._text_elements(Admin.ProductList.product_models)
