from pages.page import Page

class LoginPage(Page):

    @property
    def email_field(self):
        self.is_element_visible_css('#identifierId')
        return self.is_element_visible_css('#identifierId')

    @property
    def password_field(self):
        password_field = self.is_element_visible_css('input[name="password"]')
        return password_field

    @property
    def text_log_in(self):
        text = self.is_text_present('//h1', 'Добро пожаловать')
        if text:
            return True
        else:
            return False\

    @property
    def text_wrong_code(self):
        text = self.is_text_present_by_css('div.GQ8Pzc', 'Wrong code. Try again.')
        if text:
            return True
        else:
            return False

    @property
    def scroll_to_language(self):
        element = self.is_element_visible_xpath('//*[@class="OA0qNb ncFHed"]//*[contains(text(), "Русский")]')
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        return element

    @property
    def button_language(self):
        return self.is_element_visible_xpath('//*[@class="MocG8c B9IrJb LMgvRb KKjvXb"]')

    @property
    def button_forgot_password(self):
        self.is_element_visible_css('#forgotPassword')
        button = self.is_element_visible_css('#forgotPassword')
        return button

    @property
    def button_next(self):
        return self.is_element_visible_xpath('//div//*[contains(text(), "Next")]')

    @property
    def account_recovery(self):
        self.is_text_present('//h1', "Account recovery")
        recovery_email_field = self.is_element_visible_css('input[name="password"]')
        return recovery_email_field

    @property
    def any_email(self):
        any_email_field = self.is_element_visible_css('input#idvAnyEmailPin')
        return any_email_field





