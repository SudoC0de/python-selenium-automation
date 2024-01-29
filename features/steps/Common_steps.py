from behave import given, when, then

@given('Open Target Homepage')
def open_target_homepage(context):
    context.driver.get("https://www.target.com/")