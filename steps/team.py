from behave import given, when, then


@when('I open team page')
def step_impl(context):
    br = context.browser
    br.get('https://dart-test-stage.raccoongang.com/')
    br.find_element_by_css_selector('ul>li>a[href$="https://dart-test-stage.raccoongang.com/search/team"]').click()


@then('I can see aang foto')
def step_impl(context):
    context.browser.find_element_by_css_selector(
        "div>img[src$='/static/search/img/team/aang.jpg']"
    )

@then('I can see vbucchieri foto')
def step_impl(context):
    context.browser.find_element_by_css_selector(
        "div>img[src$='/static/search/img/team/vbucchieri.jpg']"
    )

@then('I can see jmclaus foto')
def step_impl(context):
    context.browser.find_element_by_css_selector(
        "div>img[src$='/static/search/img/team/jmclaus.jpg']"
    )

@then('I can see pmcgachey foto')
def step_impl(context):
    context.browser.find_element_by_css_selector(
        "div>img[src$='/static/search/img/team/pmcgachey.jpg']"
    )

@then('I can see dseaton foto')
def step_impl(context):
    context.browser.find_element_by_css_selector(
        "div>img[src$='/static/search/img/team/dseaton.jpg']"
    )

@then('I can see dtingley foto')
def step_impl(context):
    context.browser.find_element_by_css_selector(
        "div>img[src$='/static/search/img/team/dtingley.jpg']"
    )

@then('I can see sturkay foto')
def step_impl(context):
    context.browser.find_element_by_css_selector(
        "div>img[src$='/static/search/img/team/sturkay.jpg']"
    )

@then('I can see eyates foto')
def step_impl(context):
    context.browser.find_element_by_css_selector(
        "div>img[src$='/static/search/img/team/eyates.jpg']"
    )
