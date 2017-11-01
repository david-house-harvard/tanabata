from behave import when, then

from pages import MainPage, AboutPage


@then('I open about page')
def step_impl(context):
    MainPage(context).go_about()


@then('I can see Harvard-X background')
def step_impl(context):
    AboutPage(context).check_background('harvardx-bg')


@then('I can see Screenshot Highlighting Canvas Import image')
def step_impl(context):
    AboutPage(context).check_image('canvas-image')


@then('I can see Harvard YouTube ScreenShot')
def step_impl(context):
    AboutPage(context).check_image('youtube-image')


@then('I can see DART Ecosystem image')
def step_impl(context):
    AboutPage(context).check_image('ecosystem-image')


@then('I can see Text-Based Resource Counts Across All HarvardX SVG')
def step_impl(context):
    context.browser.find_element_by_css_selector("svg")


@then('I can click on Canvas Beta Tester Registration link')
def step_impl(context):
    AboutPage(context).check_link('canvas-link')


@then('I can click on edX XML link')
def step_impl(context):
    AboutPage(context).check_link('edx-xml-link')


@then('I can click on Harvard annotation tool link')
def step_impl(context):
    AboutPage(context).check_link('annotate-link')


@then('I can click on VPAL-Research link')
def step_impl(context):
    AboutPage(context).check_link('research-link')


@then('I can click on HUIT link on DART Architecture')
def step_impl(context):
    AboutPage(context).check_link('huit-link')


@then('I can click on HUIT link second on HUIT')
def step_impl(context):
    AboutPage(context).check_link('huit-second-link')


@then('I can click on HarvardX link on DART Architecture')
def step_impl(context):
    AboutPage(context).check_link('harx-link')


@then('I can click on collaborative group of researchers on VPAL Research Group')
def step_impl(context):
    AboutPage(context).check_link('harx-second-link')


@then('I can click on The Office of the Vice Provost for Advances in Learning (VPAL) link')
def step_impl(context):
    AboutPage(context).check_link('office-link')

