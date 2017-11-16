"""
Generic login page
"""
from .common_page import CommonPage


class LoginPage(CommonPage):
    """
    Login page, functional in local deployment without HarvardKey
    """

    def navigate(self):
        self.browser.get(self.base_url+'/users/login/')

    def login(self):
        self.browser.find_element_by_css_selector('[type="submit"]').click()

    def set_name(self, name='moon'):
        self.browser.find_element_by_name('username').send_keys(name)
