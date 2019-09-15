class Catalog:
    column_items_links = {"xpath": "//div[@class='list-group']/a"}
    column_items_banner = {"xpath": "//div[@class='swiper-viewport']"}

    class RefineSearch:
        type_of_item = {"xpath": "//h3/following-sibling::*/div[@class='col-sm-3']//li"}
        list_view_button = {"xpath": "//button[@id='list-view']"}
        grid_view_button = {"xpath": "//button[@id='grid-view']"}
        compare_link = {"xpath": "//a[@id='compare-total']"}
        sort_by_select = {"xpath": "//select[@id='input-sort']"}
        sort_by_select_option_name_z_a = {"xpath": "//select[@id='input-sort']/option[3]"}
        sort_by_select_option_name_low_high = {"xpath": "//select[@id='input-sort']/option[4]"}
        input_limit = {"xpath": "//select[@id='input-limit']"}
        input_limit_option = {"xpath": "//select[@id='input-limit']/option"}
