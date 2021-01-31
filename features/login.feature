Feature: Login

  @wip
  Scenario: Log in link
    Given I am on the Wikipedia homepage
    And I am not logged in
    Then I should see a link to log in

  Scenario: Log in
    Given I am on the Wikipedia homepage
    And I am not logged in
    When I log in
    Then I should be logged in

  Scenario: Logging out
    Given I am on the Wikipedia homepage
    And I am logged in
    When I click the log out link
    Then I will be logged out