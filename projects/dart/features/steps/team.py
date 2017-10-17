from behave import given, when, then
from pages import MainPage, TeamPage


@when ('I open team page')
def step_impl(context):
    MainPage(context).go_team()


@then ('I can see four sections')
def step_impl(context):
    TeamPage(context).check_sections()


@then ('I can see Vpal team section')
def step_impl(context):
    TeamPage(context).check_vpal()


@then('I can see logo VPAL')
def step_impl(context):
    TeamPage(context).check_logo_vpal()


@then('I can see aang foto')
def step_impl(context):
    TeamPage(context).check_aang_photo()