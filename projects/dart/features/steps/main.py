import requests
from behave import given, when, then
from selenium import webdriver

from utils.common import assert_has_width
from pages import MainPage


@when('I open main page')
def step_impl(context):
    br = context.browser
    br.get(context.base_url)


@then('I can see harvard-logo and click on harvard-logo')
def step_impl(context):
    br = context.browser
    el = MainPage(context).click(attr_name='logo-harvard-header')
    r = requests.get(el.get_attribute("href"))
    assert r.status_code == 200

    br.switch_to_window(br.window_handles[0])


@then('I can click on an About in header')
def step_impl(context):
    MainPage(context).click(attr_name='page-about')
    context.browser.switch_to_window(context.browser.window_handles[0])


@then('I can click on a Team in header')
def step_impl(context):
    MainPage(context).click(attr_name='page-team')
    context.browser.switch_to_window(context.browser.window_handles[0])


@then('I can see dart-logo-link and click on dart-logo-link in header')
def step_impl(context):
    MainPage(context).click(attr_name='logo-dart-header')


@then('I can see Harvard University DART logo in content-wrapper')
def step_impl(context):
    MainPage(context).find(attr_name='logo-dart-content')


@then('I can see harvard-logo in footer')
def step_impl(context):
    MainPage(context).find(attr_name='logo-dart-footer')


@then('I can click on a Privacy')
def step_impl(context):
    br = context.browser
    el = MainPage(context).click(attr_name='link-privacy')
    r = requests.get(el.get_attribute("href"))
    assert r.status_code == 200

    br.switch_to_window(br.window_handles[0])


@then('I can click on an Accessibility')
def step_impl(context):
    br = context.browser
    el = MainPage(context).click(attr_name='link-accessibility')
    r = requests.get(el.get_attribute("href"))
    assert r.status_code == 200

    br.switch_to_window(br.window_handles[0])


@then('I can click on an Report copyright infringement')
def step_impl(context):
    br = context.browser
    el = MainPage(context).click(attr_name='link-infringement')
    r = requests.get(el.get_attribute("href"))
    assert r.status_code == 200

    br.switch_to_window(br.window_handles[0])


@then('I can do search on main page')
def step_impl(context):
    MainPage(context).do_search(key='moon')
    context.browser.switch_to_window(context.browser.window_handles[0])


@then('I can see search results')
def step_impl(context):
    assert 'View and filter all' in context.browser.page_source


@then('I can click on Browse link')
def step_impl(context):
    MainPage(context).go_browse()
    context.browser.switch_to_window(context.browser.window_handles[0])

@then('I can click on Search link')
def step_impl(context):
    MainPage(context).go_search()
    context.browser.switch_to_window(context.browser.window_handles[0])


@then('I can see DART catalog')
def step_impl(context):
    assert 'The DART catalog currently includes' in context.browser.page_source
