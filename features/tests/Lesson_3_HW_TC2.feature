Feature: Lesson 3 Test Scenarios for Target Cart Functionality

  Scenario: User will see "Your cart is empty" when there are no items in the cart page
    Given Open Target Homepage
    When Click on Cart icon
    Then Cart Empty Message Shown