class CatalogPage:
    column_items_links = "//div[@class='list-group']/a"
    column_items_banner = "//div[@class='swiper-viewport']"

    class RefineSearch:
        type_of_item = "//h3/following-sibling::*/div[@class='col-sm-3']//li"
        list_view_button = "//button[@id='list-view']"
        grid_view_button = "//button[@id='grid-view']"
        compare_link = "//a[@id='compare-total']"
        sort_by_select = "//select[@id='input-sort']"
        sort_by_select_option_name_z_a = "//select[@id='input-sort']/option[3]"
        input_limit = "//select[@id='input-limit']"
        input_limit_option = "//select[@id='input-limit']/option"
