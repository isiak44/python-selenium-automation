Feature: Test for Target User Interaction

  Scenario: Verify Logged Out User Can Access Sign In
    Given Open Target page
    When Open signin navigation
    And Click signin button
    Then Verify signin page pops up


  Scenario: User Can Verify Empty cart Message
    Given Open Target page
    When Locate and click on cart icon
    Then Verify cart is empty message


  Scenario: User can search for Tea
    Given Open Target page
    When locate target search box
    And  input Tea to target search box
    Then  verify Tea in search result


  Scenario: Verify user can add product to cart
    Given Open Target page
    When locate target search box
    When  input mug to target search box
    And Click on Add to cart button
    And store product price
    And Click Add to cart button from side nav
    And Open target cart page
    Then Verify cart has correct product price


  Scenario: Verify 14 benefit cells in Target circle page
    Given Open Target page
    When Open Target circle page from header
    Then Locate 14 benefit cells