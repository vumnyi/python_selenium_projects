class Admin:
    continue_button = "//*[text() = 'Continue']"
    button_back = "//*[text() = 'Back']"
    list_group_column_links = "//div[@class='list-group']/a"
    username_input = "//input[@name='username']"
    forgotten_password_link = "//a[text() = 'Forgotten Password']"
    firstname = "//input[@name='firstname']"
    lastname = "//input[@name='lastname']"
    email = "//input[@name='email']"
    telephone = "//input[@name='telephone']"
    password = "//input[@name='password']"
    password_confirm = "//input[@name='confirm']"
    subscribe_yes = "//*[text() = 'Subscribe']/following::*[@type='radio' and @value='1']"
    subscribe_no = "//*[text() = 'Subscribe']/following::*[@type='radio' and @value='0']"
    privacy_police_link = "//b[text() = 'Privacy Policy']/ancestor::a"
    privacy_police_checkbox = "//b[text() = 'Privacy Policy']/following::input[@type='checkbox']"

    class UserMenu:
        class RightMenu:
            def item(text):
                choose_item = "//*[@id='column-right']//a[contains (., '%s')]" % text
                return choose_item

        class PaymentForm:
            it = "//*[@id='payment-new']"

    class Account:
        h2 = "//h2"

    class AdminNavigation:
        def sections(name):
            return "//li/a[contains (., '%s')]" % name

        def sections_item(item_name):
            return "//li/a[contains (., '%s')]" % item_name

    class AdminButtonsEditItem:
        add_new = "//*[@data-original-title='Add New']"
        save_button = "//*[@data-original-title='Save']"
        cancel_button = "//*[@data-original-title='Cancel']"
        edit_button = "//*[@data-original-title='Edit']"
        delete_button = "//*[@data-original-title='Delete']"

    class AdminFilter:
        product_name_input = "//*[@id='input-name']"
        model_name_input = "//*[@id='input-model']"
        price_input = "//*[@id='input-price']"
        quantity_input = "//*[@id='input-quantity']"
        status_select = "//*[@id='input-status']"
        filter_button = "//*[@id='button-filter']"

    class ProductList:
        product_names = "//td[@class='text-left'][1]"
        product_models = "//td[@class='text-left'][2]"

        def current_product_check_box(product_name):
            return "//td[contains (., '%s')]/parent::*//input[@type='checkbox']" % product_name

    class AddProduct:
        def topics(topics_name):
            return "//*[@class='nav nav-tabs']//a[contains (., '%s')]" % topics_name

        class General:
            product_name_input = "//*[@id='input-name1']"
            meta_tag_title = "//*[@id='input-meta-title1']"

        class Data:
            model_input = "//*[@id='input-model']"
            price_input = "//*[@id='input-price']"
            quantity_input = "//*[@id='input-quantity']"
