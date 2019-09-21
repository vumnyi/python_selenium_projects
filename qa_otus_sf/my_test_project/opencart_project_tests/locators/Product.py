class Product:
    breadcrumbs = {"xpath": "//ul[@class='breadcrumb']/li"}

    # description = {"xpath": "//a[text() = 'Description']"}
    # specification = {"xpath": "//a[text() = 'Specification']"}
    # reviews = {"xpath": "//a[contains (text(), 'Reviews')]"}

    def choose_product_tab(tab_name):
        # return {"xpath": "//a[contains (text(), '%s')]" % tab_name}
        return {"xpath": "//a[contains (text(), '{}')]".format(tab_name)}

    # review
    write_review_textarea = {"xpath": "//textarea[@name='text']"}
    write_review_name = {"xpath": "//input[@name='name']"}

    def choose_review_rating(rating):
        # return {"xpath": "//input[@name='rating' and @value='%s']" % rating}
        return {"xpath": "//input[@name='rating' and @value='{}']".format(rating)}

    write_review_button_continue = {"xpath": "//button[@id='button-review']"}
    # product_options_div
    product_options_div = {"xpath": "//div[@id='content']//div[@class='col-sm-4']"}
    product_options_div_add_to_wish_list = {
        "xpath": product_options_div["xpath"] + "//button[@data-original-title = 'Add to Wish List']"}
    product_options_div_compare = {
        "xpath": product_options_div["xpath"] + "//button[@data-original-title = 'Compare this Product']"}
    product_options_brand_link = {"xpath": product_options_div["xpath"] + "//li[text() = 'Brand: ']/a"}
    product_options_div_h1 = {"xpath": "//div[@id='content']//div[@class='col-sm-4']/h1"}
    product_options_div_h2_price = {"xpath": "//div[@id='content']//div[@class='col-sm-4']//h2"}
    # product_options_div_available_options
    available_options_radio_input = {"xpath": product_options_div["xpath"] + "//div[@class='radio']"}
    available_options_checkbox_input = {"xpath": product_options_div["xpath"] + "//div[@class='checkbox']//input"}
    available_options_text_input = {
        "xpath": product_options_div["xpath"] + "//label[text() = 'Text']/following-sibling::input"}
    available_options_select_dropdown = {"xpath": product_options_div["xpath"] + "//select"}
    available_options_select_dropdown_option = {"xpath": product_options_div["xpath"] + "//select/option"}
    available_options_textarea = {"xpath": product_options_div["xpath"] + "//textarea"}
    available_options_upload_file_button = {"xpath": product_options_div["xpath"] + "//button[text() = ' Upload File']"}
    available_options_date_input = {
        "xpath": product_options_div["xpath"] + "//label[text() = 'Date']/following-sibling::div/input"}
    available_options_time_input = {
        "xpath": product_options_div["xpath"] + "//label[text() = 'Time']/following-sibling::div/input"}
    available_options_date_time_input = {
        "xpath": product_options_div["xpath"] + "//label[text() = 'Date & Time']/following-sibling::div/input"}
    available_options_qty_input = {
        "xpath": product_options_div["xpath"] + "//label[text() = 'Qty']/following::input[@id='input-quantity']"}
    available_options_add_to_cart_button = {"xpath": product_options_div["xpath"] + "//button[@id='button-cart']"}
    # available_options_add_to_cart_button = product_options_div["xpath"] + "//button[@id='button-cart']"
    available_options_reviews_link = {"xpath": product_options_div["xpath"] + "//a[contains (text(), 'reviews')]"}
    available_options_write_review_link = {"xpath": product_options_div["xpath"] + "//a[contains (text(), 'Write')]"}
    # social_media_buttons
    available_options_facebook = {
        "xpath": product_options_div["xpath"] + "//a[@class ='addthis_button_facebook_like at300b']"}
    available_options_twitter = {"xpath": product_options_div["xpath"] + "//a[@class ='addthis_button_tweet at300b']"}
    available_options_share = {"xpath": product_options_div["xpath"] + "//a[@class ='atc_s addthis_button_compact']"}

    class Images:
        main_image = {"xpath": "//ul[@class='thumbnails']/li[1]"}
        additional_images = {"xpath": "//li[@class='image-additional']"}
        # wrap image gallery
        wrapper = {"xpath": "//*[@class='mfp-wrap mfp-gallery mfp-close-btn-in mfp-auto-cursor mfp-ready']"}
        wrap_image = {"xpath": wrapper["xpath"] + "//img"}
        wrap_image_close_button = {"xpath": wrapper["xpath"] + "//button[@title='Close (Esc)']"}
        wrap_image_previos_button = {"xpath": wrapper["xpath"] + "//button[@title='Previous (Left arrow key)']"}
        wrap_image_next_button = {"xpath": wrapper["xpath"] + "Next (Right arrow key)"}
