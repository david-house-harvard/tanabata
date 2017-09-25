from behave import given, when, then


@given('I am not stupid')
def step_impl(context):
    1 + 1 == 2


@when('I open google page')
def step_impl(context):
    br = context.browser
    # base_url should be set in env file
    br.get(context.base_url)


@then('I can see goole page content')
def step_impl(context):
    assert 'google' in context.browser.page_source
