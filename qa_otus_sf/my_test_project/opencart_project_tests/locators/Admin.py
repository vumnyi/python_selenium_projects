class Admin:
    continue_button = {"xpath": "//*[text() = 'Continue']"}
    button_back = {"xpath": "//*[text() = 'Back']"}
    list_group_column_links = {"xpath": "//div[@class='list-group']/a"}
    username_input = {"xpath": "//input[@name='username']"}
    forgotten_password_link = {"xpath": "//a[text() = 'Forgotten Password']"}
    firstname = {"xpath": "//input[@name='firstname']"}
    lastname = {"xpath": "//input[@name='lastname']"}
    email = {"xpath": "//input[@name='email']"}
    telephone = {"xpath": "//input[@name='telephone']"}
    password = {"xpath": "//input[@name='password']"}
    password_confirm = {"xpath": "//input[@name='confirm']"}
    subscribe_yes = {"xpath": "//*[text() = 'Subscribe']/following::*[@type='radio' and @value='1']"}
    subscribe_no = {"xpath": "//*[text() = 'Subscribe']/following::*[@type='radio' and @value='0']"}
    privacy_police_link = {"xpath": "//b[text() = 'Privacy Policy']/ancestor::a"}
    privacy_police_checkbox = {"xpath": "//b[text() = 'Privacy Policy']/following::input[@type='checkbox']"}

    class UserMenu:
        class RightMenu:
            def item(text):
                choose_item = {"xpath": "//*[@id='column-right']//a[contains (., '%s')]" % text}
                return choose_item

        class PaymentForm:
            it = {"xpath": "//*[@id='payment-new']"}

    class Account:
        h2 = {"xpath": "//h2"}

    class AdminNavigation:
        def sections(name):
            return "//li/a[contains (., '%s')]" % name

        def sections_item(item_name):
            return "//li/a[contains (., '%s')]" % item_name

    class AdminButtonsEditItem:
        add_new = {"xpath": "//*[@data-original-title='Add New']"}
        save_button = {"xpath": "//*[@data-original-title='Save']"}
        cancel_button = {"xpath": "//*[@data-original-title='Cancel']"}
        edit_button = {"xpath": "//*[@data-original-title='Edit']"}
        delete_button = {"xpath": "//*[@data-original-title='Delete']"}

    class AdminFilter:
        product_name_input = {"xpath": "//*[@id='input-name']"}
        model_name_input = {"xpath": "//*[@id='input-model']"}
        price_input = {"xpath": "//*[@id='input-price']"}
        quantity_input = {"xpath": "//*[@id='input-quantity']"}
        status_select = {"xpath": "//*[@id='input-status']"}
        filter_button = {"xpath": "//*[@id='button-filter']"}

    class ProductList:
        product_names = {"xpath": "//td[@class='text-left'][1]"}
        product_models = {"xpath": "//td[@class='text-left'][2]"}

        def current_product_check_box(product_name):
            return "//td[contains (., '%s')]/parent::*//input[@type='checkbox']" % product_name

    class AddProduct:
        def topics(topics_name):
            return "//*[@class='nav nav-tabs']//a[contains (., '%s')]" % topics_name

        class General:
            product_name_input = {"xpath": "//*[@id='input-name1']"}
            meta_tag_title = {"xpath": "//*[@id='input-meta-title1']"}

        class Data:
            model_input = {"xpath": "//*[@id='input-model']"}
            price_input = {"xpath": "//*[@id='input-price']"}
            quantity_input = {"xpath": "//*[@id='input-quantity']"}
