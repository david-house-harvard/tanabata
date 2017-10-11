from behave import given, when, then
from pages import MainPage, TeamPage


@when ('I open team page')
def step_impl(context):
    MainPage(context).go_team()


@then ('I can see four sections')
def step_impl(context):
    TeamPage(context).check_sections()


@then ('I can see all cards have names')
def step_impl(context):
    TeamPage(context).check_names()


@then ('I can see Vpal team section')
def step_impl(context):
    TeamPage(context).check_vpal()


@then('I can see logo VPAL')
def step_impl(context):
    TeamPage(context).check_photo('logo-vpal')


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


@then('I can see logo HUIT')
def step_impl(context):
    TeamPage(context).check_photo('logo-huit')


@then('I can see pmcgachey foto')
def step_impl(context):
    TeamPage(context).check_photo('vbucchieri')


@then('I can see eyates foto')
def step_impl(context):
    TeamPage(context).check_photo('eyates')

@then('I can see jmclaus logo')
def step_impl(context):
    TeamPage(context).check_photo('jmclaus')

@then('I can see raccoongang logo')
def step_impl(context):
    TeamPage(context).check_svg('raccoongang')