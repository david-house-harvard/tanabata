import re
import requests
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from utils.common import assert_has_width
from pages import MainPage, BrowsePage


@when('I opened Browse page')
@given('I opened Browse page')
def step_impl(context):
    MainPage(context).go_browse()


@given('I saw Content Sources with list group item')
def step_impl(context):
    BrowsePage(context).can_see_list_source_sidebar


@when('I can click on Harvard YouTube item')
@when('I can click Harvard YouTube item')
def step_impl(context):
    BrowsePage(context).click_youtube_sidebar()


@then('I can see only Harvard YouTube item')
def step_impl(context):
    BrowsePage(context).can_see_only_youtube


@when('I can see less or equal items then 20')
@then('I can see next up to 20 cards on a page')
@then('I can see first 20 cards on a page')
@then('I can see up to 20 cards on a page')
def step_impl(context):
    BrowsePage(context).can_see_up_to_cars


@when('I can click HarvardX item')
@when('I click on HarvardX item')
def step_impl(context):
    BrowsePage(context).click_harvard_sidebar()

@then('I can see only HarvardX item')
def step_impl(context):
    BrowsePage(context).can_see_only_harvard


@when('I can click View All item')
@then('I can click View All item')
def step_impl(context):
    BrowsePage(context).click_view_all()


@then('each card has name-source')
def step_impl(context):
    BrowsePage(context).check_course_source()


@then('each card has image')
def step_impl(context):
    BrowsePage(context).check_course_images()


@then('each card has name-course')
def step_impl(context):
    BrowsePage(context).check_course_names()


@when('I click on a card')
def step_impl(context):
    BrowsePage(context).click_card()


@then('I can see collection page')
def step_impl(context):
    BrowsePage(context).is_on_collection_page

@when('I can see more then 20 cards')
@given('I can see all items pagination')
def step_impl(context):
    BrowsePage(context).pagination_is_present


@when('I can see more then 20 cards in HarvardX')
@when('I can see more cards than 20 in HarvardX')
def step_impl(context):
    BrowsePage(context).harvard_has_more_items


@when('I can click for page number 2 on pagination')
def step_impl(context):
    BrowsePage(context).click_on_second_page()


@given('I can see number X in HarvardX')
def step_impl(context):
    BrowsePage(context).harvard_has_items


@given('I can see number Y in YouTube')
def step_impl(context):
    BrowsePage(context).youtube_has_items


@then('I can see one item pagination')
def step_impl(context):
    BrowsePage(context).pagination_works


@then('I can click on all pages in pagination')
def step_impl(context):
    BrowsePage(context).check_all_pages()
