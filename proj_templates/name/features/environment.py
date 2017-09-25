"""
Can be customized.
"""

import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

BEHAVE_DEBUG_ON_ERROR = True
WAIT = os.getenv('WAIT', 1)

def before_scenario(context, scenario):
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
    elif browser == 'edge':
        context.browser = webdriver.Edge()
    elif browser == 'safari':
        context.browser = webdriver.Safari()
    elif browser == 'ie':
        context.browser = webdriver.Ie()
    elif browser == 'opera':
        context.browser = webdriver.Opera()
    elif browser == 'phantomjs':
        if 'docker' in context.config.userdata.keys():
            context.browser = webdriver.Remote(
                command_executor='http://phantomjs:8910',
                desired_capabilities=DesiredCapabilities.PHANTOMJS
            )
        else:
            context.browser = webdriver.PhantomJS()
    else:
        print("Browser you entered:", browser, "is invalid value")

    context.browser.implicitly_wait(WAIT)
    context.browser.maximize_window()

    context.base_url = context.config.userdata.get('instance_url')


def after_scenario(context, scenario):
    if scenario.status == "failed":
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        os.chdir("screenshots")
        context.browser.save_screenshot(scenario.name + "_failed.png")

    context.browser.quit()

def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        import pdb
        pdb.post_mortem(step.exc_traceback)
