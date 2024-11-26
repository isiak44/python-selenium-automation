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



