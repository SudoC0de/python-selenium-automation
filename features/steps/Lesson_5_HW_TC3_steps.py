from time import sleep
from behave import then


@then('Verify All Results Have Title And Image')
def verify_all_results_have_title_and_image(context):
    sleep(5) # if this is not included, the whole page loads without loading search results
    product_title_elements_length: int = context.app.target_search_results_page.get_product_title_elements_length()
    product_image_elements_length: int = context.app.target_search_results_page.get_product_image_elements_length()

    if product_title_elements_length == 0 or product_image_elements_length == 0:
        assert False, 'There are no product results available'
    else:
        assert product_title_elements_length == product_image_elements_length,\
            f'Expected {product_title_elements_length} titles and images. Received {product_title_elements_length} titles and {product_image_elements_length} images instead'
