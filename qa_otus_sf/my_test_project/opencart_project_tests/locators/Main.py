class Main:
    promoblock = "//*[@class='swiper-viewport']"

    class Featured:
        block_featured = "//div[@id='content']/*[@class='row']"
        products = block_featured + "/*[contains(@class, 'product-layout')]"
        names = products + "//h4"

