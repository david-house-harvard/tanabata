from behave import given, when, then


@when('I open about page')
def step_impl(context):
    br = context.browser
    br.get('https://dart-test-stage.raccoongang.com/')
    br.find_element_by_css_selector('ul>li>a[href$="https://dart-test-stage.raccoongang.com/search/about"]').click()


@then('I can see import to canvas LMS image')
def step_impl(context):
    br = context.browser

    assert br.find_element_by_css_selector(
        "div>img[src$='static/search/img/about_canvas_import_screenshot_indicator.jpg']"
    )
    assert br.find_element_by_css_selector(
        "div>img[src$='static/search/img/Harvard_YouTube_ScreenShot.png']"
    )
    assert br.find_element_by_css_selector(
        "div>img[src$='static/search/img/DART_Ecosystem_Feb_17.png']"
    )
    assert br.find_element_by_css_selector("svg")
