from behave import given, when, then

from pages import MainPage, SearchPage


@then('I can see search results!')
def step_impl(context):
    SearchPage(context).i_see_results()


@then('Then I can compare term search result with content')
def step_impl(context):
    MainPage(context).compare_result('arg')

