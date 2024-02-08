Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Target Homepage
    When Enter Coffee into Target search field
    And Click on Target search icon
    Then Target results for Coffee are shown