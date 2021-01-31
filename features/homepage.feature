Feature: Homepage

  Scenario: Seeing content sections on home page
    Given I am on the Wikipedia homepage
    Then I should see a welcome message
    And I should see a section titled "On this day"
    And I should see a section titled "In the news"
    And I should see a section titled "From today's featured article"
    And I should see a section titled "Did you know ..."