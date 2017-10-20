import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeDriverManager, IEDriverManager
from webdriver_manager.phantomjs import PhantomJsDriverManager


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
        if 'docker' in context.config.userdata.keys():
            from pyvirtualdisplay import Display
            display = Display(visible=0, size=(1200, 600))
            display.start()
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            options.add_argument('window-size=1200x600')
            options.add_argument('--no-sandbox')
            context.browser = webdriver.Chrome(chrome_options=options)
            global BEHAVE_DEBUG_ON_ERROR
            BEHAVE_DEBUG_ON_ERROR = False
        else:
            context.browser = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'firefox':
        context.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == 'edge':
        context.browser = webdriver.Edge(EdgeDriverManager().install())
    elif browser == 'safari':
        context.browser = webdriver.Safari()
    elif browser == 'ie':
        context.browser = webdriver.Ie(IEDriverManager().install())
    elif browser == 'opera':
        context.browser = webdriver.Opera()
    elif browser == 'phantomjs':
        context.browser = webdriver.PhantomJS(PhantomJsDriverManager().install())
    else:
        print("Browser you entered:", browser, "is invalid value")

    context.browser.implicitly_wait(WAIT)
    context.browser.set_window_size(1920, 1080)

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
