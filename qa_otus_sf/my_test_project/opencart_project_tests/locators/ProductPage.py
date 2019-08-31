class ProductPage:
    breadcrumbs = "//ul[@class='breadcrumb']/li"
    description = "//a[text() = 'Description']"
    specification = "//a[text() = 'Specification']"
    # review
    reviews = "//a[contains (text(), 'Reviews')]"
    write_review_textarea = "//textarea[@name='text']"
    write_review_rating = "//input[@name='rating']"
    write_review_button_continue = "//button[@id='button-review']"
    # product_options_div
    product_options_div = "//div[@id='content']//div[@class='col-sm-4']"
    product_options_div_add_to_wish_list = product_options_div + "//button[@data-original-title = 'Add to Wish List']"
    product_options_div_compare = product_options_div + "//button[@data-original-title = 'Compare this Product']"
    product_options_brand_link = product_options_div + "//li[text() = 'Brand: ']/a"
    product_options_div_h1 = "//div[@id='content']//div[@class='col-sm-4']/h1"
    product_options_div_h2_price = "//div[@id='content']//div[@class='col-sm-4']//h2"
    # product_options_div_available_options
    available_options_radio_input = product_options_div + "//div[@class='radio']"
    available_options_checkbox_input = product_options_div + "//div[@class='checkbox']//input"
    available_options_text_input = product_options_div + "//label[text() = 'Text']/following-sibling::input"
    available_options_select_dropdown = product_options_div + "//select"
    available_options_select_dropdown_option = product_options_div + "//select/option"
    available_options_textarea = product_options_div + "//textarea"
    available_options_upload_file_button = product_options_div + "//button[text() = ' Upload File']"
    available_options_date_input = product_options_div + "//label[text() = 'Date']/following-sibling::div/input"
    available_options_time_input = product_options_div + "//label[text() = 'Time']/following-sibling::div/input"
    available_options_date_time_input = product_options_div + "//label[text() = 'Date & Time']/following-sibling::div/input"
    available_options_qty_input = product_options_div + "//label[text() = 'Qty']/following::input[@id='input-quantity']"
    available_options_add_to_cart_button = product_options_div + "//button[@id='button-cart']"
    available_options_reviews_link = product_options_div + "//a[contains (text(), 'reviews')]"
    available_options_write_review_link = product_options_div + "//a[contains (text(), 'Write')]"
    # social_media_buttons
    available_options_facebook = product_options_div + "//a[@class ='addthis_button_facebook_like at300b']"
    available_options_twitter = product_options_div + "//a[@class ='addthis_button_tweet at300b']"
    available_options_share = product_options_div + "//a[@class ='atc_s addthis_button_compact']"

    class Images:
        main_image = "//ul[@class='thumbnails']/li[1]"
        additional_images = "//li[@class='image-additional']"
        # wrap image gallery
        wrapper = "//*[@class='mfp-wrap mfp-gallery mfp-close-btn-in mfp-auto-cursor mfp-ready']"
        wrap_image = wrapper + "//img"
        wrap_image_close_button = wrapper + "//button[@title='Close (Esc)']"
        wrap_image_previos_button = wrapper + "//button[@title='Previous (Left arrow key)']"
        wrap_image_next_button = wrapper + "Next (Right arrow key)"

    class Alert:
        success = "//div[contains(@class, 'alert-success')]"
