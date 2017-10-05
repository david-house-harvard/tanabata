Feature: Search


  Scenario: Access search on page

    Given an logged in user
    When I open main page
    Then I can do search on main page
    Then I can see search results


  Scenario: Access search on page as anonymous

    Given an anonymous user
    When I open main page
    Then I can do search on main page
    Then I am redirected to the login page
