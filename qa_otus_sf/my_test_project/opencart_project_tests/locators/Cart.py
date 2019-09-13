class Cart:
    class bottom_btn:
        it = "//*[@class='buttons clearfix']"

        def button_name(name):
            button = "//*[@class='buttons clearfix']//a[contains (., '%s')]" % name
            return button
