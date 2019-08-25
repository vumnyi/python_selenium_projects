class CommonLocators:
    nav_links = "//ul[@class='nav navbar-nav']/li"
    input_search = "//*[@name='search']"
    search_button = "//*[@id='search']//button"
    shopping_cart = "//*[@id='cart']"
    shopping_cart_total = shopping_cart + "//span[@id='cart-total']"
    product_item = "//*[@class='product-thumb']"
    product_item_image = product_item + "//img"
    product_item_caption = product_item + "/div[@class='caption']"
    product_item_caption_link = product_item_caption + "//a"
    caption_button_group = "//*[@class='button-group']"
    caption_button_group_add_to_cart = caption_button_group + "/button[contains (., 'Add to Cart')]"
    caption_button_group_add_to_wish_list = caption_button_group + "/button[@data-original-title = 'Add to Wish List']"
    caption_button_group_add_compare = caption_button_group + "/button[@data-original-title = 'Compare this Product']"

    class Header:
        currency = "//span[contains (., 'Currency')]"
        currency_euro = currency + "/following::*/*[contains (text(), 'Euro')]"
        currency_pound_sterling = currency + "/following::*/*[contains (text(), 'Sterling')]"
        currency_dollar = currency + "/following::*/*[contains (text(), 'Dollar')]"
        my_account = "//span[contains (., 'My Account')]"
        my_account_register = my_account + "/following::li/a[text() = 'Register']"
        my_account_login = my_account + "/following::li/a[text() = 'Login']"
        wish_list = "//span[contains (., 'Wish List')]"
        shopping_cart = "//span[contains (., 'Shopping Cart')]"
        checkout = "//span[contains (., 'Checkout')]"

    class Footer:
        # Information
        about_us = "//li[contains (., 'About Us')]"
        delivery_information = "//li[contains (., 'Delivery Information')]"
        privacy_policy = "//li[contains (., 'Privacy Policy')]"
        terms_conditions = "//li[contains (., 'Terms & Conditions')]"
        # Customer Service
        contact_us = "//li[contains (., 'Contact Us')]"
        returns = "//li[contains (., 'Returns')]"
        site_map = "//li[contains (., 'Site Map')]"
        # Extras
        brands = "//li[contains (., 'Brands')]"
        gift_certificates = "//li[contains (., 'Gift Certificates')]"
        affilate = "//li[contains (., 'Affiliate')]"
        specials = "//li[contains (., 'Specials')]"
        # My Account
        my_account = "//div[@class='col-sm-3']//li[contains (., 'My Account')]"
        order_history = "//li[contains (., 'Order History')]"
        wish_list = "//div[@class='col-sm-3']//li[contains (., 'Wish List')]"
        newsletter = "//li[contains (., 'Newsletter')]"
