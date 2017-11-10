Feature: Signup form

  Scenario: Register a new user

    Given an unregistered user
    When I submit a valid email
    Then I am redirected to login success page

    Given an unregistered user
    When I submit an invalid email
    Then I get warning message

    Given an unregistered user
    When I submit a valid twitter credentials
    Then I am redirected to login welcome page