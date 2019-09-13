class Main:
    promoblock = {"xpath": "//*[@class='swiper-viewport']"}

    class Featured:
        block_featured = {"xpath": "//div[@id='content']/*[@class='row']"}
        products = {"xpath": block_featured["xpath"] + "/*[contains(@class, 'product-layout')]"}
        names = {"xpath": products["xpath"] + "//h4"}
