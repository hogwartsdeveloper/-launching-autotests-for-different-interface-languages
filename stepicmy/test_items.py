import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button_is_displayed(browser):
    browser.get(link)
    btns = browser.find_elements_by_css_selector("[type='submite']")
    assert len(btns) > 0, "Should be a button"