Feature: Test Scenarios for Target Sign In Functionality
  # Enter feature description here

  Scenario: User will see "Your cart is empty" when there are no items in the cart page
    Given Open Target Homepage
    When Click on Sign In icon
    Then Click on sidebar Sign In Icon
    Then Verify Sign In form opened