import requests
from behave import given, when, then
from selenium import webdriver

from utils.common import assert_has_width


@when('I open about page')
def step_impl(context):
    br = context.browser
    br.get(context.base_url)
    #br.execute_script("document.body.style.background = 'none'")
    # context.browser.implicitly_wait(100)
    br.find_element_by_css_selector(
        'ul>li>a[href$="{}/search/about"]'.format(context.base_url)
    ).click()


@then('I can see about_canvas_import_screenshot_indicator.png')
def step_impl(context):
    assert_has_width(
        context.browser,
        context.browser.find_element_by_css_selector(
            "div>img[src$='static/search/img/about_canvas_import_screenshot_indicator.png']"
        )
    )


@then('I can see Harvard_YouTube_ScreenShot.png')
def step_impl(context):
    assert_has_width(
        context.browser,
        context.browser.find_element_by_css_selector(
            "div>img[src$='static/search/img/Harvard_YouTube_ScreenShot.png']"
        )
    )


@then('I can see DART_Ecosystem_Feb_17.png')
def step_impl(context):
    assert_has_width(
        context.browser,
        context.browser.find_element_by_css_selector(
            "div>img[src$='static/search/img/DART_Ecosystem_Feb_17.png']"
        )
    )


@then('I can see SVG')
def step_impl(context):
    context.browser.find_element_by_css_selector("svg")


@then('I can click on https://harvard.az1.qualtrics.com link')
def step_impl(context):
    br = context.browser

    br.find_element_by_css_selector(
        'div>h4>a[href$="https://harvard.az1.qualtrics.com/jfe/form/SV_d3VpcAXlAPW4dMh"]'
    ).click()

    r = requests.get("https://harvard.az1.qualtrics.com/jfe/form/SV_d3VpcAXlAPW4dMh")
    assert r.status_code == 200

    br.switch_to_window(br.window_handles[0])


@then('I can click on https://edx.readthedocs.io link')
def step_impl(context):
    br = context.browser

    br.find_element_by_css_selector(
        'div>p>a[href$="https://edx.readthedocs.io/projects/edx-open-learning-xml/en/latest/"]'
    ).click()

    r = requests.get("https://edx.readthedocs.io/projects/edx-open-learning-xml/en/latest/")
    assert r.status_code == 200

    br.switch_to_window(br.window_handles[0])


@then('I can click on http://annotation.chs.harvard.edu/ link')
def step_impl(context):
    br = context.browser

    br.find_element_by_css_selector(
        'div>p>a[href$="http://annotation.chs.harvard.edu/"]'
    ).click()

    r = requests.get("http://annotation.chs.harvard.edu/")
    assert r.status_code == 200

    br.switch_to_window(br.window_handles[0])


@then('I can click on http://vpal.harvard.edu/research link')
def step_impl(context):
    br = context.browser

    br.find_element_by_css_selector(
        'div>p>a[href$="http://vpal.harvard.edu/research"]'
    ).click()

    r = requests.get("http://vpal.harvard.edu/research")
    assert r.status_code == 200

    br.switch_to_window(br.window_handles[0])


@then('I can click on http://huit.harvard.edu/ link')
def step_impl(context):
    br = context.browser

    br.find_element_by_css_selector(
        'div>p>a[href$="http://huit.harvard.edu/"]'
    ).click()

    r = requests.get("http://huit.harvard.edu/")
    assert r.status_code == 200

    br.switch_to_window(br.window_handles[0])


@then('I can click on http://huit.harvard.edu/ link second')
def step_impl(context):
    br = context.browser

    br.find_element_by_css_selector(
       'div>p>a[href$="http://huit.harvard.edu/"][title$="HUIT web site"]'
    ).click()

    r = requests.get("http://huit.harvard.edu/")
    assert r.status_code == 200

    br.switch_to_window(br.window_handles[0])


@then('I can click on http://harvardx.harvard.edu/ link')
def step_impl(context):
    br = context.browser

    br.find_element_by_css_selector(
        'div>p>a[href$="http://harvardx.harvard.edu/"]'
    ).click()

    r = requests.get("http://harvardx.harvard.edu/")
    assert r.status_code == 200

    br.switch_to_window(br.window_handles[0])


@then('I can click on http://vpal.harvard.edu/research link second')
def step_impl(context):
    br = context.browser

    br.find_element_by_css_selector(
        'div>p>a[href$="http://vpal.harvard.edu/research"][title$="Information on the Advances in Learning Research Group"]'
    ).click()

    r = requests.get("http://vpal.harvard.edu/research")
    assert r.status_code == 200

    br.switch_to_window(br.window_handles[0])


@then('I can click on http://vpal.harvard.edu/ link')
def step_impl(context):
    br = context.browser

    br.find_element_by_css_selector(
        'div>p>a[href$="http://vpal.harvard.edu/"]'
    ).click()

    r = requests.get("http://vpal.harvard.edu")
    assert r.status_code == 200

    br.switch_to_window(br.window_handles[0])
