"""
Common method to work with pages.
"""

class CommonPage:
    """
    Includes common actions not related to particular page.
    """
    def __init__(self, context):
        self.browser = context.browser

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

    def find_all(self, attr_name):
        elements = self.browser.find_elements_by_css_selector(
            '[data-test="{}"]'.format(attr_name)
        )
        return elements
