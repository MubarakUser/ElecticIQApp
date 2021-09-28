Feature: Cyber attack completely fake statistics
  Scenario: Verify the login
    Given Verify the title of statistics page

  Scenario Outline: Verify sort by name
    Given Clear the filter box
    And Capture the table
    And The Table with some fake data
    When I sort the table by name
    Then Verify the names in ascending order
    And Filter the data by <name>
    Then Capture the filtered table and verify by name
        Examples:
      | name |
      | Man in the Middle|
      | Password attack  |
      | Phishing         |
      |Session hijack    |
      |SQL Injection     |
      |XSS               |

    @complexity
  Scenario Outline: Verify sort by complexity
    Given Clear the filter box
    And Capture the table
    And The Table with some fake data
    When I sort the table by complexity
    Then Verify the complexity in low-medium-high order
    And Filter the data by <complexity>
    Then Capture the filtered table and verify by complexity and its count
    Examples:
      | complexity |
      |low         |
      |medium      |
      |high        |

