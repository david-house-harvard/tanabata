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
        self.browser.is_displayed(el)
        r = requests.get(el.get_attribute("src"))
        everything_is_ok = r.status_code == 200 and el.value_of_css_property('opacity') > 0 and el.size.height > 10
        assert everything_is_ok

    def check_svg(self, username):
        el = self.find(attr_name=username)
        self.browser.is_displayed(el)
        everything_is_ok = el.value_of_css_property('opacity') > 0 and el.size.height > 5
        assert everything_is_ok

    def check_logo_vpal(self):
        self.check_elements(attr_name='logo-VPAL')
    def check_sections(self):
        if self.check_elements(attr_name='team-section'):
            elements = self.find_all(attr_name='team-section')
        assert len(elements) == 4

    def check_vpal(self):
        elements = self.find_all(attr_name='team-section')
        assert elements[0]

    def check_huit(self):
        elements = self.find_all(attr_name='team-section')
        assert elements[1]

    def check_contract(self):
        elements = self.find_all(attr_name='team-section')
        assert elements[2]

    def check_alumni(self):
        elements = self.find_all(attr_name='team-section')
        assert elements[3]

    def check_aang_photo(self):
        self.find(attr_name=)

