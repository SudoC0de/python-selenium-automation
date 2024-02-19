Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Target Homepage
    When Search for Coffee
    Then Target results for Coffee are shown