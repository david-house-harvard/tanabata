Feature: Browse


  Scenario: Access browse page as anonymous

    Given an anonymous user
    When I open main page
    Then I can click on Browse link
    Then I am redirected to the login page


  Scenario: Access browse page

    Given an logged in user
    When I open main page
    Then I can click on Browse link
    Then I can see DART catalog


  Scenario: Content Sources

    Given an logged in user
      And I opened Browse page
      And I saw Content Sources with list group item
    When I can click Harvard YouTube item
    Then I can see only Harvard YouTube item
      And I can see up to 20 cards on a page
    When I click on HarvardX item
    Then I can see only HarvardX item
      And I can see up to 20 cards on a page
      And I can see one item pagination
    Then I can click View All item



  Scenario: Cards

    Given an logged in user
    When I opened Browse page
    Then I can see up to 20 cards on a page
      And each card has name-source
      And each card has image
      And each card has name-course
    When I click on a card
    Then I can see collection page


  Scenario: Content Sources HarvardX

    Given an logged in user
      And I opened Browse page
      And I saw Content Sources with list group item
      And I can see all items pagination
    When I can see more cards than 20 in HarvardX
      And I click on HarvardX item
    Then I can see first 20 cards on a page
      And I can see one item pagination
    When I can click for page number 2 on pagination
    Then I can see next up to 20 cards on a page


  Scenario: Content Sources pagination

    Given an logged in user
      And I opened Browse page
      And I saw Content Sources with list group item
      And I can see number X in HarvardX
      And I can see number Y in YouTube

      """
      users' visit page they should see total number of cards,
      if there are more then 20 cards user should see pagination
      with maximum 20 cards showed on one page
      (count of all items: (X+Y)//20 page links if (X+Y)%20 = 0
      or ((X+Y)//20)+1 otherwise)
      (count of one item: X//20 if X%20 = 0 or (X//20)+1 otherwise)
      """
      And I can see all items pagination
    When I click on HarvardX item
      And I can see more then 20 cards in HarvardX
    Then I can click on all pages in pagination
    When I can click Harvard YouTube item
      And I can see less or equal items then 20
    Then I can click on all pages in pagination
    When I can click View All item
      And I can see more then 20 cards
    Then I can see first 20 cards on a page
      And I can click on all pages in pagination
