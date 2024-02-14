Feature: Search Results Properties

  Scenario: Search Results Include A Product Title And Image
    Given Open Target Homepage
    When Enter Coffee into Target search field
    And Click on Target search icon
    Then Verify All Results Have Title And Image