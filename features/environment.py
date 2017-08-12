from selenium import webdriver


def before_all(context):
    context.browser = webdriver.PhantomJS()
    context.browser.implicitly_wait(1)
    context.browser.maximize_window()
    context.base_url = 'https://dart-test-stage.raccoongang.com/'


def after_all(context):
    context.browser.quit()


def before_feature(context, feature):
    pass
