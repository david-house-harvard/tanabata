import re

from .common_page import CommonPage


class SearchPage(CommonPage):

    def i_see_results(self):
        url = 'search/search?query=' in self.browser.current_url
        assert url
        assert self.browser.find_element_by_name('query')

    def compare_result(self):
        print(self.browser.find_element_by_css_selector('tbody>tr'))
        assert self.browser.find_element_by_css_selector('tbody>tr')
        result_list = self.browser.find_element_by_css_selector('tbody>tr')
        print(result_list)
        query = self.browser.find_element_by_name('query').get_attribute('value')

        for item in result_list:
            result = True if query in item else False
            if not result:
                assert False

    def count_results(self):
        active_tab = self.browser.find_element_by_css_selector('.filter-list__item.active h4').text
        number = re.search(r'/((.*)/)', active_tab)
        result_list = self.browser.find_element_by_css_selector('tbody>tr')
        assert int(number.group(1)) == len(result_list)

    def
