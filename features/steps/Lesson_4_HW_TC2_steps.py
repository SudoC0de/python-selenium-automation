from behave import given, then


@given('Open Target Circle Page')
def open_target_circle_page(context):
    context.app.target_circle_page.open_circle_page()


@then('Verify 5 Benefit Boxes Shown')
def verify_5_benefit_boxes_shown(context):
    benefit_container_count: int = len(context.app.target_circle_page.get_benefit_box_elements())

    assert benefit_container_count == 5, f"Expected 5 benefits but got {benefit_container_count} instead"
