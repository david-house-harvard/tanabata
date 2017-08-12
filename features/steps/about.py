from behave import given, when, then


@when('I open about page')
def step_impl(context):
    br = context.browser
    br.get(context.base_url)
    br.find_element_by_css_selector(
        'ul>li>a[href$="{}/search/about"]'.format(context.base_url)
    ).click()


@then('I can see import to canvas LMS image')
def step_impl(context):
    br = context.browser

    # TODO distinguish same links
    #br.find_element_by_css_selector(
    #    'div>p>a[href$="http://huit.harvard.edu/"]'
    #).click()

    #br.switch_to_window(br.window_handles[-1])
    #assert 'Wait! Have you checked the new IT HELP site?' in br.page_source

    #br.switch_to_window(br.window_handles[0])

    #br.find_element_by_css_selector(
    #    'div>p>a[href$="http://harvardx.harvard.edu/"]'
    #).click()

    #br.switch_to_window(br.window_handles[-1])
    #assert 'Office of the Vice Provost for Advances In Learning' in br.page_source

    #br.switch_to_window(br.window_handles[0])


@then('I can see about_canvas_import_screenshot_indicator.jpg')
def step_impl(context):
    context.browser.find_element_by_css_selector(
        "div>img[src$='static/search/img/about_canvas_import_screenshot_indicator.jpg']"
    )


@then('I can see Harvard_YouTube_ScreenShot.png')
def step_impl(context):
    context.browser.find_element_by_css_selector(
        "div>img[src$='static/search/img/Harvard_YouTube_ScreenShot.png']"
    )


@then('I can see DART_Ecosystem_Feb_17.png')
def step_impl(context):
    context.browser.find_element_by_css_selector(
        "div>img[src$='static/search/img/DART_Ecosystem_Feb_17.png']"
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

    br.switch_to_window(br.window_handles[-1])
    assert 'Thank you for your interest in being a DART Canvas Beta Tester' in br.page_source

    br.switch_to_window(br.window_handles[0])


@then('I can click on https://edx.readthedocs.io link')
def step_impl(context):
    br = context.browser

    br.find_element_by_css_selector(
        'div>p>a[href$="https://edx.readthedocs.io/projects/edx-open-learning-xml/en/latest/"]'
    ).click()

    br.switch_to_window(br.window_handles[-1])
    assert 'EdX Open Learning XML Guide' in br.page_source

    br.switch_to_window(br.window_handles[0])


@then('I can click on http://annotation.chs.harvard.edu/ link')
def step_impl(context):
    br = context.browser

    br.find_element_by_css_selector(
        'div>p>a[href$="http://annotation.chs.harvard.edu/"]'
    ).click()

    br.switch_to_window(br.window_handles[-1])
    assert 'Annotation Tools for Teaching, Learning and Research' in br.page_source

    br.switch_to_window(br.window_handles[0])


@then('I can click on http://vpal.harvard.edu/research link')
def step_impl(context):
    br = context.browser

    br.find_element_by_css_selector(
        'div>p>a[href$="http://vpal.harvard.edu/research"]'
    ).click()

    br.switch_to_window(br.window_handles[-1])
    assert 'The Office of the Vice Provost for Advances in Learning Research Group enables research on how students learn.' in br.page_source

    br.switch_to_window(br.window_handles[0])


@then('I can click on http://huit.harvard.edu/ link')
def step_impl(context):
    br = context.browser

    br.find_element_by_css_selector(
        'div>p>a[href$="http://huit.harvard.edu/"]'
    ).click()

    br.switch_to_window(br.window_handles[-1])
    assert 'Wait! Have you checked the new IT HELP site?' in br.page_source

    br.switch_to_window(br.window_handles[0])


@then('I can click on http://harvardx.harvard.edu/ link')
def step_impl(context):
    br = context.browser

    br.find_element_by_css_selector(
        'div>p>a[href$="http://harvardx.harvard.edu/"]'
    ).click()

    br.switch_to_window(br.window_handles[-1])
    assert 'Office of the Vice Provost for Advances In Learning' in br.page_source

    br.switch_to_window(br.window_handles[0])


@then('I can click on http://vpal.harvard.edu/research link second')
def step_impl(context):
    br = context.browser

    br.find_element_by_css_selector(
        'div>p>a[href$="http://vpal.harvard.edu/research"][title$="Information on the Advances in Learning Research Group"]'
    ).click()

    br.switch_to_window(br.window_handles[-1])
    assert 'The Office of the Vice Provost for Advances in Learning Research Group enables research on how students learn' in br.page_source

    br.switch_to_window(br.window_handles[0])


@then('I can click on http://vpal.harvard.edu/ link')
def step_impl(context):
    br = context.browser

    br.find_element_by_css_selector(
        'div>p>a[href$="http://vpal.harvard.edu/"]'
    ).click()

    br.switch_to_window(br.window_handles[-1])
    assert 'Launched through a generous gift from Gustave and Rita Hauser' in br.page_source

    br.switch_to_window(br.window_handles[0])
