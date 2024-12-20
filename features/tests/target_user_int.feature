Feature: Test for Target User Interaction

  Scenario: Verify Logged Out User Can Access Sign In
    Given Open Target page
    When Open signin navigation
    And Click signin button
    Then Verify signin page pops up


  Scenario: Verify registered user can login successfully
    Given Open Target page
    When Open signin navigation
    And Click signin button
    And Login with a valid email and password
    Then Verify user is logged in successfully


  Scenario: User Can Verify Empty cart Message
    Given Open Target page
    When Locate and click on cart icon
    Then Verify cart is empty message


  Scenario: User can search for Tea
    Given Open Target page
    When  input Tea to target search box
    Then  verify Tea in search result
    Then verify search term Tea in current url

  Scenario: Verify user can add product to cart
    Given Open Target page
    When  input mug to target search box
    And Click on Add to cart button
    And store product name
    And Click Add to cart button from side nav
    And Open target cart page
    Then Verify cart has correct product name


  Scenario: Verify 14 benefit cells in Target circle page
    Given Open Target page
    When Open Target circle page from header
    Then Locate 14 benefit cells

