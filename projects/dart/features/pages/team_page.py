"""
TeamPage implementation.
"""
import requests

from .common_page import CommonPage


class TeamPage(CommonPage):
    def check_elements(self, attr_name):
        """
            Check that all cards includes some tag (ex. name).

            Extended description of function.

            'team-member-card' (str): data attribute for each card on team page
            attr_name (str): Data attribute to check that card contains
        """

        elements = self.find_all(attr_name=attr_name)
        all_elements = self.find_all(attr_name='team-member-card')
        assert len(elements) == len(all_elements)

    def check_names(self):
        self.check_elements(attr_name='team-member-name')

    def check_section(self, name):
        assert self.find(attr_name=name)

    def check_photo(self, username):
        el = self.find(attr_name=username)
        r = requests.get(el.get_attribute('src'))
        assert r.status_code == 200
        assert int(el.value_of_css_property('opacity')) > 0
        assert int(el.size['height']) > 10

    def check_svg(self, username):
        el = self.find(attr_name=username)
        assert int(el.value_of_css_property('opacity')) > 0
        assert int(el.size['height']) > 5

    def check_link(self, link_name):
        el = self.find(attr_name=link_name)
        link = el.get_attribute('href')
        r = requests.get(link)
        el.click()
        assert r.status_code == 200

        self.browser.switch_to_window(self.browser.window_handles[0])
