Feature: About page

  Scenario: Access about page

    Given an anonymous user
    When I open about page
    Then I can see about_canvas_import_screenshot_indicator.jpg
    Then I can see Harvard_YouTube_ScreenShot.png
    Then I can see DART_Ecosystem_Feb_17.png
    Then I can see SVG
    Then I can click on https://harvard.az1.qualtrics.com link
    Then I can click on https://edx.readthedocs.io link
    Then I can click on http://annotation.chs.harvard.edu/ link
    Then I can click on http://vpal.harvard.edu/research link
    Then I can click on http://huit.harvard.edu/ link
    Then I can click on http://huit.harvard.edu/ link second
    Then I can click on http://harvardx.harvard.edu/ link
    Then I can click on http://vpal.harvard.edu/research link second
    Then I can click on http://vpal.harvard.edu/ link
