"""
BrowsePage implementation.
"""
import requests

from .common_page import CommonPage


class CollectionsPage(CommonPage):
    '''
        xxx

        xxx

        xxx
    '''
    def open_edx_banner(self):
        self.browser.get('/browse/collections/d09a4ffd-0f14-4016-9747-5f84655e9659')

    def see_harvard_collection_name(self):
        self.find('collection-title').text()

    def see_and_click_breadcrumbs(self):
        self.click('collection-breadcrumb')
        self.click('collection-breadcrumb-parent')

    def see_block(self, name):
        el = self.find(attr_name=name)
        assert el.is_displayed()
        assert int(el.value_of_css_property('opacity')) > 0
        assert int(el.size['height']) > 5

    def click(self, attr_name):
        el = self.find(attr_name=username)
        r = requests.get(el.get_attribute('src'))
        assert r.status_code == 200



