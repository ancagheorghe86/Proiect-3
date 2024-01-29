import unittest

from pages.login_page import LoginPage

class LoginTests(unittest.TestCase):
    def test_invalod_login(self):
        login_page = LoginPage()

        # 1. intru pe pagina de login -> login_page.open()
        # 2. caut input email -> scriu email in input email -> login_page.set_email(email)
        # 3. caut input pass -> scriu pass in input password ->
        # 4. caut buton login -> click pe buton login -> login_page.click_login_button()
        login_page.open()
        login_page.set_email(email = "dedjef@chjhcj.com")
        login_page.set_password(password = "bjhcdchbdkc")
        login_page.click_login_button()

'''
Alte teste:
 - test wrong email
 - test no email
 
 
 '''
#