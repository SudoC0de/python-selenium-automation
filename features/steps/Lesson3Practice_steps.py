from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target homepage')
def open_target_homepage(context):
    context.driver.get("https://www.target.com/")
