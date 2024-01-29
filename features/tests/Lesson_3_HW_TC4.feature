Feature: Lesson 3 Test Case 4 Scenarios for Target Cart Functionality
  # Enter feature description here

  Scenario: User add an item to the cart and verify it's in the cart
    Given Open Target Homepage
    When Add Coffee To Cart
    Then Verify Coffee Added To Cart