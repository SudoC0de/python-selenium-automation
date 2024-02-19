from behave import given, then


@given('Open Men\'s Knit Shirt Jacket Page')
def open_knitshirt_jacket_page(context):
    context.app.target_mens_knit_shirt_jacket_page.open_page()

@then('Verify Cycling Colors')
def verify_cycling_colors(context):
    context.app.target_mens_knit_shirt_jacket_page.cycle_colors()
