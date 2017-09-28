"""
Main PageObject class.
"""

class MainPage:
    """
    Main Page implementation.
    """
    def __init__(self, context):
        self.browser = context.browser

    def do_search(self, key):
        """
        Fill search field with a key.
        """
        self.browser.find_element_by_name('query').send_keys('moon')
        self.browser.find_element_by_css_selector('.btn').click()

    def go_browse(self):
        self.browser.find_element_by_css_selector('[title="DART Browse"]').click()
