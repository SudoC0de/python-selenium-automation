Feature: Target Sign In Failures

  Scenario: User is shown "Can't Find Account" after entering in invalid credentials
    Given Open Target Homepage
    When Click on Sign In icon
    Then Click on sidebar Sign In Icon
    Then Sign In with invalid credentials
    Then Verify "Can't Find Account" Message is shown