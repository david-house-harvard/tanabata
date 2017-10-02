Feature: Browse


  Scenario: Access browse page

    Given an logged in user
    When I open main page
    Then I can click on Browse link
    Then I can see DART catalog


    Scenario: Access browse page as anonymous

    Given an anonymous user
    When I open main page
    Then I can click on Browse link
    Then I am redirected to the login page
