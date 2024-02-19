Feature: Search Results Properties

  Scenario: Search Results Include A Product Title And Image
    Given Open Target Homepage
    When Search for Coffee
    Then Verify All Results Have Title And Image