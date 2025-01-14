Feature: Test for Target User Interaction

  @smoke
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

  @smoke
  Scenario: User Can Verify Empty cart Message
    Given Open Target page
    When Locate and click on cart icon
    Then Verify cart is empty message


  Scenario: User can search for Coffee
    Given Open Target page
    When  input coffee to target search box
    Then  verify coffee in search result
    Then verify search term coffee in current url

  Scenario: Verify user can add product to cart
    Given Open Target page
    When  input coffee to target search box
    And Click on Add to cart button
    And store product name
    And Click Add to cart button from side nav
    And Open target cart page
    Then Verify cart has correct product name


  Scenario: Verify 14 benefit cells in Target circle page
    Given Open Target page
    When Open Target circle page from header
    Then Locate 14 benefit cells


  Scenario: User can open and close Terms and Conditions from sign in page
   Given Open Target page
    When Open signin navigation
    And Click signin button
   When Store original window
   And Click on Target terms and conditions link
   And Switch to the newly opened window
   Then Verify Terms and Conditions page is opened
   And User can close new window and switch back to original


  Scenario: User can select help topic target account
    Given Open target help page for returns
    Then Verify help topic Returns page opened
    When Select help topic Target Account in dropdown
    Then Verify help topic Create account page opened


  Scenario: User can select help topic gift cards
    Given Open target help page for returns
    Then Verify help topic Returns page opened
    When Select help topic Gift Cards in dropdown
    Then Verify help topic Target GiftCard balance page opened


  Scenario: User can not login with invalid credentials
   Given Open Target page
    When Open signin navigation
    And Click signin button
    And Login with an invalid email and password
    Then Verify error message is displayed


  Scenario: User can see favorites tooltip for search results
    Given Open Target page
    When Input Tea to target search box
    And Hover favorites icon
    Then Verify favorites tooltip is shown