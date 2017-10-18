from behave import given, when, then
from pages import MainPage, TeamPage


@when('I go to main page')
def step_impl(context):
    context.browser.get(context.base_url)


@then ('I open team page')
def step_impl(context):
    MainPage(context).go_team()


@then ('I can see all cards have names')
def step_impl(context):
    TeamPage(context).check_names()


@then ('I can see Vpal team section')
def step_impl(context):
    TeamPage(context).check_section('vpal-section')


@then('I can see logo VPAL')
def step_impl(context):
    TeamPage(context).check_photo('logo-VPAL')


@then('I can see aang foto')
def step_impl(context):
    TeamPage(context).check_photo('aang')


@then('I can see dseaton foto')
def step_impl(context):
    TeamPage(context).check_photo('dseaton')


@then('I can see dtingley foto')
def step_impl(context):
    TeamPage(context).check_photo('dtingley')


@then('I can see sturkay foto')
def step_impl(context):
    TeamPage(context).check_photo('sturkay')


@then ('I can see HUIT team section')
def step_impl(context):
    TeamPage(context).check_section('huit-section')



@then('I can see logo HUIT')
def step_impl(context):
    TeamPage(context).check_photo('logo-huit')


@then('I can see pmcgachey foto')
def step_impl(context):
    TeamPage(context).check_photo('pmcgachey')


@then('I can see vbucchieri foto')
def step_impl(context):
    TeamPage(context).check_photo('vbucchieri')


@then('I can see eyates foto')
def step_impl(context):
    TeamPage(context).check_photo('eyates')


@then('I can see Contracted Support team section')
def step_impl(context):
    TeamPage(context).check_section('contract-section')


@then('I can see jmclaus logo')
def step_impl(context):
    TeamPage(context).check_photo('jmclaus')


@then('I can see raccoongang logo')
def step_impl(context):
    TeamPage(context).check_svg('raccoongang')


@then('I can click on raccoongang link')
def step_impl(context):
    TeamPage(context).check_link('raccoongang-link')


@then ('I can see Undergraduate Analytics and Research team section')
def step_impl(context):
    TeamPage(context).check_section('alumni-section')
