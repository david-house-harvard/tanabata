"""
AboutPage implementation.
"""
import re

import requests


from .common_page import CommonPage


class AboutPage(CommonPage):
    def check_image(self, picture):
        el = self.find(attr_name=picture)
        r = requests.get(el.get_attribute('src'))
        assert r.status_code == 200
        assert int(el.value_of_css_property('opacity')) > 0
        assert int(el.size['height']) > 10

    def check_background(self, picture):
        el = self.find(attr_name=picture)
        src = re.search(r'"(.*)"', el.value_of_css_property('background-image'))
        s = None
        if src:
            s = src.group(1)
        r = requests.get(s)
        assert r.status_code == 200
        assert int(el.value_of_css_property('opacity')) > 0
        assert int(el.size['height']) > 10

    def check_link(self, link_name):
        el = self.find(attr_name=link_name)
        link = el.get_attribute('href')
        r = requests.get(link)
        el.click()
        assert r.status_code == 200

        self.browser.switch_to_window(self.browser.window_handles[0])
