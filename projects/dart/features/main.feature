Feature: Main page

  Scenario: Access main page

    Given an anonymous user
    When I open main page
    Then I can see harvard-logo and click on harvard-logo
    Then I can click on an About in header
    Then I can click on a Team in header
    Then I can see harvard-logo in footer
    Then I can click on a Privacy
    Then I can click on an Accessibility
    Then I can click on an Report copyright infringement
    Then I can see dart-logo-link and click on dart-logo-link in header
    Then I can see Harvard University DART logo in content-wrapper
    Then I can click on Browse link
    Then I can click on Search link
