"""
Class to work with main page

"""
from .base_page import BasePage


class MainPage(BasePage):

    def page_url(self):
        return self.browser.current_url
