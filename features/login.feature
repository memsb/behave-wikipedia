Feature: Login

  Scenario: Log in link
    Given I am on the Wikipedia homepage
    And I am not logged in
    Then I should see a link to log in


  Scenario: Log in requires valid credentials
    Given I am on the Wikipedia homepage
    And I am not logged in
    When I attempt to log in with invalid credentials
    Then I will not be logged in
    And I should see a login error message

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