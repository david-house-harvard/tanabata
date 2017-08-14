Feature: Team page

  Scenario: Access team page

    Given I an anonymous user
    When I open team page
    Then I can see "aang" foto
    Then I can see "vbucchieri" foto
    Then I can see "jmclaus" foto
    Then I can see "pmcgachey" foto
    Then I can see "dseaton" foto
    Then I can see "dtingley" foto
    Then I can see "sturkay" foto
    Then I can see "eyates" foto
    Then I can see logo "VPAL" with type "jpg"
    Then I can see logo "HUIT" with type "png"
    Then I can see logo "HarvardX" with type "png"
