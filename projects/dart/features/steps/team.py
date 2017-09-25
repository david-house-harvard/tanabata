from behave import given, when, then


@when('I open team page')
def step_impl(context):
    br = context.browser
    br.get(context.base_url)
    br.find_element_by_css_selector(
        'ul>li>a[href$="{}/search/team"]'.format(context.base_url)
    ).click()


@then('I can see "{member}" foto')
def step_impl(context, member):
    context.browser.find_element_by_css_selector(
        "div>img[src$='/static/search/img/team/{}.jpg']".format(member)
    )


@then('I can see logo "{logo_name}" with type "{logo_type}"')
def step_impl(context, logo_name, logo_type):
    context.browser.find_element_by_css_selector(
        "div>img[src$='/static/search/logo_{}.{}']".format(logo_name, logo_type)
    )
