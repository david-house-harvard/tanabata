"""
Common methods to work with pages.

"""


class BasePage:
    """
       Includes common actions for any page.
    """
    def __init__(self, context):
        self.browser = context.browser

    def find(self, attr_name):
        el = self.browser.find_element_by_css_selector('{}'.format(attr_name))
        return el

    def click(self, attr_name):
        el = self.find(attr_name)
        el.click()
        return el
