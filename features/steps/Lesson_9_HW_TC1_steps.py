from behave import given, then


@given('Open Target Help Returns Page')
def open_target_help_returns_page(context):
    context.app.target_help_page.open_help_returns_page()


@then('User selects {help_topic} help topic')
def select_help_topic(context, help_topic: str):
    context.app.target_help_page.select_help_topic(help_topic)


@then('Verify {help_topic} help topic opened')
def verify_help_topic(context, help_topic: str):
    context.app.target_help_page.verify_help_topic(help_topic)
