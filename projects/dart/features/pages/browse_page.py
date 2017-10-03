"""
BrowsePage implementation.
"""
from selenium.common.exceptions import NoSuchElementException

from .common_page import CommonPage

class BrowsePage(CommonPage):
    """
    Browse page implementation.

    Set current pagination items number.
    """
    items_on_page = 20

    def check_elements(self, attr_name):
        elements = self.find_all(attr_name=attr_name)
        all_elements = self.find_all(attr_name='count-cards')
        assert len(elements) == len(all_elements)

    def check_course_names(self):
        self.check_elements(attr_name='name-course')

    def check_course_images(self):
        self.check_elements(attr_name='all-image-descr')

    def check_course_source(self):
        count = (
            len(self.find_all(attr_name='all-item-descr')) +
            len(self.find_all(attr_name='harvardx-item-descr')) +
            len(self.find_all(attr_name='harvard-youtube-item-descr'))
        )
        all_elements = self.find_all(attr_name='count-cards')
        assert len(all_elements) == count

    def click_card(self):
        self.click(attr_name='count-cards')

    def click_view_all(self):
        self.click(attr_name='all-source-sidebar')

    @property
    def is_on_collection_page(self):
        self.find(attr_name='collection-page')

    @property
    def pagination_is_present(self):
        self.find(attr_name='all-pagination')

    @property
    def harvard_has_items(self):
        el = self.find(attr_name='value-harvardx-sidebar')
        assert int(el.text) > 0

    @property
    def youtube_has_items(self):
        el = self.find(attr_name='value-youtube-sidebar')
        assert int(el.text) > 0

    def click_on_second_page(self):
        elements = self.find_all(attr_name='page_link')
        elements[1].click()

    @property
    def harvard_has_more_items(self):
        el = self.find(attr_name='value-harvardx-sidebar')
        assert int(el.text) > self.items_on_page

    @property
    def pagination_works(self):
        self.find(attr_name='all-pagination')
        courses_count = int(self.find(attr_name='value-harvardx-sidebar').text)
        pages_count = len(self.find_all(attr_name='page_link'))
        calculated = (
            courses_count // self.items_on_page
            if courses_count % self.items_on_page == 0
            else courses_count // self.items_on_page + 1
        )
        assert pages_count == calculated
        last_page = self.find_all(attr_name='page_link')[-1]
        last_page.click()
        assert len(self.find_all(attr_name='count-cards')) == courses_count % self.items_on_page

    def check_all_pages(self):
        elements = self.find_all(attr_name='page_link')
        for i in range(len(elements)):
            page = self.find_all(attr_name='page_link')[i]
            page.click()
            self.check_course_names()
            self.check_course_images()
            self.check_course_source()

    def click_harvard_sidebar(self):
        self.click(attr_name='harvardx-source-sidebar')

    def click_youtube_sidebar(self):
        self.click(attr_name='youtube-source-sidebar')

    @property
    def can_see_only_harvard(self):
        try:
            self.find(attr_name='harvard-youtube-item-descr')
        except NoSuchElementException:
            pass
        else:
            raise NoSuchElementException("There are some non Harvard items.")

    @property
    def can_see_up_to_cars(self):
        elements = self.find_all(attr_name='count-cards')
        assert len(elements) <= self.items_on_page

    @property
    def can_see_only_youtube(self):
        try:
            self.find(attr_name='harvardx-item-descr')
        except NoSuchElementException:
            pass
        else:
            raise NoSuchElementException("There are some non Youtube items.")

    @property
    def can_see_list_source_sidebar(self):
        self.find(attr_name='list-source-sidebar')
