def test_example(browser):
    browser.get('http://localhost')
    title_link_text = browser.find_element_by_xpath('//h1/a').text
    assert 'Your Store' == title_link_text