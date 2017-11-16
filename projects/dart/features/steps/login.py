from behave import given
from pages import LoginPage

@given('an anonymous user')
def step_impl(context):
    pass


@given('an logged in user')
def step_impl(context):
    login_page = LoginPage(context)
    login_page.navigate()
    login_page.set_name(context.credentials['login'])
    login_page.login()


@then('I am redirected to the login page')
def step_impl(context):
    assert 'Login as user' in context.browser.page_source
