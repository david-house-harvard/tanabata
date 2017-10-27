from behave import given, when, then

from pages import MainPage, SearchPage


@then('I can see search results!')
def step_impl(context):
    SearchPage(context).i_see_results()


@then('I can compare term search result with content')
def step_impl(context):
    SearchPage(context).compare_result()


@then('I can count all search results with items in sidebar')
def step_impl(context):
    SearchPage(context).count_results()


@then('I can do search again on search page')
def step_impl(context):
    SearchPage(context).do_search_again()


@when('I can do search again on search page')
def step_impl(context):
    SearchPage(context).do_search_again()


@then('I can click on filtering')
def step_impl(context):
    SearchPage(context).click_on_filter()


@then('I can see my search request with Search HarvardX Only filtering')
def step_impl(context):
    SearchPage(context).see_filtered_result()


@then('I can count filtering search results with items in sidebar')
def step_impl(context):
    SearchPage(context).count_results()


@then('I can see firsts top courses')
def step_impl(context):
    SearchPage(context).see_top_courses()


@when('I choose search Harvard Only')
def step_impl(context):
    SearchPage(context).click_on_filter()


@then('I can see firsts top courses include filtering Harvard Only')
def step_impl(context):
    SearchPage(context).see_filtered_top_cards()


@then('I can see image with name courses and organization name in this top/hot courses')
def step_impl(context):
    SearchPage(context).see_filtered_top_cards()


@then('I see filtering lists with count search result')
def step_impl(context):
    SearchPage(context).i_see_filters_and_numbers()


@then('I can check all lists items and count them with tabulated results')
def step_impl(context):
    SearchPage(context).calc_filtered()


@then('I can check one results which have name, icons')
def step_impl(context):
    SearchPage(context).check_result_content()


@then('I can click on youtube channel link in one results')
def step_impl(context):
    SearchPage(context).check_link('creator')


@then('I can click on a preview video button')
def step_impl(context):
    SearchPage(context).check_preview()


@then('I can click link on edx course link')
def step_impl(context):
    SearchPage(context).check_link('course-link')


@then('I can click link on created by is')
def step_impl(context):
    SearchPage(context).check_link('creator')


@when('I resize my windows')
def step_impl(context):
    SearchPage(context).resize()


@then('I can see right location blocks on a page')
def step_impl(context):
    SearchPage(context).check_mobile_elements_visible()
