# Created by Ooma at 7/9/2020
Feature: A full test suit for Sing In Page
  to be broken down into smaller test cases
  when Framework is set up

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders
    Then Verify Sign-In page is opened


  Scenario: Verify All Static Text On Sign In Page
    When Open Sign-In page
    Then Verify Sign-In page is opened
    And Verify In-Box Email Text is Email (phone for mobile accounts)
    And Verify In-Box Conditions Of Use Text Is By continuing, you agree to Amazon's Conditions of Use and Privacy Notice.
    And Verify Create Amazon Button Text is Create your Amazon account
    And Verify New To Amazon Text is New to Amazon?
    And Verify Footer Text is 1996-2020, Amazon.com, Inc. or its affiliates
    And Verify Continue Button Text Is Continue
    When Click To Assert Need Help Texts
    Then Verify Need Help Text is Need help?
    Then Verify Forgot Your Password Text Is Forgot your password?
    Then Verify Other Issues Text Is Other issues with Sign-In
#    IN BOX BUNDLE


  Scenario:
    When Open Sign-In page
    Then Verify Continue Button Is Clickable

  Scenario:
    When Open Sign-In page
    Then Verify Conditions Of Use Is Clickable

  Scenario:
    When Open Sign-In page
    Then Verify Privacy Notice Is Clickable


  Scenario:
    When Open Sign-In page
    Then Verify Need Help Drop Down Is Functioning: Forgot your password? and Other issues with Sign-In appear and disappear


  Scenario:
    When Open Sign-In page
    When Click To Assert Need Help Texts
    Then Verify Forgot Your Password Is Clickable


  Scenario:
    When Open Sign-In page
    Then Verify Other Issues Is Clickable


  Scenario:
    When Open Sign-In page
    Then Verify Create your Amazon account Button Is Clickable
    # FOOTER BUNDLE


  Scenario:
    When Open Sign-In page
    Then Verify Conditions Of Use In Footer Is Clickable


  Scenario:
    When Open Sign-In page
    Then Verify Privacy Notice In Footer Is Clickable


  Scenario:
    When Open Sign-In page
    Then Verify Footer Help Button Is Clickable