Feature: Tests for product page

  Scenario: User can select colors
    Given Open target product A-91511634  page
    Then Verify user can click through colors


    Scenario: Verify product name and images on search result page
      Given Open Target page
      When locate target search box
      And Input Tea to target search box
      Then Verify each product has a product name and image