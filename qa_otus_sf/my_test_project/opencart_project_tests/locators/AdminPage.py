class AdminPage:
    continue_button = "//*[text() = 'Continue']"
    button_submit = "//input[@type='submit']"
    button_back = "//*[text() = 'Back']"
    login_button = "input[@value='Login']"
    list_group_column_links = "//div[@class='list-group']/a"
    email_input = "//input[@name='email']"
    password_input = "//input[@name='password']"
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

    class Account:
        h2 = "//h2"




