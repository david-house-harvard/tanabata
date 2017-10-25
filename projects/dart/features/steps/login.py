from behave import given


@given('an anonymous user')
def step_impl(context):
    pass


@given('an logged in user')
def step_impl(context):
    br = context.browser
    br.get(context.base_url+'users/login/')
    br.find_element_by_name('username').send_keys('dummy')
    br.find_element_by_css_selector('[type="submit"]').click()


@then('I am redirected to the login page')
def step_impl(context):
    assert 'Login as user' in context.browser.page_source
