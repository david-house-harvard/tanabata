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

    def go_search(self):
        self.browser.find_element_by_css_selector('[title="DART Search"]').click()

    def find(self, attr_name):
        el = self.browser.find_element_by_css_selector(
            '[data-test="{}"]'.format(attr_name)
        )
        return el

    def click(self, attr_name):
        """
        attr_name: data-test attribute
        """
        el = self.find(attr_name)
        el.click()
        return el
