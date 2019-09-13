class Common:
    email_input = {"xpath": "//input[@name='email']"}
    password_input = {"xpath": "//input[@name='password']"}
    button_submit = {"xpath": "//*[@type='submit']"}
    login_button = {"xpath": "//input[@value='Login']"}
    nav_links = {"xpath": "//ul[@class='nav navbar-nav']/li"}
    input_search = {"xpath": "//*[@name='search']"}
    search_button = {"xpath": "//*[@id='search']//button"}
    shopping_cart = {"xpath": "//*[@id='cart']"}
    shopping_cart_total = {"xpath": shopping_cart["xpath"] + "//span[@id='cart-total']"}
    product_item = {"xpath": "//*[@class='product-thumb']"}
    product_item_image = {"xpath": product_item["xpath"] + "//img"}
    product_item_caption = {"xpath": product_item["xpath"] + "/div[@class='caption']"}
    product_item_caption_link = {"xpath": product_item_caption["xpath"] + "//a"}
    caption_button_group = {"xpath": "//*[@class='button-group']"}
    caption_button_group_add_to_cart = {"xpath": caption_button_group["xpath"] + "/button[contains (., 'Add to Cart')]"}
    caption_button_group_add_to_wish_list = {
        "xpath": caption_button_group["xpath"] + "/button[@data-original-title = 'Add to Wish List']"}
    caption_button_group_add_compare = {
        "xpath": caption_button_group["xpath"] + "/button[@data-original-title = 'Compare this Product']"}

    class Header:
        currency = {"xpath": "//span[contains (., 'Currency')]"}
        currency_euro = {"xpath": currency["xpath"] + "/following::*/*[contains (text(), 'Euro')]"}
        currency_pound_sterling = {"xpath": currency["xpath"] + "/following::*/*[contains (text(), 'Sterling')]"}
        currency_dollar = {"xpath": currency["xpath"] + "/following::*/*[contains (text(), 'Dollar')]"}
        my_account = {"xpath": "//span[contains (., 'My Account')]"}
        my_account_register = {"xpath": my_account["xpath"] + "/following::li/a[text() = 'Register']"}
        my_account_login = {"xpath": my_account["xpath"] + "/following::li/a[text() = 'Login']"}
        wish_list = {"xpath": "//span[contains (., 'Wish List')]"}
        shopping_cart = {"xpath": "//span[contains (., 'Shopping Cart')]"}
        checkout = {"xpath": "//span[contains (., 'Checkout')]"}

        def my_account_dropdown(item):
            dropdown_item = {"xpath": "//span[contains (., 'My Account')]/following::ul//a[contains (., '%s')]" % item}
            return dropdown_item

    class Footer:
        # Information
        about_us = {"xpath": "//li[contains (., 'About Us')]"}
        delivery_information = {"xpath": "//li[contains (., 'Delivery Information')]"}
        privacy_policy = {"xpath": "//li[contains (., 'Privacy Policy')]"}
        terms_conditions = {"xpath": "//li[contains (., 'Terms & Conditions')]"}
        # Customer Service
        contact_us = {"xpath": "//li[contains (., 'Contact Us')]"}
        returns = {"xpath": "//li[contains (., 'Returns')]"}
        site_map = {"xpath": "//li[contains (., 'Site Map')]"}
        # Extras
        brands = {"xpath": "//li[contains (., 'Brands')]"}
        gift_certificates = {"xpath": "//li[contains (., 'Gift Certificates')]"}
        affilate = {"xpath": "//li[contains (., 'Affiliate')]"}
        specials = {"xpath": "//li[contains (., 'Specials')]"}
        # My Account
        my_account = {"xpath": "//div[@class='col-sm-3']//li[contains (., 'My Account')]"}
        order_history = {"xpath": "//li[contains (., 'Order History')]"}
        wish_list = {"xpath": "//div[@class='col-sm-3']//li[contains (., 'Wish List')]"}
        newsletter = {"xpath": "//li[contains (., 'Newsletter')]"}

    class Alert:
        class Success:
            it = {"xpath": "//div[contains(@class, 'alert-success')]"}
            link_to_login = {"xpath": it["xpath"] + "/a[contains(@href, 'login')]"}
            link_to_create_account = {"xpath": it["xpath"] + "/a[contains(@href, 'register')]"}
            link_to_product = {"xpath": it["xpath"] + "/a[contains(@href, 'product')]"}
            link_to_wishlist = {"xpath": it["xpath"] + "/a[contains(@href, 'wishlist')]"}
            link_to_cart = {"xpath": it["xpath"] + "/a[contains(@href, 'cart')]"}
