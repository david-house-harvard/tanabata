from behave import given, when, then

from pages import MainPage, CollectionsPage


@when('I open banner edx-collection')
def step_impl(context):
    CollectionsPage(context).open_edx_banner()


@then('I can see harvardX Collections name')
def step_impl(context):
    CollectionsPage(context).open_edx_banner()

@then('I can see and click all links in breadcrumbs')
def step_impl(context):
    CollectionsPage(context).see_and_click_breadcrumbs()

@then('I can see card block')
def step_impl(context):
    CollectionsPage(context).see_block('collection-card')

@then('I can see card image holder')
def step_impl(context):
    CollectionsPage(context).see_block('card-image-holder')

@then('I can see metadata holder')
def step_impl(context):
    CollectionsPage(context).see_block('metadata-holder')


@then('I can see Launched icon, name and value')
def step_impl(context):
    CollectionsPage(context).see_block('launched-icon')
    CollectionsPage(context).see_block('launched-name')
    CollectionsPage(context).see_block('launched-value')


@then('I can see Creator icon, name and value, I can click on value')
def step_impl(context):
    CollectionsPage(context).see_block('creator-icon')
    CollectionsPage(context).see_block('creator-name')
    CollectionsPage(context).see_block('creator-value')
    CollectionsPage(context).click('creator-link')


@then('I can see Content type icon, name and value')
def step_impl(context):
    CollectionsPage(context).see_block('content-icon')
    CollectionsPage(context).see_block('content-name')
    CollectionsPage(context).see_block('content-value')


@then('I can see Subject Area Tags icon, name and value')
def step_impl(context):
    CollectionsPage(context).see_block('subject-icon')
    CollectionsPage(context).see_block('subject-name')
    CollectionsPage(context).see_block('subject-value')


@then('I can see Last updated icon, name and value')
def step_impl(context):
    CollectionsPage(context).see_block('update-icon')
    CollectionsPage(context).see_block('update-name')
    CollectionsPage(context).see_block('update-value')


@then('I can see results holder')
def step_impl(context):
    CollectionsPage(context).see_block('results-holder')


@then('I can see result filter')
def step_impl(context):
    CollectionsPage(context).see_block('results-filter')


@then('I can see filter list Asset Types')
def step_impl(context):
    CollectionsPage(context).see_block('asset-types')

@then('I can see filter list Collections Types')
def step_impl(context):
    CollectionsPage(context).see_block('collection-types')

@then('I can see list item Total resources which have icon, name and number')
def step_impl(context):
    CollectionsPage(context).see_block('collection-types')