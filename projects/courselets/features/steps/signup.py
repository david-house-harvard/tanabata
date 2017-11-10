from projects.courselets.features.utils.temp_mail import email_confirmation
from behave import given, when, then
from projects.courselets.features.pages.login_page import LoginPage
from projects.courselets.features.pages.main_page import MainPage
import time

USERNAME_TWITTER = 'lbsr@szerz.com'
PASSWORD_TWITTER = 'Kolesnik99'


@given('an unregistered user')
def step_impl(context):
    pass


@when('I submit a valid email')
def step_impl(context):
    email_generation = email_confirmation.temporary_email_generate()

    br = context.browser
    br.get(context.base_url + 'login/')
    login_page = LoginPage(context)
    login_page.signup_form(email_generation)
    check_sent_message = login_page.email_sent_popup()

    assert check_sent_message == email_generation

    time.sleep(10)

    inbox = email_confirmation.get_mails(email_generation)
    convert = email_confirmation.get_link(inbox)
    get_link = email_confirmation.get_clear_link(convert)
    confirm_email = br.get(get_link)

    time.sleep(5)


@then('I am redirected to login success page')
def step_impl(context):
    success_page = MainPage(context).page_url()
    assert success_page == (context.base_url + 'ct/')


@when('I submit an invalid email')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + 'login/')
    LoginPage(context).signup_form('test')


@then('I get warning message')
def step_impl(context):
    message_text = 'You passed not correct data. Email - enter a valid email address.'
    login_page = LoginPage(context).alert_email()

    assert message_text == login_page


@when('I submit a valid twitter credentials')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + 'login/')
    LoginPage(context).twitter(USERNAME_TWITTER, PASSWORD_TWITTER)
    time.sleep(3)


@then('I am redirected to login welcome page')
def step_impl(context):
    success_page = MainPage(context).page_url()
    assert success_page == (context.base_url + 'ct/')
