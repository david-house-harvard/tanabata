Feature: Search


  Scenario: Access search on page as anonymous

    Given an anonymous user
    When I open main page
    Then I can do search on main page
    Then I am redirected to the login page


  Scenario: Access search on page

    Given an logged in user
    When I open main page
    Then I can do search on main page
    Then I can see search results


  Scenario: Comparison search request with to content

    Given a logged in user
    When I open the main page
    Then I can do search on the main page
    Then I can compare term search result with content
      And I can count all search results with items in sidebar


  Scenario: Search on the search page with filtering

    Given I am on a search page
    When I can do search again on search page
      And I can click on filtering
    Then I can see my search request with Search HarvardX Only filtering
      And I can count filtering search results with items in sidebar


  Scenario: Top courses and filtering

    Given an logged in user
    When I open main page
    Then I can do search on main page
    Then I can see search results on a search page
      And I can see firsts top courses
    When I choose search Harvard Only
      And click on a search again button
    Then I can see firsts top courses include filtering Harvard Only
    Then I can see image with name courses and organization name in this top/hot courses


  Scenario: Tabulated Results

    Given an logged in user
    When I open main page
    Then I can do search on main page
    Then I can see search results on a search page
      And see filtering lists with count search result
    Then I can check all lists items and count them with tabulated results
    Then I can check one results which have name, icons
      And I can click on youtube channel link in one results
      And I can click on a preview video button
      And I can click link on edx course link
      And I can click link on created by is


  Scenario: Responsive

    Given I am on a search page
    When I resize my windows
    Then I can see right location blocks on a page


  Scenario: not found page

    Given I am on a search page
    When I have not to do the right `search again`
    Then I can see `We did not find any videos related to` page
    Then I can click on an Anonymous survey link
