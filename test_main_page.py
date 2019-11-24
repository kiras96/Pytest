import time
# import pytest


# @pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_can_go_to_login_page(browser):
    link = f"http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()
    time.sleep(3)
