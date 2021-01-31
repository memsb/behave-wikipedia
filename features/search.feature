Feature: Searching Wikipedia

  Scenario Outline: Searches with multiple results
    Given I am on the Wikipedia homepage
    When I search for "<term>"
    Then I should see a search result for "<result>"

    Examples: Vague searches
      | term        | result                        |
      | newton      | Isaac Newton                  |
      | python      | Python (programming language) |
      | development | Software development          |

  Scenario Outline: Searches that take you directly to a result
    Given I am on the Wikipedia homepage
    When I search for "<term>"
    Then I should be sent to the page for "<page>"

    Examples: Specific searches
      | term       | page       |
      | Bill Gates | Bill Gates |
      | Chalk      | Chalk      |
      | Cheese     | Cheese     |
      | Chess      | Chess      |