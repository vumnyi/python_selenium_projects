from locators import Catalog
from .BasePage import BasePage


class CatalogPage(BasePage):
    def change_sort(self, kind_of_sort):
        self._click(Catalog.RefineSearch.sort_by_select)
        if kind_of_sort == 'name_z_a':
            self._click(Catalog.RefineSearch.sort_by_select_option_name_z_a)
        elif kind_of_sort == 'name_low_high':
            self._click(Catalog.RefineSearch.sort_by_select_option_name_low_high)
        return self

