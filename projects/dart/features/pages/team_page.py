"""
TeamPage implementation.
"""
from selenium.common.exceptions import NoSuchElementException

from .common_page import CommonPage

class TeamPage(CommonPage):
    def check_elements(self, attr_name):
        elements = self.find_all(attr_name=attr_name)
        all_elements = self.find_all(attr_name='team-member-card')
        assert len(elements) == len(all_elements)

    def check_names(self):
        self.check_elements(attr_name='team-member-name')

    def check_course_images(self):
        self.check_elements(attr_name='all-image-descr')

