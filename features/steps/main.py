import requests

from behave import given, when, then
from selenium import webdriver
from utils.common import assert_has_width

@when('I open main page')
def step_impl(context):
    br = context.browser
    br.get(context.base_url)


@then('I can see harvard-logo-container and click on harvard-logo-container')
def step_impl(context):
    br = context.browser
    br.find_element_by_id(
        "harvard-logo-container"
    ).click()
    r = requests.get("https://www.harvard.edu/")
    assert r.status_code == 200

    br.switch_to_window(br.window_handles[0])


@then('I can click on an About in header')
def step_impl(context):
    br = context.browser
    br.find_element_by_css_selector(
        'ul>li>a[href$="{}/search/about"]'.format(context.base_url)
    ).click()


@then('I can click on a Team in header')
def step_impl(context):
    br = context.browser
    br.find_element_by_css_selector(
        'ul>li>a[href$="{}/search/team"]'.format(context.base_url)
    ).click()


# @then('I can click on a Coming Soon in header')
# def step_impl(context):
#     br = context.browser
#     br.find_element_by_css_selector(
#         'ul>li>a[href$="#"]'
#     ).click()


@then('I can see dart-logo-link and click on dart-logo-link in header')
def step_impl(context):
    br = context.browser
    br.find_element_by_css_selector(
        'ul>li>a>img[src$="https://s3.amazonaws.com/vpal-static-findability-assets/branding/harvard/images/harvardDART_dark_bac_blue_DART_light.png"]'
    ).click()
    r = requests.get("https://dart-test-stage.raccoongang.com/search/")
    assert r.status_code == 200


@then('I can see Harvard University DART logo in content-wrapper')
def step_impl(context):
    context.browser.find_element_by_css_selector(
        "div>img[src$='https://s3.amazonaws.com/vpal-static-findability-assets/branding/harvard/images/harvardDART_light_bac.png']"
    )


@then('I can see harvard-logo in footer')
def step_impl(context):
    context.browser.find_element_by_css_selector(
        "div>img[src$='https://s3.amazonaws.com/vpal-static-findability-assets/branding/harvard/images/harvardDART_dark_bac_blue_DART_light.png']"
    )


@then('I can click on a Privacy')
def step_impl(context):
    br = context.browser
    br.find_element_by_css_selector(
        'div>p>a[href$="http://www.harvard.edu/privacy-statement"]'
    ).click()
    r = requests.get("http://www.harvard.edu/privacy-statement")
    assert r.status_code == 200
    br.switch_to_window(br.window_handles[0])


@then('I can click on an Accessibility')
def step_impl(context):
    br = context.browser
    br.find_element_by_css_selector(
        'div>p>a[href$="http://accessibility.harvard.edu/"]'
    ).click()
    r = requests.get("http://accessibility.harvard.edu/")
    assert r.status_code == 200
    br.switch_to_window(br.window_handles[0])


@then('I can click on an Report copyright infringement')
def step_impl(context):
    br = context.browser
    br.find_element_by_css_selector(
        'div>p>a[href$="http://www.harvard.edu/reporting-copyright-infringements"]'
    ).click()
    r = requests.get("https://www.harvard.edu/copyright-issue")
    assert r.status_code == 200
    br.switch_to_window(br.window_handles[0])


@then('I can type in HomeSearch field in content-wrapper')
def step_impl(context):
    context.browser.find_element_by_name('query').send_keys('moon')


@then('I can click on search button in content-wrapper')
def step_impl(context):
    context.browser.find_element_by_css_selector('.btn').click()


@then('I can see search results')
def step_impl(context):
    assert 'View and filter all' in context.browser.page_source


@then('I can click on Browse link')
def step_impl(context):
    context.browser.find_element_by_css_selector('[title="DART Browse"]').click()


@then('I can see DART catalog')
def step_impl(context):
    assert 'The DART catalog currently includes' in context.browser.page_source
