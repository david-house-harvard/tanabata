Feature: Main page

  Scenario: Access main page

    Given an anonymous user
    When I open main page
    Then I can see harvard-logo-container and click on harvard-logo-container
    Then I can click on an About in header
    Then I can click on a Team in header
    Then I can click on a Coming Soon in header
    Then I can see harvard-logo in footer
    Then I can click on a Privacy
    Then I can click on an Accessibility
    Then I can click on an Report copyright infringement
    Then I can see dart-logo-link and click on dart-logo-link in header
    Then I can see Harvard University DART logo in content-wrapper


  Scenario: Access search on page

    Given an logged in user
    When I open main page
    Then I can type in HomeSearch field in content-wrapper
    Then I can click on search button in content-wrapper
    Then I can see search results


  Scenario: Access search on page as anonymous

    Given an anonymous user
    When I open main page
    Then I can type in HomeSearch field in content-wrapper
    Then I can click on search button in content-wrapper
    Then I am redirected to the login page


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
