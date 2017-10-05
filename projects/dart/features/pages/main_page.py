"""
Main PageObject class.
"""
from .common_page import CommonPage

class MainPage(CommonPage):
    """
    Main Page implementation.
    """
    def do_search(self, key):
        """
        Fill search field with a key.
        """
        self.browser.find_element_by_name('query').send_keys('moon')
        self.browser.find_element_by_css_selector('.btn').click()

    def go_browse(self):
        self.browser.find_element_by_css_selector('[title="DART Browse"]').click()

    def go_search(self):
        self.browser.find_element_by_css_selector('[title="DART Search"]').click()
