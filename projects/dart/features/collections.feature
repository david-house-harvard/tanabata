Feature: Collections


  Scenario: Access Collections and page title and desc

      Given an logged in user
        And I opened Browse page
      When I open banner edx-collection #use /browse/collections/d09a4ffd-0f14-4016-9747-5f84655e9659 "saving schools mini-course 1"
      Then I can see harvardX Collections name
      Then I can see and click all links in breadcrumbs
      Then I can see card block
        And I can see card image holder
        And I can see metadata holder
        And I can see Launched icon, name and value
        And I can see Creator icon, name and value, I can click on value
        And I can see Content type icon, name and value
        And I can see Subject Area Tags icon, name and value
        And I can see Last updated icon, name and value


  Scenario: Filter Types

      Given an logged in user
        And I opened Browse page
      When I open banner edx-collection
      Then I can see results holder
      Then I can see result filter
      Then I can see filter list Asset Types
      Then I can see filter list Collections Types


  Scenario: Filter Asset Types Total resources

      Given an logged in user
        And I opened Browse page
      When I open banner edx-collection
      Then I can see filter list Asset Types
        And I can see list item Total resources which have icon, name and number
        And I can click on item Total resources
        And I make sure that Total resources number match to pagination and browse tabel lists


  Scenario: Filter Asset Types Problems

      Given an logged in user
        And I opened Browse page
      When I open banner edx-collection
      Then I can see filter list Asset Types
        And I can see list item Problems which have icon, name and number
        And I can click on item Problems
        And I make sure that type Problems equals problem
        And I make sure that Problems number match to pagination and browse tabel lists


  Scenario: Filter Asset Types HTML page

      Given an logged in user
        And I opened Browse page
      When I open banner edx-collection
      Then I can see filter list Asset Types
        And I can see list item HTML pages which have icon, name and number
        And I can click on item HTML pages
        And I make sure that type HTML pages equals html
        And I make sure that HTML pages number match to pagination and browse tabel lists


  Scenario: Filter Asset Types Videos

      Given an logged in user
        And I opened Browse page
      When I open banner edx-collection
      Then I can see filter list Asset Types
        And I can see list item Videos which have icon, name and number
        And I can click on item Videos
        And I make sure that type Videos equals video
        And I make sure that Videos number match to pagination and browse tabel lists


  Scenario: Filter Asset Types Verticals

      Given an logged in user
        And I opened Browse page
      When I open banner edx-collection
      Then I can see filter list Asset Types
        And I can see list item Verticals which have icon, name and number
        And I can click on item Verticals
        And I make sure that type Verticals equals vertical
        And I make sure that Verticals number match to pagination and browse tabel lists


  Scenario: Filter Collection Types

      Given an logged in user
        And I opened Browse page
      When I open banner edx-collection
      Then I can see filter list Collections Types
        And I can see list item Chapters which have icon, name and number
        And I can click on item Chapters
        And I make sure that type Chapters equals chapter
        And I make sure that Chapters number match to pagination and browse tabel lists
        And I can see list item Sequentials which have icon, name and number
        And I can click on item Sequentials
        And I make sure that type Sequentials equals sequential
        And I make sure that Sequentials number match to pagination and browse tabel lists


 Scenario: Table header Tabulated results
