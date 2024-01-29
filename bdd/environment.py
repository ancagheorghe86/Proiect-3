from driver import Driver
from pages.login_page import LoginPage

def before_all(context):
    context.browser = Driver()
    context.login_page = LoginPage()
    #context.register_page = RegisterPge()

def after_all(context):
    context.browser.close()



