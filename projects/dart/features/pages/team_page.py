"""
TeamPage implementation.
"""
import requests
from .common_page import CommonPage


class TeamPage(CommonPage):
    def check_elements(self, attr_name):
        elements = self.find_all(attr_name=attr_name)
        all_elements = self.find_all(attr_name='team-member-card')
        assert len(elements) == len(all_elements)

    def check_names(self):
        self.check_elements(attr_name='team-member-name')

    def check_sections(self):
        assert len(self.find_all(attr_name='team-section')) == 4

    def check_photo(self, username):
        el = self.find(attr_name=username)
        r = requests.get(el.get_attribute('src'))
        assert r.status_code == 200
        assert el.value_of_css_property('opacity') > 0
        assert el.size['height'] > 10

    def check_svg(self, username):
        el = self.find(attr_name=username)
        assert el.value_of_css_property('opacity') > 0
        assert el.size['height'] > 5

    def check_link(self, link_name):
        el = self.find(attr_name=link_name)
        el.click()
        r = requests.get(el.get_attribute('src'))
        assert r.status_code == 200

        self.browser.switch_to_window(self.browser.window_handles[0])
