import os

from selenium import webdriver


def before_all(context):
    if 'browser' in context.config.userdata.keys():
        if context.config.userdata['browser'] is None:
            browser = 'chrome'
        else:
            browser = context.config.userdata['browser']
    else:
        browser = 'chrome'

    if browser == 'chrome':
        context.browser = webdriver.Chrome()
    elif browser == 'firefox':
        context.browser = webdriver.Firefox()
    elif browser == 'safari':
        context.browser = webdriver.Safari()
    elif browser == 'ie':
        context.browser = webdriver.Ie()
    elif browser == 'opera':
        context.browser = webdriver.Opera()
    elif browser == 'phantomjs':
        context.browser = webdriver.PhantomJS()
    else:
        print("Browser you entered:", browser, "is invalid value")

    context.browser.implicitly_wait(1)
    context.browser.maximize_window()

    context.base_url = context.config.userdata.get('instance_url')


def after_scenario(context, scenario):
    if scenario.status == "failed":
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        os.chdir("screenshots")
        context.browser.save_screenshot(scenario.name + "_failed.png")

def after_all(context):
    context.browser.quit()
