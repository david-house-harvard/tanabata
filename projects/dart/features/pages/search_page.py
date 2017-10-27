import re

import requests
from .common_page import CommonPage
from .main_page import MainPage


class SearchPage(CommonPage):

    def i_see_results(self):
        url = 'search/search?query=' in self.browser.current_url
        assert url
        assert self.browser.find_element_by_name('query')

    def compare_result(self):
        assert self.browser.find_elements_by_css_selector('tbody>tr')
        result_list = self.browser.find_elements_by_css_selector('tbody>tr>td>.match:first-child')
        query = self.browser.find_element_by_name('query').get_attribute('value').lower()
        counter = 0
        print(len(result_list))
        for item in result_list:
            result = True if query in item.text.lower() else False
            counter += 1
            if not result:
                print(counter, item.text.lower())
                assert False

    def count_results(self):
        active_tab = self.browser.find_element_by_css_selector('.filter-list__item.active h4').text
        number = self.browser.find_element_by_css_selector('.container-fluid.results>p>.text-danger').text
        result_list = self.browser.find_elements_by_css_selector('.preview-button')
        assert int(number) == len(result_list)

    def click_on_filter(self):
        self.browser.find_element_by_css_selector('#harvardx-checkbox').click()
        self.browser.find_element_by_css_selector('#result_search').click()

    def do_search_again(self):
        self.browser.find_element_by_css_selector('#result_search').click()

    def see_filtered_result(self):
        created_by = MainPage(self).find_all('creator')
        counter = 0
        for item in created_by:
            text = 'harvardx'
            result = item.text.lower()
            if text not in result and result:
                raise Exception(counter, text, result)

    def see_top_courses(self):
        hot_courses = self.browser.find_elements_by_css_selector('.hot-course__item')
        assert len(hot_courses) > 0

    def see_filtered_top_cards(self):
        created_by = self.browser.find_elements_by_css_selector('.list-group-item__source')
        counter = 0
        for item in created_by:
            text = 'harvardx'
            result = item.text.lower()
            if text not in result and result:
                raise Exception(counter, text, result)

    def top_cards_have_all(self):
        cards_num = len(MainPage(self).find_all('hot_course'))
        img_num = len(MainPage(self).find_all('hot_course_image'))
        creator_num = len(MainPage(self).find_all('hot_course_creator'))
        title_num = len(MainPage(self).find_all('hot_course_title'))
        assert cards_num == img_num
        assert cards_num == creator_num
        assert cards_num == title_num

    def i_see_filters_and_numbers(self):
        pass
        # assert len(self.browser.find_element_by_css_selector('.container-fluid.results>p>.text-danger')) > 0
        # assert len(MainPage(self).find_all('filter_tab')) > 0

    def calc_filtered(self):
        results = MainPage(self).find_all('search_result')
        results_len = int(MainPage(self).find('filter_num_results').text)
        counter = 0

        for item in results:
            if item.is_displayed():
                counter += 1
        assert counter == results_len

    def check_result_content(self):
        result = MainPage(self).find('search_result')
        icons_count = len(result.find_elements_by_css_selector('.fa'))
        icons_in_tab = 7
        titles_count = len(result.find_elements_by_css_selector('h4>a'))
        assert icons_count == icons_in_tab
        assert titles_count >= 1

    def check_link(self, link_name):
        el = self.find(attr_name=link_name)
        link = el.get_attribute('href')
        r = requests.get(link)
        el.click()
        assert r.status_code == 200
        self.browser.switch_to_window(self.browser.window_handles[0])

    def check_preview(self):
        el = MainPage(self).find('preview_button')
        el.click()

    def resize(self):
        self.browser.set_window_size(480,320)

    def check_mobile_elements_visible(self):
        assert self.browser.find_element_by_css_selector('.list-group-item.list-group-item-info').is_displayed()
        assert self.browser.find_element_by_css_selector('.hot-course_mobile-trigger').is_displayed()

    def null_results_search(self):
        self.browser.find_element_by_name('query').send_keys('qazxswedc')
        self.browser.find_element_by_css_selector('.btn').click()

    def see_no_results_text(self):
        query_text = self.browser.find_element_by_name('query').get_attribute('value')
        expected_result = 'We did not find any videos related to {}.'.format(query_text)
        result = self.browser.find_element_by_css_selector('#videos>h4').text
        assert result == expected_result
