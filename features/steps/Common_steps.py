from behave import given, when


@given('Open Target Homepage')
def open_target_homepage(context):
    context.app.target_homepage.open_target_homepage()


@when('Search for {search_word}')
def homepage_search(context, search_word):
    context.app.target_homepage.execute_search(search_word)
