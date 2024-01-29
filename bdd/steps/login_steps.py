from behave import *

@Given ("I am o the login page")
def step_inpl(context):
    context.login_page.open()

@when ("I enter {email} in the email input")
def step_impl(context, email):
    context.login_page.set_email(email)

@when ("I enter {password} in the password input")
def step_impl(context, password):
    context.login_page.set_password(password)

@when ("I click the login button")
def step_impl(context):
    context.login_page.clock_login_button()

@then ("I should see {message}")
def step_impl(context, message):
    message_displayed = context.login_page.get_login_message()
    assert message_displayed ==  message
    